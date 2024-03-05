import warnings

warnings.filterwarnings('ignore')
from scipy import misc
import imageio
import numpy as np
from matplotlib import pyplot as plt  # For image viewing
import cv2

# !/usr/bin/python
import getopt
import sys

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap

# dng reading requires libraw to work

# Open an image
image = cv2.imread('Capture.JPG')

plt.show()
# Get the red band from the rgb image, and open it as a numpy matrix
# NIR = image[:, :, 0]

# ir = np.asarray(NIR, float)


ir = (image[255, :, 0]).astype('float')

# Get one of the IR image bands (all bands should be same)
# blue = image[:, :, 2]

# r = np.asarray(blue, float)

r = (image[:, :, 2]).astype('float')

# Create a numpy matrix of zeros to hold the calculated NDVI values for each pixel
ndvi = np.zeros(r.size)  # The NDVI image will be the same size as the input image

# Calculate NDVI
ndvi = np.true_divide(np.subtract(ir, r), np.add(ir, r))

# Display the results
output_name = 'NDVI_show.jpg'

# grayscale color palette to showcase NDVI
cols = ['red', 'orange', 'yellow', 'green']


def create_colormap(args):
    return LinearSegmentedColormap.from_list(name='custom1', colors=cols)


# colour bar to match grayscale units
def create_colorbar(fig, image):
    position = fig.add_axes([0.125, 0.19, 0.2, 0.05])
    norm = colors.Normalize(vmin=-1., vmax=1.)
    cbar = plt.colorbar(image,
                        cax=position,
                        orientation='horizontal',
                        norm=norm)
    cbar.ax.tick_params(labelsize=6)
    tick_locator = ticker.MaxNLocator(nbins=3)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.set_label("NDVI", fontsize=10, x=0.5, y=0.5, labelpad=-25)


fig, ax = plt.subplots()
image = ax.imshow(ndvi, cmap=create_colormap(colors))
plt.axis('off')

create_colorbar(fig, image)

extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(output_name, dpi=600, transparent=True, bbox_inches=extent, pad_inches=0)
plt.show()
