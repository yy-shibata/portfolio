import sklearn.datasets
dt = sklearn.datasets.load_digits()
X = dt.data
y = dt.target
X_train = int( len(X) * 4 / 5)
X_train_data = dt.data[:X_train]
y_train_data = dt.target[:X_train]
print("練習用データ[" + str(X_train - 1) + "] = " + str(X_train_data[X_train - 1]))
print("練習用解答[" + str(X_train - 1) + "] = " + str(y_train_data[X_train - 1]))
X_test_data = dt.data[X_train:]
y_test_data = dt.target[X_train:]
print("試験用データ[" + str(len(X) - X_train - 1) + "] = " + str(X_test_data[len(X) - X_train - 1]))
print("試験用解答[" + str(len(X) - X_train - 1) + "] = " + str(y_test_data[len(X) - X_train - 1]))