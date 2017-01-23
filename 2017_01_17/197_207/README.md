README FILE
===========
Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2017/README.md


We star tthe analysis where the images have been
corrected for OverScan and Trimming.

## Step 0: Overscan and Trimming
- OverscanAllImages.ipynb do the overscan and trimming from Augustin Guyonnet

## Step 1:

- MakeLogBook.ipynb :  Jupyther notebook making the logbook of the images by reading the fits header of the images.
  - make the list of images making the logbook from the information in the header such as dates, airmasses,.... 

## Step 2:

- ViewAllImages_HD14943.ipynb : Read the raw images provided by Augustin which has been corrected for overscan and trimmed also

## Step 3:

- FindCentralStar_HD14943.ipynb	: find where is the big central star and cut the image:
	- Find all stars in the image using photutils. 
	- The main star has the minimum distance sum wrt to all other sources.

## Step 4:

- FindOptRot_HD14943.ipynb : calculation of angle of rotation

## Step 5:

- Extract_Spectrum_HD14943.ipynb : Really extract the spectrum
(per second). 
	- In fact extract the two +1/-1 orders

## Step 6:
- View_SimSpectrum_HD14943.ipynb : To view simulated spectra and use a single file to save simulated spectra


## Step 7:

- Fit_Spectrum_HD14943.ipynb : Does the fit to get the calibration curve.
   It saves the result of the fit inside a fits file.
   
## Step 8 :
- Calibrate_Spectrum_HD14943.ipynb : Does the calibration of the dispersive axis on the data and save calibrated data in fits file.

## Step 9:
- CompareCalibSim_Spectrum_HD14943_ipynb : Compare reconstructed spectrum with simulation. Note the simulation must be smoothed compared to data spectrum.


## Step 10:
- AnaCalibDataSim_Spectrum_HD14943.ipynb :
- Work on spectra to derive atmospheric studies
- Shows cloud grey attenuation
- Shows H2O variation


## Step 11:
- AnaEqWdtDataSim_Spectrum_HD14943.ipynb:
calculate  the Equivalent Widths


-----



To run python choose anaconda astropyphys
	
