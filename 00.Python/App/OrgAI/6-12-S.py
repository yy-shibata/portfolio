import PIL.Image
import numpy as np
import sklearn.datasets
import sklearn.svm
import matplotlib.pyplot as plt

dt = sklearn.datasets.load_digits()
X_train_data = dt.data
y_train_data = dt.target

X_test_image = np.round(16 - np.array(PIL.Image.open("0.png").resize((8, 8)).convert("L")) / 16, 0)
X_test_data = np.ravel(X_test_image)
y_test_data = [0]

for i in range(9):
    data = np.round(16 - np.array(PIL.Image.open(str(i + 1) + ".png").resize((8, 8)).convert("L")) / 16, 0)
    X_test_image = np.block([[[X_test_image]], [[data]]])
    X_test_data = np.vstack((X_test_data, np.ravel(data)))
    y_test_data = np.append(arr = y_test_data, values = i + 1)

clf = sklearn.svm.SVC(random_state = 0, gamma = 0.00001, C = 1)
clf.fit(X_train_data, y_train_data)

fig, axes = plt.subplots(2, 5, tight_layout = True, figsize = (8, 8), dpi = 64)
plt.gray()
for cnt in range(10):
    axes[int(cnt / 5), int(cnt % 5)].matshow(X_test_image[cnt])
    axes[int(cnt / 5), int(cnt % 5)].xaxis.set_visible(False)
    axes[int(cnt / 5), int(cnt % 5)].yaxis.set_visible(False)
    axes[int(cnt / 5), int(cnt % 5)].set_title("pre:" + str(clf.predict(X_test_data)[cnt]))
    i += 1
plt.show()