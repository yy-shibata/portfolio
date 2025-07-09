import sklearn.datasets
dt = sklearn.datasets.load_digits()
print(dt.data[0])
print(dt.images[0])
print(dt.target[0])