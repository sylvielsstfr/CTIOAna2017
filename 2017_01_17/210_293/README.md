README FILE
===========
Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2017/210_293/README.md

Last update 2017 January 24th


Object name uder study HD60773
Ronchi grating 400 lines/mm
Telescope CTIO 0.9 m, Focale 12.6 m,F/#=14
FOV : 13.6 arcmin
CCD : 2048 x 2048
24 microns/pixel, 0.4 arcsec/pixel

No filter

## Step 1: Overscan and Trimming
- OverscanAllImages.ipynb do the overscan and trimming from Augustin Guyonnet
- should provide the path for the input images
- all the trimmed images are written in the current directory
- the user has to move the trimmed images into the trim_images/ directroy.

## Step 2: Make the Logbook

- MakeLogBook.ipynb :  Jupyther notebook making the logbook of the images by reading the fits header of the images.
  - make the list of images making the logbook from the information in the header such as dates, airmasses,....
  - the input path is the trim_images/ directory 
  - the oputput files are csv and fits are important to generate a series of simulated atmosphere
  - - specify the proper object name and infos inside the notebook.

  
##  Step 3: Make Master Bias
-CTIOAna2017/2017_01_18/BuildMasterBias/MakeMasterBias.ipynb

produces  MasterBias_CTIO_20170118.fits				
## Step 4 : Make Master Dark
- not done up to now

## Step 5 : Make Master Flat
- CTIOAna2017/2017_01_18/BuildMasterFlat/MakeMasterFlat.ipynb

produces  MasterFlat_CTIO_20170118.fits, using  MasterBias_CTIO_20170118.fits				


## Step 6 : Images Reduction
- ReduceAllImages_HD14943.ipynb

Reduces s series of images using peviously done
- MasterFlat_CTIO_20170118.fits
- MasterBias_CTIO_20170118.fits		

## Step 7 : Sky Background subtraction
- SkyBGSubt_HD14943.ipynb
- formerly refered as ViewAllImages_HD14943.ipynb : 
- the goal of this is to remove more background.
- Probably this way, based on photutis of removing background is not good.
- it is open to any improvment (better than nothing).
- input path trim_images/
- output path processed_fitsimages/
- Don't forget to rename the file according the object name as well inse the object name inside the notebook


## Step 8: Find The location of the target star

- FindCentralStar_HD14943.ipynb	: find where is the big central star and cut the image around the region of interest:
	- Find all stars in the image using photutils. 
	- The main star has the minimum distance sum wrt to all other sources.
	- the tests on rotation are switch off because good rotation is performed in next notebook.
- input directory : processed_images/
- output directory : cut_fitsimages/
- don't forget to rename the object_name

## Step 9: Turn the image so the dispersive axis is along X

- FindOptRot_HD14943.ipynb : calculation of angle of rotation

## Step 10: Extract the 1-D spectrum

- Extract_Spectrum_HD14943.ipynb : Really extract the spectrum
(per second). 
	- In fact extract the two +1/-1 orders

## Step 11: Control of the Simulated spectra
- View_SimSpectrum_HD14943.ipynb : To view simulated spectra and use a single file to save simulated spectra


## Step 12: Calibration in wavelength

- Fit_Spectrum_HD14943.ipynb : Does the fit to get the calibration curve.
   It saves the result of the fit inside a fits file.
   
## Step 13 : Don't remember but necessary
- Calibrate_Spectrum_HD14943.ipynb : Does the calibration of the dispersive axis on the data and save calibrated data in fits file.

## Step 14: Compare data/simulation spectra
- CompareCalibSim_Spectrum_HD14943_ipynb : Compare reconstructed spectrum with simulation. Note the simulation must be smoothed compared to data spectrum.


## Step 15: Does some atmospheric studies over time
- AnaCalibDataSim_Spectrum_HD14943.ipynb :
- Work on spectra to derive atmospheric studies
- Shows cloud grey attenuation
- Shows H2O variation


## Step 16: Equivalent Width
- AnaEqWdtDataSim_Spectrum_HD14943.ipynb:
calculate  the Equivalent Widths


-----

- Magic command with ds9:

ds9 -tile -cmap rainbow -zscale  -zoom 0.075  *.fits

To run python choose anaconda astropyphys
	
