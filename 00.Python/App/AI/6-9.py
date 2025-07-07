import sklearn.datasets
import sklearn.neural_network
import sklearn.metrics
import matplotlib.pyplot as plt
dt = sklearn.datasets.load_digits()
X = dt.data
y = dt.target
X_train = int( len(X) * 4 / 5)
X_train_data = dt.data[:X_train]
y_train_data = dt.target[:X_train]
X_test_data = dt.data[X_train:]
y_test_data = dt.target[X_train:]
clf = sklearn.neural_network.MLPClassifier(hidden_layer_sizes = 32, solver = "adam", random_state = 0, max_iter = 10000, verbose = False, activation = "logistic", tol = 1e-8, early_stopping = False)
clf.fit(X_train_data, y_train_data)
sklearn.metrics.plot_confusion_matrix(clf, X_test_data, y_test_data)
plt.show()