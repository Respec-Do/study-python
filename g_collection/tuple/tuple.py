# mutable : 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)

# immutable : 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10  튜플은 수정이 불가능하다.
# test = list(data_tuple2)
# test[0] = 10
# print(test)

# 기존의 있는 주소에 접근해서 바꾸는 게 아니기에
# 수정하는 것이 아니라 새로운 튜플을 만드는 것임.
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
# () 없이도 튜플은 ',' 만으로 만들 수 있음.
datas = 1, 2
print(type(datas))

# 상수는 대문자로 선언하기로 약속
ERROR_CODE = 1,
print(type(ERROR_CODE[0]))
