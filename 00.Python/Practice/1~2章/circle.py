PI = 3.14
r = 0

def circle():
    global r
    r = float(input("円の半径を入力："))
    s = r * r * PI
    return s

x = circle()
print(f"半径{r}の円の面積は{x}です")
print("終了します")