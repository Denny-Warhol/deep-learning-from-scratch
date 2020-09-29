import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/cactus.png')  # read image

plt.imshow(img)
plt.show()
