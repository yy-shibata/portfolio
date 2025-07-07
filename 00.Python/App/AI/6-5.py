import sklearn.datasets
import matplotlib.pyplot as plt
dt = sklearn.datasets.load_digits()
print(dt.data.shape)
plt.matshow(dt.images[0])
plt.gray()
plt.show()
