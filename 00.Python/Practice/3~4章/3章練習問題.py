# ファイルを列単位で読み込む
f = open("japan.txt", "r")
for data in f:
    print(data, end="")
f.close()
print("end")