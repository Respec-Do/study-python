# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(self.name, self.price)



class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def selling_product(self,customer):
        selling_price = round(self.product.price * (100 - customer.discount_rate) / 100)
        return selling_price

    def remaining_cash(self,customer):
        customer.cash -= selling_price
        return customer.cash



class Customer:
    def __init__(self, name, age, discount_rate, cash = 0):
        self.name = name
        self.age = age
        self.discount_rate = discount_rate
        self.cash = cash



product = Product('mango', 20000)
customer = Customer('도강현','29', 40, 25000)
market = Market(product, 40)

selling_price = market.selling_product(customer)
print(selling_price)
remaining_cash = market.remaining_cash(customer)
print(remaining_cash)