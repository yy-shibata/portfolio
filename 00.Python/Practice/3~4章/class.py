class Fruits:
    def __init__(self,t,p):
        self.title = t
        self.price = p

    def check_price(self,n):
        print(self.title,"は 1パック", self.price, "円です")
        print(n,"パック購入で", self.price * n, "円です")

f2 = Fruits("イチゴ", 498)
f2.check_price(3)