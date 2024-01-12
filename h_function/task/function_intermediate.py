# user_info = [
#     {'number' : 1, 'name' : 'john'},
#     {'number' : 2, 'name' : 'mike'},
#     {'number' : 3, 'name' : 'ted'},
#     {'number' : 4, 'name' : 'lindy'},
#     {'number' : 5, 'name' : 'adam'}

# ]
#
# # #추가(초보자용)
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #
# #     '''
# #     user_info.append({'number' : number, 'name' : name})
# #
#
# # 추가
# # 회원 번호는 자동 증가한다.
# def insert(name):
#     user_info.append({'number' : len(user_info) , 'name' : name})
#     for i in range(len(user_info)):
#         user_info[i]['number'] = i + 1
# #목록
# def info():
#     user_number = [user_info[i]['number'] for i in range(len(user_info))]
#     user_name = [user_info[i]['name'] for i in range(len(user_info))]
#     print(user_number,'\n',user_name)
#
# #조회(번호로 조회)
# def check(number):
#
#     user_name = user_info[number-1]['name']
#     print(user_name)
#
#
#
# # 수정(번호로 이름 수정)
# def correction(number, name):
#
#     user_info[number-1]['name'] = name
#
# # 삭제(번호로 삭제)
# def delete(number):
#
#     del user_info[number-1]
#
#     # user_info = [{'number' : i +1, **user} for i, user in enumerate(user_info)]
#
#
#     for i in range(len(user_info)):
#         user_info[i]['number'] = i+1
# check(5)
# correction(5,'steven')
# check(5)
# info()
# delete(4)
# info()
# print(user_info)
# insert('chris')
# info()
# print(user_info)


# # 강사님 답안
# # 추가
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number' : number, 'name' : name})
#     # 중복만 없으면 됨. 사이 숫자만 없으면 된다.
#
# # 목록
# def select_all():
#     return user_info
#
# # 조회
# def select(number):
#     # 컴프리헨션 시도
#     return user for user in user_info if user['number'] == number
#     # for user in user_info:
#         # if user['number'] == number:
#         #     return user
#     # return {}
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number' : 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     (select(kwargs.get('number'))['name']) = kwargs.get('name')
#
# # update(number = 1, name = 'han')
# # print(select_all())
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#
# delete(1)
# print(select_all())
# insert(name = 'hong')
# print(select_all())

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)

#기존 값이 5개여서 num=5에서 시작
num = 5
def insert(*, title, content,file, read_count = 0):
    #전역변수 이용위해 global
    global num
    #insert 사용할때마다 number 1개씩 추가하면서 append함.
    num += 1
    post_info.append({'number': num, 'title': title, 'content': content, 'file' : file, 'read_count' : 0})

# insert(title = '테스트 제목6',content = '테스트 내용 6')

# 목록(최신순으로 조회)

print(post_info)
def select_all():
    #최신순으로 정렬해서 불러오기위해 new_post라는 빈 리스트 생성
    new_post = []
    #역순으로 new_post에 기존 post_info를 append
    for i in range(len(post_info)): #0~4
        new_post.append(post_info[len(post_info) - i-1])
    return new_post

print(select_all())
# 조회(번호로 조회, 조회수 1 증가)
def select(number):
    for post in post_info:
        if post['number'] == number:
            #조회시 read_count의 개수를 늘리기 위해 +1 해줌
            post['read_count'] += 1
            return post
# select(1)
# print(select_all())

# 검색 (내부 코드용)
def search(number):
    for post in post_info:
        if post['number'] == number: return post
# 수정(번호로 정보 수정)

def update(**kwargs):
    '''

    :param kwargs: param kwargs: {'number' : 기존 번호, 'title': '새로운 테스트 제목',
                                  'content': '새로운 테스트 내용', 'file' : '새로운 파일 내용'}
    '''
    #수정시 조회수 증가를 방지하기 위해 select가 아닌 search로 사용
    search(kwargs.get('number'))['title'] = kwargs.get('title')
    search(kwargs.get('number'))['content'] = kwargs.get('content')
    search(kwargs.get('number'))['file'] = kwargs.get('file')

update(number = 5, title = 'python', content = 'hello python')
print(select_all())
# 삭제(번호로 삭제)

def delete(number):
    del post_info[post_info.index(search(number))]

delete(4)
print(select_all())
select(5)
print(select_all())




