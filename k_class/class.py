class A:

    # @classmethod
    # def __new__(cls, *args, **kwargs): # 메모리에 필드를 할당하는 것은 __new__, 진짜 생성자는 __new__
    #     obj = super().__new__(cls)
    #     return obj #필드의 주소값이 됨

    def __init__(self, data1, data2, name=''):
        print(self)
        self.name = name      # __new__ 와 __init__은 한쌍이다. 둘다 선언하지 않아도 자동으로 생성이 됨.
        self.data1 = data1    # __new__ 로부터 __init__에 할당해준다라고 이해하면 됨.
        self.data2 = data2    # __init__ 의 self에 주소가 자동으로 담김


    # def print_name(self, name):
    #
    #     print(name)
    def print_name(self):
        print(self.name)

a = A(10, 20) # A() 로 선언한것이 객체화한것. 그것을 a에 담아줌.
print(a)
# a.data1 = 10 # 10이라는 값을 a라는 필드에 넣겠다.
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

b = A(100,200) # b라는 또 다른 객체
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()