# number = 15
#
# if number %3 == 0:
#     print(f'{number}는 3의 배수입니다')
# if number %5 ==  0:
#     print(f'{number}는 5의 배수입니다')
#
#
# # number가 양수인지, 음수인지, 0인지 검사
# if number > 0:
#     print('양수입니다')
# elif number < 0:
#     print('음수입니다')
# else:
#     print('0입니다')
#
# positive_condition = number>0
# negative_condition = number<0
# zero_condition = number==0
#
# 나이를 입력받은 후 미성년자인지 검사
# age = int(input('나이를 입력하세요: '))
# condition = 0 < age < 20
# error_condition = age <= 0
#
# if condition:
#     print('미성년자입니다.')
# elif error_condition:
#     print('잘못 입력하셨습니다.')
# else:
#     print('성인입니다.')

# 두 정수를 입력 받은후 대소비교 진행


message = '두 정수를 입력: '
example_message = 'ex)10, 5'
num1, num2 = map(int,input(message + '\n' + example_message + '\n').split(','))

# 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 정수 : 0
# 실수 : 0.0
# 문자열 : '' 또는 ""
# 불린 : False

result_message = ''


if num1 > num2:
    result_message = f'{num1}이 더 큰 수입니다.'
elif num2 > num1:
    result_message = f'{num2}이 더 큰 수입니다.'
else:
    result_message = '두 정수는 같은 수입니다.'

print(result_message)












