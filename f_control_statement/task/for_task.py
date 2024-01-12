# 1 ~ 15까지 출력
# 30 ~ 1 까지 출력
# 1~ 100가지 중 홀수만 출력
# 1~ 10까지 합 출력
# 1~ n까지 합 출력
# 3 4 5 6 3 4 5 6 3 4 5 6 출력

# for i in range(1,16):
#     print(i, end=' ')
# print()
#
# for i in range(30,0,-1):
#     print(i, end=' ')
# print()
#
# for i in range(1,101,2):
#     print(i, end=' ')
# print()
#
# total = 0
# for i in range(11):
#     total += i
# print(total)
# print()
#
# total = 0
# num = int(input("Enter a number: "))
# for i in range(num):
#     total += i
# print(total)
# print()
#
# for i in range(3):
#     for j in range(3,7):
#         print(j, end= ' ')

#1, 235, 500을 1235500으로 출력
num1, num2, num3 = 1, 235, 500
total = str(num1) +str(num2) +str(num3)
print(total)

for i in (1, 235, 500):
    print(i, end='')
print()
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i
result = int(result)
print(result)


