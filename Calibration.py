#*************************************************************
# 
# Experiment: E7, Determination of the Rydberg constant
#             (Calibration script)
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
#
#


#********************************************************
# An gray image is just a 2D-array with numbers (gray values) 
# that indicate the intensity at a certain position.
# The smallest unit with a single intensity value is 
# called a "pixel".
#
# You can load am image file with name "Mercury.png" 
# with the command
#         img = plt.imread("Mercury.png")    
# You can display the image with the command
#         plt.imshow( img )
#
# (a) open new figure with: plt.figure(1)
plt.figure(1)
# (b) Load and diplay your spectroscopy image for mercury.
img = plt.imread("Mercury.png")
plt.imshow(img)
# (c) Inspect the new figure, the figure menu and the image
# (d) Use the magnifyer logo to zoom into the image
# (e) Repeat the zoom until you observe single pixels (just info)
# (f) Use the logos for arrows or home to zoom out
# (g) The pixel number on the x-axis and y-axis are given
#     by tick marks. 
#********************************************************



#********************************************************
# The spectrum covers only a small part of the image
# and it is helpful to select a certain range on the
# y-axis. 
# On the y-axis of the picture, identfy the pixel y-values 
# at the start and stop of the spectrum. (Typically pixels 
# are approximately 120 to 300)
#
# Suggestion:
# y0Pix = ...
# y1Pix = ...
#********************************************************

y0Pix = 135
y1Pix = 235

#********************************************************
# You can select a horizontal slice of an image with
# the support function
#      imgCut = lab1.selectHSlice(img, y0Pix, y1Pix)
# 
# - Open a new figure with plt.figure(2)
# - Cut a horizontal slice that contains the spectrum
# - Display the slice
#
# Suggestion:
# plt.figure(2)
# imgCut = lab1.selectHSlice(...)
# plt.imshow( ... )
#********************************************************

plt.figure(2)
imgCut = lab1.selectHSlice(img, y0Pix, y1Pix)
plt.imshow(imgCut)


#********************************************************
# Your goal is to identify the x-position of the 
# spectral lines (which run along the y-axis of the image).
#
# It is helpful to "project the image onto the x-axis", i.e. 
# to sum all pixel values at the same x-position. You can
# use to sum() command or the following support function
#
#        xVect,yVect = lab1.projectXAxis(imgCut)
#
# The function returns two vectors
#  xVect - provides the pixel number on the x-axis, e.g.
#          0,1,2,...
#  yVect - provides the sum of all pixel values at the same
#          x-position
#
# (a) create figure 3
# (b) Project the cut image onto the x-axis
#      - create vectors "pixPos" and "specInt"
#        for the "pixel-position" and the "spectral intensity"
# (c) Plot pixPos vs. specInt with a line symbol
# (d) Add axis labels
#
# Suggestion:
# plt.figure(3)
# pixPos,specInt = lab1.projectXAxis(imgCut)
# plt.plot(pixPos,specInt)
# plt.xlabel('Pixel position')
# plt.ylabel('Intensity (arb.)')
#
#********************************************************

plt.figure(3)
pixPos,specInt = lab1.projectXAxis(imgCut)
plt.plot(pixPos,specInt)
plt.xlabel('Pixel position')
plt.ylabel('Intensity (arb.)')


#********************************************************
# Find the strongest peaks of the mercury spectrum with known
# wave lengths. 
#
# Use the figure in the script to identify the 4 transitions 
# with wave lengths of 
#     404.3nm, 436.1nm,  
#     546.2nm, 579.4 nm,
# and determine the corresponding pixel positions 
# 
# It might be helpful to magnify certain sections of your 
# plot. You can use the magnifyer button in external figures to
# enlarge the view.
#
# Create two vectors to relate pixel position of the lines (pixLines) and
# the known wave lengths (waveLines).
# 
# Suggestion:
# waveLines = np.array([404.3,436.1,...,...])
# pixLines  = np.array([...,...,...,...])
#
#***********************************************************

waveLines = np.array([404.3,436.1,546.2,579.4])
pixLines  = np.array([150.00, 190.04, 332.02, 372.05])



#********************************************************
# An uncalibrated spectrometer can only provide the pixel 
# position of the emission lines on a camera image, but not the 
# corresponding wave lengths. 
# There is a linear relationship between the pixel position 
# and the corresponding wave length, and you task is to 
# determine the slope "m" and the offset "c" of this relationship.
#
# e.g.       waveLines = m * pixLines + c  
#  
# Use a linear fit to determine m and c.
#
# (1) It might be helpful to start with a plot of your arrays 
# pixLines and waveLines. Use the command "plt.figure(4)" to 
# generate a new figure. 
# (2) use "lab1.fitLine()" to determine "m" and "c"
# (3) plot your fit result on top of your data, i.e. generate
# a few x-data points and the corresponding y-data points and
# plot a line on top of your data.
# 
# Suggestions:
#    c,m,dm = lab1.fitLine(...)
#    xr = np.linspace(...)
#    yr = ...
#    plt.plot(xr,yr,'r-')
#    plt.xlabel(...)
#    plt.ylabel(...)
#    plt.title(...)
#
#************************************************************

plt.figure(4)
c,m,dm = lab1.fitLine(pixLines, waveLines)
plt.plot(pixLines, waveLines,"bo")
xr = np.linspace(min(pixLines), max(pixLines), 100)
yr = xr * m + c 
plt.plot(xr,yr,'r-')
plt.xlabel('Pixel position')
plt.ylabel('Wavelength (nm)')
plt.title('Spectrum of a Mercury Lamp')


#************************************************************
# Please record the final values for your fit.
# You are going to use the values in the next script.
#
# m = ...
# c = ...
# dm = ... 
# 
# y0Pix = ...  
# y1Pix = ...
#
# Suggestion
# print( "Image processing: y0 ={0:.2f}, y1 = {1:.2f}".format(y0Pix,y1Pix) ) 
# print( "Fit parameters: m ={0:.7f} +- {1:.7f}, c={2:.7e}".format(m,dm,c) ) 
#************************************************************

m = 0.7847595245019967
c = 286.65618321805493
dm = 0.0049804656013411755


y0Pix = 135
y1Pix = 235

print( "Image processing: y0 ={0:.2f}, y1 = {1:.2f}".format(y0Pix,y1Pix) ) 
print( "Fit parameters: m ={0:.7f}  ± {1:.7f}, c = {2:.7f}".format(m,dm,c) ) 
