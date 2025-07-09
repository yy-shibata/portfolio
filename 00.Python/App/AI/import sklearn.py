import sklearn.datasets
import matplotlib.pyplot as plt
# disitsの読み込み
dt = sklearn.datasets.load_digits()
print(dt.data.shape)
#準備したが層を画面に表示する
plt.matshow(dt.images[0])
plt.gray()
plt.show()