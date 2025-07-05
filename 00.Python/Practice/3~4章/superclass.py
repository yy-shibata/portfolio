class Fruits:
    def __init__(self,t,p):
        self.title = t
        self.price = p

    def check_price(self,n):
        print(self.title,"は 1パック", self.price, "円です")
        print(n,"パック購入で", self.price * n, "円です")

class Strawberry(Fruits):
    color = "赤色"
    taste = "甘酸っぱい"

f3 = Strawberry("イチゴ", 498)
print(f3.title, "は", f3.color, "で", f3.taste, "果物です")
f3.check_price(3)