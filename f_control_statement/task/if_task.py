# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

#1. 빨간색
#2. 검은색
#3. 노란색
#4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.
# message = '메뉴번호를 입력하세요: '
# menu = '1. 빨간색\n2. 검은색\n3. 노란색\n4. 흰색'
# user_num = int(input(menu + '\n' + message + '\n'))
#
# result_message = ''
# if user_num == 1:
#     result_message = 'red'
# elif user_num == 2:
#     result_message = 'black'
# elif user_num == 3:
#     result_message = 'yellow'
# else:
#     result_message = 'white'
#
#
# print(result_message)

title = '색상을 골라주세요!\n'
menu =  '1. 빨간색\n' \
        '2. 검은색\n' \
        '3. 노란색\n' \
        '4. 흰색\n'

choice = int(input(title + menu))
choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4
color1, color2, color3, color4 = 'red', 'black','yellow','white'
result = None

if choice1:
    result = color1
elif choice2:
    result = color2
elif choice3:
    result = color3
elif choice4:
    result = color4

print(result)