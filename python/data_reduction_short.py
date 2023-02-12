# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:25:23 2023

@author: Group 3
"""




import numpy as np, glob, astropy.io.fits as fits
science_df = (np.array([fits.getdata(path) for path in glob.glob("data/H/VIRCAM_H_SCIENCE_DIT2.0_NDIT25*.fits")]) - fits.getdata("data/masterdark_H_dit2_ndit25.fits"))/fits.getdata("data/masterflat_H_dit3_ndit1.fits")
science_df_destriped = [[s[i] - np.nanmedian(s[i]) + np.nanmedian(s) for i in range(0, 2048)] for s in science_df]
i = 1
for s in np.array([s - np.nanmedian(np.array([s - np.nanmedian(s) for s in science_df]), axis=0) for s in science_df_destriped]):
    if i < 10:
        fits.writeto("data/science_H/VIRCAM_H_SCIENCE_DIT2.0_NDIT25_"+str(0)+str(i)+".fits", data=s, header = fits.Header(fits.open(np.array(glob.glob("data/H/VIRCAM_H_SCIENCE_DIT2.0_NDIT25*.fits"))[i-1])[0].header), overwrite=True)
    else:
        fits.writeto("data/science_H/VIRCAM_H_SCIENCE_DIT2.0_NDIT25_"+str(i)+".fits",data=s, header = fits.Header(fits.open(np.array(glob.glob("data/H/VIRCAM_H_SCIENCE_DIT2.0_NDIT25*.fits"))[i-1])[0].header),overwrite=True)
    i += 1