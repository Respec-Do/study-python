# animals = ['dog','cat','bird','fish']
# print(animals)
# print(type(animals))
#
# # 인덱스로 접근
# print(animals[1])
# print(animals[2])
# # animals.append('')
#
# # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동)
# print(animals[-1])
#
# #len()
# print(len(animals))
#
# # append()
# animals.append('hamster')
# print(len(animals))
# print(animals)
#
# animals.append('cat')
# print(animals)
#
# # insert()
# animals.insert(1, 'dog')
# print(animals)
#
# #remove()
# animals.remove('fish')
# print(animals)
#
# # del()
# # del(animals[1])
# del animals[1]
# print(animals)
#
# #clear()
# # animals.clear()
# # print(animals)
#
# # index()
# print(animals.index('bird'))
#
# # 수정
# animals[animals.index('bird')] = 'lion'
# print(animals)
#
#
# # 그 외 알면 좋은것들
# animals = ['dog','cat','bird','fish']
# print(animals *2)
#
# print("dog" in animals)
# print("tiger" in animals)
#
# for i in animals:
#     print(i, end=' ')
#
#
#
#
# 실습
# 1 ~ 90 까지 list에 담고 출력
# 1 ~ 100까지 중 짝수만 list에 담고 출력
# 1 ~ 10 까지 list에 담은 후 짝수만 출력
# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
#
# 1 ~ 90 까지 list에 담고 출력
# li1 = [0] * 90
# for i in range(len(li1)):
#     li1[i] = i +1
# print(li1)
#
# # 1 ~ 100까지 중 짝수만 list에 담고 출력
# li2 = []
# for i in range(1,101):
#     if i %2 == 0:
#         li2.append(i)
# print(li2)
#
# # 1 ~ 10 까지 list에 담은 후 짝수만 출력
# li3 = []
# for i in range(1,11):
#     li3.append(i)
#
# for i in li3:
#     if i%2==0:
#         print(i, end= ' ')
# print()
# # 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# li4 = ['짱구','철수','맹구','유리']
#
# li4[li4.index('철수')] = '훈이'
# del li4[3]
# print(li4)

# # '189,000 원' 을 189000으로 변경 제너레이터 사용
# s  = "189,000 원"

# list 안에 list
number_list  = [[1,3,5],[2,4,6]]
# print(number_list[0][0])

print(len(number_list))

length = len(number_list) * len(number_list[0])

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])
