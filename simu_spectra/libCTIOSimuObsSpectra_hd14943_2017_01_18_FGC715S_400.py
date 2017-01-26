"""
libCTIOSimoObsSpectra.py
=============----


author : Sylvie Dagoret-Campagne
affiliation : LAL/CNRS/IN2P3/FRANCE
Collaboration : DESC-LSST


Purpose : Simulate the observed spectra at CTIO

"""


import os
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.io import ascii
import os
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
import libCTIOSpectra as transp

#---------------------------------------------------------------------------------
# DATA BLOCK 

#
filepath_qe='../Telescope'
filename_qe = "qecurve.txt"  

###################################################################
##    OBJECT HD14943
## 
obj_name='HD14943'  # November 2016
#SED
filepath_sed='/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOData2016/SEDCalspec_HD14943'
filename_sed='hd14943_stis_003.fits'
######################################################

####################################################################
# ATMOSPHERE
filepath_atm="/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2017/atmosphere/simulations/RT/2.0/CT/pp/us/sa/rt/y2016/m01/2017_01_18/FGC715S_400/out"
####################################################################                                                                                  
filename_atm="RT_CT_pp_us_sa_rt_HD14943_Nev1_y2016_m01_aver.OUT"
filename_keysel= "^RT_CT_pp_us_sa_rt_HD14943_Nev(.+)_y2016_m.*OUT$"  # regular expressioon

###############################################################
# LOGBOOK
filepath_lb='/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2017/2017_01_18/FGC715S_400'
filename_lb='logbk_HD14943_ctio2017Jan18_FGC715S_400.fits'
################################################################

#####################################################
# OUTPUT
outputdir = 'fits/HD14943/2017_01_18/FGC715S_400'
####################################################

#-------------------------------------------------------------------------------

############################################################################
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(f):
        os.makedirs(f)
#########################################################################


#---------------------------------------------------------------------------------
if __name__ == "__main__":




    ensure_dir(outputdir)

    atm_files = [f for f in os.listdir(filepath_atm) if f.endswith('aver.OUT')] 
    atm_files=np.array(atm_files)
    
    print 
    # extract the number of files according which the filenames must be sorted
    number_files = []
    selected_files = []
    for file in atm_files:
        num_str=re.findall('^RT_CT_pp_us_sa_rt_HD14943_Nev(.+)_y2016_m.*OUT$',file)
        print num_str[0]

        if len(num_str) != 0:
            print "found file {} !!!! ".format(file) 
            number_files.append(int(num_str[0]))
            selected_files.append(file)
            
            
            
    number_files=np.array(number_files)
    selected_files=np.array(selected_files)
    #print atm_files
    print 'original file numbering= =',number_files
    
    # indexes in order to sort the number_files
    ordered_number=np.argsort(number_files)      
    print 'mapping to order files = ',ordered_number    
    
    # check the ordering according ordered_number is OK
    new_numbers=number_files[ordered_number]
    print 'check ordering is OK = ', new_numbers
    
    # order the filenames according ordered_number
    ordered_files=selected_files[ordered_number]
    print 'ordered_files = ',  ordered_files
    
    # get quantum efficiency of the detector
    fullfilename_qe=os.path.join(filepath_qe,filename_qe)  
    wl_qe,qe=transp.Get_QE(fullfilename_qe)
    
    fullfilename_sed=os.path.join(filepath_sed,filename_sed)
    wl_sed,sed=transp.Get_SED(fullfilename_sed)
    
    
    qe_out=transp.ComputeQE(wl_sed,wl_qe,qe)    
    
    
    logbook=os.path.join(filepath_lb,filename_lb) 
    hdulist=fits.open(logbook)
    
    table_data=hdulist[1].data
    print table_data.columns 
    airmass=table_data['airmass']
    date=table_data['date']
    expo=table_data['exposure']
    datafile=table_data['filename']

    # loop on files
    for idx,atm_file in np.ndenumerate(ordered_files):
        print idx[0], atm_file
        file_fits=re.findall("(.*).OUT$",atm_file)[0]+'_spectra.fits'
        print file_fits
    
        fullatmfile=os.path.join(filepath_atm,atm_file)
        
        wl_atm,atm=transp.Get_Atm(fullatmfile)
        
        atm_out=transp.ComputeAtm(wl_sed,wl_atm,atm)
        
        spectra=transp.ComputeSEDxAtmxQE(wl_sed,sed,wl_atm,atm,wl_qe,qe)
        
        prim_hdr=fits.Header()
        prim_hdr['OBJ_NAME']=obj_name
        prim_hdr['AIRMASS']=airmass[idx[0]]
        prim_hdr['UNITS']='wavelength in nm'
        prim_hdr['DATE']=date[idx[0]]
        prim_hdr['EXPOSURE']=expo[idx[0]]
        prim_hdr['FILENAME']=datafile[idx[0]] 
        prim_hdr['COMMENT']="Prediction of observable SPECTRA"
        primhdu=fits.PrimaryHDU(header=prim_hdr)
    
        col1 = fits.Column(name='WAVELENGTH', format='E', array=wl_sed)
        col2 = fits.Column(name='SEDcalspec', format='E', array=sed)
        col3 = fits.Column(name='Atmosphere', format='E', array=atm_out)
        col4 = fits.Column(name='QE', format='E', array=qe_out)
        col5 = fits.Column(name='SEDxQExATM', format='E', array=spectra)
        
        cols = fits.ColDefs([col1, col2,col3,col4,col5])
        tbhdu = fits.BinTableHDU.from_columns(cols)     # new binary table HDU
        thdulist = fits.HDUList([primhdu, tbhdu])

        output_fits_file=os.path.join(outputdir,file_fits)
        
        thdulist.writeto(output_fits_file,clobber=True)
        
