# 인간(부모)
# 이름, 나이
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 걷기(walk)
# '두 발로 걷습니다' 출력
    @staticmethod
    def walk():
        print("두 발로 걷습니다")


# 원숭이(자식)
# 이름, 나이, 동물원 이름
class Monkey(Human):
    def __init__(self,name, age ,zoo_name):
        super().__init__(name, age)
        self.zoo_name = zoo_name

# 걷기(walk)
    def walk(self):
        super().walk()
        print("네 발로 걷습니다")

# '두 발로 걷습니다', '네 발로 걷습니다' 출력

human = Human('han', 20)
human.walk()
monkey = Monkey('sue', 5, '롯데')
monkey.walk()