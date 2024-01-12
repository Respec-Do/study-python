# f(x) = 2x + 1

# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)

# 두 정수의 곱셈 함수
# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# 1~10까지 print()로 출력하는 함수
# 이름을 n번 print()로 출력하는 함수
# 1~n까지의 합을 구해주는 함수
# 1~100까지 중 n의 배수를 print()로 출력하는 함수
# 세 정수의 뺄셈 함수
# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수

'''

# 두 정수의 곱셈 함수
# def mul(number1, number2):
#     return number1 * number2
#
# result = mul(10, 20)
# print(result)

# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def div(number1, number2):
#     return number1%number2, number1//number2
#
# result1, result2 = div(10,4)
# print(result1, result2)

# 1~10까지 print()로 출력하는 함수
# def printer():
#     for number in range(1,11):
#         print(number)
#
#     return
# printer()

# 이름을 n번 print()로 출력하는 함수
# def name_call(count):
#     for n in range(count):
#         print('도강현')
#     return
#
# name_call(10)

# 1~n까지의 합을 구해주는 함수
# def adder(number):
#     total = 0
#     for i in range(1,number+1):
#         total += i
#
#     return total
# message = '정수 입력: '
# result = adder(int(input(message)))
# print(result)


# 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def call_multiple(number):
#     for i in range(1,101):
#         if i % number == 0:
#             print(i, end= ' ')
#
#     return
# message = '정수 입력: '
# call_multiple(int(input(message)))

# 세 정수의 뺄셈 함수
# def three_subtractor(num1, num2, num3):
#     total = num1 - num2 - num3
#     return total
#
# message = '세 정수 입력: '
# num1, num2, num3 = (map(int,(input(message).split(','))))
# # print(type(num1), num2, num3)
# result = three_subtractor(num1, num2, num3)
# print(result)

# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수

'''

# def index_counter(sentence, alphabet):
#     count_list = []
#     for i in range(1, len(sentence)+1):
#         if alphabet == sentence[i-1]:
#             count_list.append(i)
#
#     if count_list == []:
#         return None
#     else:
#         return count_list
#
#
# sentence_message ='문자열을 입력하세요: '
# alphabet_message = '문자를 입력하세요: '
# sentence, alphabet = map(str, input(sentence_message + '\n' + alphabet_message).split(', '))
# # print(sentence, alphabet)
# result = index_counter(sentence, alphabet)
# print(f'alphabet 은 {result}번째에 있습니다')
# # a, b = map(str, input(sentence_message + '\n' + alphabet_message + '\n').split(', '))
# # print(a, b)