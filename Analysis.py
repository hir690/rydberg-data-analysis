#*************************************************************
# 
# Experiment: Determination of the Rydberg constant
#             (Analysis script)
# Names:      Hira Chaudhry  
# Date:       02/03/2026
#
#*************************************************************
import numpy as np
import matplotlib.pyplot as plt
import lab1


#********************************************************
# In this script it will be helpful to plot your data in 
# an external figure window, which provides a ZOOM option.
# 
# You can plot a figure inline (in your console output) 
# or external (in a separate figure). 
#
# To toggle between the two modes, please type 
# IN YOUR CONSOLE the commands:
# %matplotlib qt             plot in external figure
# %matplotlib inline         plot in internal figure
#
# Use the inline mode for the final printing command.

#********************************************************
# Load your image with the hydrogen spectrum and display it
#
# (a) Open new figure with  plt.figure(1)
plt.figure(1)
# (b) Load and diplay your spectroscopy image for hydrogen.
img = plt.imread("Hydrogen3.png")
plt.imshow(img)
#********************************************************






#********************************************************
# The spectrum covers only a small part of the image
# and it is helpful to select a certain range on the
# y-axis. 
#
# On the y-axis of the picture, identfy the y-values of the
# pixel at the top and bottom of the spectrum. 
#
# (Typically the values are identical to the values in the 
# calibration script)
#
# Select the useful horizontal slice of the hydrogen image
#
#          imgCut = lab1.selectHSlice( ... )
# 
# (a) Define y0Pix and y1Pix
# (b) Open a new figure with plt.figure(2)
# (c) Cut a horizontal slice that contains the spectrum
# (d) Display the slice
#
#********************************************************
y0Pix = 100
y1Pix = 320

plt.figure(2)
imgCut = lab1.selectHSlice(img, y0Pix, y1Pix)
plt.imshow(imgCut)





#********************************************************
# Project the cut image onto the x-axis", i.e. use
#
#        pixPos,specInt = lab1.projectXAxis(imgCut)
#
# Convert the pixel position to wavelengths. Use the 
# previously determined linear relationship.
#
# (a) Project onto x-axis, create vectors: pixPos, specInt
# (b) Convert pixPos to wavelengths
#          - define parameters of line
#                   m = ... 
#                   c = ...
#          - calculate weavelengths
#                   waveLength = m * pixPos + c
#********************************************************

pixPos,specInt = lab1.projectXAxis(imgCut)

m = 0.7847595245019967
c = 286.65618321805493

waveLength = m * pixPos + c

#********************************************************
# Plot your hydrogen sepctrum data with the correct
# wavelengths.
#
# (a) Create figure window 4 with plt.figure(3)
# (b) Plot waveLength on the x-axis
# (c) Plot specInt on the y-axis
# (d) use the line symbol '-'
# (e) provide useful labels and title
#
#********************************************************

plt.figure(3)
plt.plot(waveLength,specInt,'-')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb.)')
plt.title('Spectrum of a Hydrogen Lamp')





#<----------------- Calculate the Rydberg constant  ---------------------->


#********************************************************
# Calculate the Rydberg constant with eq. 2
#
# Define the necessary variables
# M  = ...   (mass)             
# eC = ...
# h  = ...
# epsilon0 = ... 
# V  = ...   (velocity of light)
#
# (do not use variable names "e" or "E" - it is used for 
# the scientific notation)
#
# Use eq. 2 to calculate:
# R = ...
#********************************************************

M = 9.109 * 10**-31 # kg  
eC = -1.602 * 10**-19 # C
h  = 6.626 * 10**-34 # Js
epsilon0 =  8.854 * 10**-12 # F/m
V = 3.00 * 10**8 #m/s

R = (M * eC**4) / (8 * epsilon0**2 * h**3 * V)


#********************************************************
# Calculate the wavelength of the two lines of the Balmer 
# series
#
# Ba_alpha (n1=3->n2=2)
# Ba_beta  (n1=4->n2=2)
#
# Suggestion:
#
# Define n1 and n2 and use eq.4
# lambdaA = ...
# lambdaB = ...
#
#********************************************************


lambdaA = 1 / (R * (1/2**2 - 1/4**2))

lambdaB = 1 / (R * (1/2**2 - 1/3**2))




#********************************************************
# Identify the Ba-alpha and the Ba-beta transitions
# in your spectrum and the their wave lengths.
# (Zoom into your figure 3 is necessary)
#
# (1) Get the wave length of Ba-alpha and Ba-beta as calculated
#     at the begining of the script (lambdaA, and lambdaB)
# (2) Identify the corresponding peaks in your sepctrum 
# (2) Use the ZOOM button in the external plot figure to get
#     the wave lengths of the peaks
# 
# Suggestion: 
# lambdaAMeas = ...
# lambdaBMeas = ...
#********************************************************

lambdaAMeas = 453.811e-9
lambdaBMeas = 626.461e-9




#********************************************************
# Calculate the Rydberg constant from each of the two
# measured wave lengths
#
# Suggestion create variables
# RA = 1/lambdaAMeas / (...)
# RB = 1/lambdaBMeas / (...)
#
#********************************************************

RA = 1 / (lambdaAMeas * (1/2**2 - 1/4**2))
RB = 1 / (lambdaBMeas * (1/2**2 - 1/3**2))




#********************************************************
# From your plot figure 3, estimate the reading error of the 
# wavelengths of your peaks. Ues the ZOOM button if
# necessary.
#
# Dlambda = 
# 
# Calclate the error R using
# Delta R/R = Delta lambda/lambda
#
# DRA = ...
# DRB = ...
#********************************************************
  
Dlambda = 0.525e-9 # nm --> m  #(454.61 - 453.56)/2

DRA = (RA * (Dlambda/lambdaAMeas))
DRB = (RB * (Dlambda/lambdaBMeas))




#************************************************************
#
# Suggestion: 
# print( "Rydberg constant: RA =({0:.7e} +- {1:.7})  UNITS".format(RA,DRA) )
# print( "Rydberg constant: RB (={0:.7e} +- {1:.7})  UNITS".format(RB,DRB) ) 
# (use currect UNITS)
#
#************************************************************
print( "Rydberg constant: RA =({0:.7e} ± {1:.7})  m-1".format(RA,DRA) )
print( "Rydberg constant: RB (={0:.7e} ± {1:.7})  m-1".format(RB,DRB) )

