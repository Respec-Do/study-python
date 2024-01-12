# 중복이 없고, 순서가 없다.
world_set = {'korea', 'america','japan','china'}
print(type(world_set))
print(len(world_set))
# 순서가 없어서 [1] 처럼 사용하면 오류 발생, 내부의 값을 가져올 수 없음
# print(world_set[1])

# .add()
world_set.add('korea')
print(world_set)

# 출력이 된다?
# set의 구조를 봤을 때, 형변환을 한 후 가져와서 출력할 때 문자열 형태로 출력하는 것임.
# set은 가져오기 위한 자료구조가 아님.

# 그럼 언제 쓰나?
# 중복은 없어야한다 -> 등의 문장이 있을 때 사용
datas = [1, 1, 3, 2, 3, 4, 1, 4, 4]
print(list(set(datas)))