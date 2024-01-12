# total_count = 3
# banks = [[] for i in range(total_count)]
# print(banks)

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    @classmethod #클래스로 직접 접근해서 쓴다.
    def translate_to_eng(cls, color):
        if color == '빨간색':
            color = 'red'

        return cls(color)

    #객체화를 직접하는 것이 아닌 메소드로 호출


car = Car('Benz', '빨간색', 15000)
car.translate_to_eng('Benz','빨간색',15000)
print(car.color)