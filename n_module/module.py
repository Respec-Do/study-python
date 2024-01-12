# import calc_add
# import calc.calc_sub as sub
# from calc.calc_sub import sub
from calc.calc import Calculator

import os
import sys



# if __name__ == '__main__':
#     # print(calc_add.add(2,3))
#     # print(sub.sub(10,5))
#     print('=' * 20)
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__))) #현재 작업하고 있는 파일의 위치
# print(sys.path.append(os.path.abspath(os.path.dirname(__file__))))