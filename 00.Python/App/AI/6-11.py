import PIL.Image
import numpy as np
img = PIL.Image.open("cannon.png")
img_resize = img.resize((8, 8))
img_resize_gray = img_resize.convert("L")
data = np.empty((8, 8), dtype = int)
data = np.array(img_resize_gray)
data = np.round(15 - data / 16, 0)
print(data)
data = np.ravel(data)
print(data)