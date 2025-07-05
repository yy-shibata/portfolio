# スーパークラス
class Fruits:
    def __init__(self,t,p):
        self.title = t
        self.price = p

    def check_price(self,n):
        print(self.title,"は 1パック", self.price, "円です")
        print(n,"パック購入で", self.price * n, "円です")

# サブクラス
class Strawberry(Fruits):
    def __init__(self, t, p,color,taste):
        super().__init__(t, p) # スーパークラスのコンストラクタ使用
        self.color = color
        self.taste = taste

    def check_price(self, n):
        super().check_price(n) # スーパークラスのメソッド使用
    
# サブクラス
class Lemon(Fruits):
    def __init__(self, t, p,color,taste):
        super().__init__(t, p) # スーパークラスのコンストラクタ使用
        self.color = color
        self.taste = taste

    def check_price(self, n):
        # オーバーライド
        print(self.title, "は 1個", self.price, "円です")
        print(n, "個購入で", self.price + n , "円です")

f4 = Strawberry("イチゴ", 498, "赤色", "甘酸っぱい")
print(f4.title,"は",f4.color,"で",f4.taste,"果物です")
f4.check_price(3)

f5 = Lemon("レモン", 198, "黄色", "酸味の強い")
print(f5.title, "は", f5.color, "で",f5.taste,"果物です")
f5.check_price(5)