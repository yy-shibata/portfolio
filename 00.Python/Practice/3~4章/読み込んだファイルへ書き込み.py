f = open("subject.txt", "a+")
print("漢字で教科書名を入力(endで終了)")
input_data = list(iter(input,"end"))
data = "\n".join(input_data) + "\n"
f.write(data)
f.close()
print("end")