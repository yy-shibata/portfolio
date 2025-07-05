n = 0
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    print(n)
    n += 1
print("終了します")