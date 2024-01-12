# 문자열끼리만 연결(+)이 가능하다!
# name = input("이름: ")
# print(f'{name}님 환영합니다')


# data = 3
# print('안' + str(data))

# 제 이름은 ??? , 키는 ??? cm 입니다.
# name, height = input("이름 :"),  input("키 :")
#
# height = input("키 :")
#
# formatting = f'제 이름은 {name}, 키는 {height}입니다.'
# print(formatting)

# 두 정 수를 입력받은 후 곱셈 결과 출력
# num_a, num_b = input("두 정수 입력: ").split(',')
# num_a, num_b = int(num_a), int(num_b)
# print(num_a+ num_b)


# map은 바꾸려고 사용한다.
# number1, number2 = map(int, input("두 정수를 입력하세요: ").split(','))
# print(number1 * number2)

# a, b, c = 'A,B,C'.split(',')
# print(a,b,c)
#
# # map(각각 어떻게 바꿀 것인가, [])
#
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message +'\n' + example_message  + '\n').split(','))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(formatting, end='')

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# 핸드폰 번호를 - 과 함꼐 입력 받은 뒤 각 자리의 번호를 분리해서 출력
# 이름과 나이를 한번에 입력 받은뒤 " 000님의 나이는 000살' 형식으로 출력
# 3갤의 정수를 입력받은 뒤 덧셈결과 출력


# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# hour, minute = input('현재 시간을 입력하세요: ').split(':')
# format1 = f'{hour}시 {minute}분'
# print(format1, end='')

# 핸드폰 번호를 - 과 함꼐 입력 받은 뒤 각 자리의 번호를 분리해서 출력
# phone_number1, phone_number2, phone_number3 = input('Enter your phone number: ').split('-')
# format2 = f'{phone_number1} {phone_number2} {phone_number3}'
# print(format2)

# 이름과 나이를 한번에 입력 받은뒤 " 000님의 나이는 000살' 형식으로 출력
# message = '이름과 나이를 입력하세요: '
# name, age = input(message).split(',')
# format3 = f'{name}님의 나이는 {age}살'
# print(format3, end='')

# 3개의 정수를 입력받은 뒤 덧셈결과 출력
message = '3개의 정수를 입력: '
num1, num2, num3 = map(int, input(message).split(','))
total = num1 + num2 + num3
print(total)






