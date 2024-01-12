'''
    파이썬은 다중 상속을 지원한다.
    하지만, 여러 부모를 상속 받았을 때, 동일한 이름의 빌드가 겹치면
    자식에서 사용할 때 혼란을 야기한다.
    이 때에는 mro()를 사용하여 접근 순서를 확인할 수 있으나,
    자식에서 재정의한 뒤 사용하는 것이 오히려 낫다.

'''

class A:
    pass

class B(A):
    def print_info(self):
        print('B')


class C(A):
    def print_info(self):
        print('C')

class D(B,C):
    pass

print(D.mro())
D().print_info()

