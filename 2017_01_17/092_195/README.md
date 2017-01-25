README FILE
===========
Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2017/092_195/README.md


author : Sylvie Dagoret-Campagne
affiliation : LAL/IN2P3/CNRS, France

Last update 2017 January 24th


Object name uder study HD14943
Ronchi grating 400 lines/mm
Telescope CTIO 0.9 m, Focale 12.6 m,F/#=14
FOV : 13.6 arcmin
CCD : 2048 x 2048
24 microns/pixel, 0.4 arcsec/pixel

No filter

## Step 1: Overscan and Trimming
- **OverscanAllImages.ipynb** do the overscan and trimming from Augustin Guyonnet
- should provide the path for the input images
- all the trimmed images are written in the current directory
- the user has to move the trimmed images into the trim_images/ directroy.

## Step 2: Make the Logbook

- **MakeLogBook.ipynb** :  Jupyther notebook making the logbook of the images by reading the fits header of the images.
  - make the list of images making the logbook from the information in the header such as dates, airmasses,....
  - the input path is  trim_images/ directory 
  - the oputput files are csv and fits are important to generate a series of simulated atmosphere
  - pecify the proper object name and infos inside the notebook.

  
##  Step 3: Make Master Bias
-**CTIOAna2017/2017_01_18/BuildMasterBias/MakeMasterBias.ipynb**

produces  MasterBias_CTIO_20170118.fits				
## Step 4 : Make Master Dark
- not done up to now

## Step 5 : Make Master Flat
- **CTIOAna2017/2017_01_18/BuildMasterFlat/MakeMasterFlat.ipynb**

produces  MasterFlat_CTIO_20170118.fits, using  MasterBias_CTIO_20170118.fits				


## Step 6 : Images Reduction
- **ReduceAllImages_HD14943.ipynb** Standard image reduction using ccdproc/astropy package.

Reduces s series of images using previously done
- MasterFlat_CTIO_20170118.fits
- MasterBias_CTIO_20170118.fits	
- input directory : trim_images/
- output directory : reduced_fitsimages/	

## Step 7 : Sky Background subtraction
- **SkyBGSubt_HD14943.ipynb** Subtract the sky background (star and moon light)
- formerly refered as ViewAllImages_HD14943.ipynb : 
- the goal of this is to remove more background.
- Probably this way, based on photutis of removing background is not good.
- it is open to any improvment (better than nothing).
- input path reduced_fitsimages/
- output path processed_fitsimages/
- Don't forget to rename the file according the object name as well inse the object name inside the notebook


## Step 8: Find The location of the target star

- **FindCentralStar_HD14943.ipynb**	: find where is the big central star and cut the image around the region of interest:
	- Find all stars in the image using photutils. 
	- The main star has the minimum distance sum wrt to all other sources.
	- the tests on rotation are switch off because good rotation is performed in next notebook.
- input directory : processed_images/
- output directory : cut_fitsimages/
- don't forget to rename the object_name

## Step 9: Turn the image so the dispersive axis is along X

- **FindOptRot_HD14943.ipynb** : calculation of angle of rotation
This is the first time one can see a 1-D spectrum for check
- We can see the vertical profile also

Carefull check must be done to see how the fit Y vs X is performed. The central star and the borders must be removed.
One must decide if one want one average angle for all images or one rotation angle per image.
- input directory : cut_fitsimages/
- output directory : rotated_fitsimages/

## Step 10: Extract the 1-D spectrum

- **Extract_Spectrum_HD14943.ipynb** : Really extract the spectrum per unit of exposure time (per second). 
- ADU vs x-pixel

	- In fact separate the two +1/-1 orders are used to find the origin of wavelength.
	- Probably some additionnal work is necessary to do more local background subtraction.
	- There is a left spectrum (order -1) and a right spectrum (order +1)
	- The gain between the two order may be different. This has not been implemented.

-input directory : rotated_fitsimages/
-output directory : spectrum_fitsspec/

## Step 11: Control of the Simulated spectra
- **View_SimSpectrum_HD14943.ipynb** : To view simulated spectra and use a single file to save simulated spectra.
This is mandatory because it builds a single fits file with all spectra.

outputfitsfile='AllSimSpectra_'+object_name+'.fits'
The atmosphere had been simulated from the LogBook here
- CTIOAna2017/atmosphere/simulate_transparency_CTIO_ScattAbs_HD14943_2017_01_17_092_195.py
The simulated spectra has been simulated from here:
-CTIOAna2017/simu_spectra/libCTIOSimuObsSpectra.py

 The next step will open this file
- At this stage, next step will need the simulated spectra.
- So the goal here is also to check how looks the simulated spectra.


## Step 12: Calibration in wavelength

- **Fit_Spectrum_HD14943.ipynb** : Does the fit to get the calibration curve pixel <-> wl
- - A second order fit is performed by now
   It saves the result of the fit inside a single fits file.
   Notice the simulated spectra are read.
 - input directory: spectrum_fitspec/
 - output directory: spectrum_calibspec/
 - input simulation :  all fits files for simulated spectrum (may be too large)
 - produce a single file with all fits output.

 Due to the fact too many fits file had been open, the next step has been written
 to open all simlated files at the same time (file produced by  **View_SimSpectrum_HD14943.ipynb**.
   
## Step 13 : Calibration in wavelength 
- **Calibrate_Spectrum_HD14943.ipynb** :  Apply the wavelength calibration calculated by  **Fit_Spectrum_HD14943.ipynb**.
- The calibration of the dispersive axis on the data and save calibrated data in fits file.
- Save Left and Right spectra with wavelength
- input directory: /spectrum_fitsspec
- output directory: /spectrum_calibspec/ 

## Step 14: Compare data/simulation spectra
- **CompareCalibSim_Spectrum_HD14943_ipynb** : Compare reconstructed spectrum with simulation. Note the simulation must be smoothed compared to data spectrum.
Save Left and Right spectra with Sim spectra.
- intput directory: /spectrum_calibspec/ 
- outputdir : spectrum_calibcompsimrealspec/

## Step 15: Does some atmospheric studies over time
- **AnaCalibDataSim_Spectrum_HD14943.ipynb** :
- Work on spectra to derive atmospheric studies
- Shows cloud grey attenuation
- Shows H2O variation
- input dir : spectrum_calibcompsimrealspec/

## Step 16: Equivalent Width
- **AnaEqWdtDataSim_Spectrum_HD14943.ipynb**:
calculate  the Equivalent Widths
input dir : spectrum_calibcompsimrealspec/

-----------------------

- Magic command with ds9:

ds9 -tile -cmap rainbow -zscale  -zoom 0.075  *.fits

To run python choose anaconda astropyphys
	
