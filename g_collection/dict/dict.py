# student = {
#     "name" : "한동석",
#     "email" : "asdf@gmail.com"
# }
#
# print(student['name'])
# print(student.get('name'))
#
# # get()을 사용하면 key를 찾지 못했을 떄 원하는 default 값으로 설정이 가능하며,
# # default 값이 없을 때에는 None을 가져온다.
# # print(student['phone']) 오류
# print(student.get('phone', '01012341234'))
#
# # 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
# student['name'] = '홍길동'
# print(student)
# # 'phone' key 값이 없기 때문에, 아래의 코드는 '추가'이다.
# student['phone'] = '01012341234'
# print(student)
#
# if 'email' in student: #수정
#     student['email'] = 'hgd1234@gmail.com'
# else: # 추가
#     student['email'] = 'hgd1234@gmail.com'
#
# print(student)


# my_dict = {
#     1 : "한동석",
#     "two" : "20살",
#     False : [10, 20 ,30],
#     "row" : [
#         {"name" : "ted", "age": 40},
#         {"name": "jack", "age": 30},
#         {"name": "john", "age": 20},
#
#     ]
#
# }
#
# # row에 있는 회원 3명의 정보를 모두 출력
#
# for i in range(len(my_dict['row'])):
#
#     print(my_dict['row'][i]['name'], my_dict['row'][i]['age'])
#
# # 아래가 더 깔끔.
# if 'row' in my_dict:
#     for data in my_dict['row']:
#         print(f'{data["name"]}: {data["age"]}')
#


# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수' 를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 이용
#
# my_dict = {
#     '홀수' : [i *2 +1 for i in range(5)],
#     '짝수' : [(i+1)*2 for i in range(5)]
# }
#
# message = '홀수, 짝수 중 입력: '
# # 제어문 사용 하지 않고?
# # odd_even = input(message)
# # if odd_even == '홀수':
# #     for data in my_dict['홀수']:
# #         print(f'{data}')
# # else:
# #     for data in my_dict['짝수']:
# #         print(f'{data}')
#
# # print(my_dict[input(message)])
# # print(my_dict[input(message)])
# print(", ".join(map(str, my_dict[input(message)])))
#

student = {
    'name': '한동석',
    'email' : 'tedhan1204@gmail.com'
}

# key 분리
print(list(student.keys()))

for key, value in student.items():
    print(key, value)
# value 분리
print(list(student.values()))
# item 분리
print(list(student.items()))








