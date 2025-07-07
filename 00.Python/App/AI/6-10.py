import PIL.Image
import matplotlib.pyplot as plt
img = PIL.Image.open("cannon.png")
img_resize = img.resize((8, 8))
img_resize_gray = img_resize.convert("LA")
plt.imshow(img_resize_gray)
plt.show()