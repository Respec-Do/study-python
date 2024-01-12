#1. email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# message = 'email을 입력하세요 : '
# sample_message = '00000@0000.com'
#
# user_id, domain = input(message + '\n' + sample_message + '\n').split('@')
# format = f'사용자아이디 : {user_id}\n사용자 도메인: {domain}'
# print(format)

# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.

'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm

    round(값, 원하는 자리수) : 소수점이 맞춰진 결과값
'''

message = '야드와 인치를 입력하세요:'
sample_message = 'ex) 10,10'
yard, inch = map(int, input(message + '\n' + sample_message + '\n').split(','))
# print(yard, inch)

converted_yard = round(yard * 91.44, 2)
converted_inch = round(inch * 2.54, 2)

formatting = f'{yard}yard는 {converted_yard}cm\n{inch}inch는 {converted_inch}cm'
print(formatting)






















