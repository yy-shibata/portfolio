import sklearn.datasets
import sklearn.svm
dt = sklearn.datasets.load_digits()
X = dt.data
y = dt.target
X_train = int( len(X) * 4 / 5)
X_train_data = dt.data[:X_train]
y_train_data = dt.target[:X_train]
X_test_data = dt.data[X_train:]
y_test_data = dt.target[X_train:]
clf = sklearn.svm.SVC(random_state = 0, gamma = 0.00001, C = 1)
clf.fit(X_train_data, y_train_data)
print(clf.score(X_test_data, y_test_data))