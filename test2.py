import matplotlib.pyplot as plt
from skimage import io, filters, measure
from scipy import ndimage

# Opening the image
im1 = io.imread('sampleimage4.jpg', as_grey=True)

# Otsu thresholding method
val = filters.threshold_otsu(im1)

# Function that fills in the holes of the image
drops = ndimage.binary_fill_holes(im1 < val)
plt.imshow(drops, cmap='gray')
plt.show()

# Counting the number of blobs
labels = measure.label(drops)
print(labels.max())
print('Coverage is %f' %(drops.mean()))