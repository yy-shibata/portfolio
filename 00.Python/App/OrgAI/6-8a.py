import sklearn.datasets
import sklearn.neural_network
import matplotlib.pyplot as plt
dt = sklearn.datasets.load_digits()
X = dt.data
y = dt.target
X_train = int( len(X) * 4 / 5)
X_train_data = dt.data[:X_train]
y_train_data = dt.target[:X_train]
X_test_data = dt.data[X_train:]
X_test_image = dt.images[X_train:]
y_test_data = dt.target[X_train:]
clf = sklearn.neural_network.MLPClassifier(hidden_layer_sizes = 32, solver = "adam", random_state = 0, max_iter = 10000, verbose = False, activation = "logistic", tol = 1e-8, early_stopping = False)
clf.fit(X_train_data, y_train_data)
j = 0
for cnt in range(len(X_test_data)):
    if clf.predict(X_test_data)[cnt] != y_test_data[cnt]:
        j += 1
fig, axes = plt.subplots(int(j / 5) + 1, 5, tight_layout = True, figsize = (8, 8), dpi = 64)
i = 0
plt.gray()
for cnt in range(len(X_test_data)):
    if clf.predict(X_test_data)[cnt] != y_test_data[cnt]:
        axes[int(i / 5), int(i % 5)].matshow(X_test_image[cnt])
        axes[int(i / 5), int(i % 5)].xaxis.set_visible(False)
        axes[int(i / 5), int(i % 5)].yaxis.set_visible(False)
        axes[int(i / 5), int(i % 5)].set_title("pre:" + str(clf.predict(X_test_data)[cnt]))
        i += 1
plt.show()