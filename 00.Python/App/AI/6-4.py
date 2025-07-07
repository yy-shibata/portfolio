import sklearn.datasets
import matplotlib.pyplot as plt
dt = sklearn.datasets.load_digits()
plt.matshow(dt.images[0])
plt.show()