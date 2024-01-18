# 숙제

# 회원가입
# 회사 추가
# 회의실 추가
# 회의실마다 이용가능 시간 추가
# 예약 추가
# 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).

from crud_module import *
from connection_module import *
import hashlib


#
# if __name__ == '__main__':
#     # 회원가입
#     message = "이메일: "
#     client_email = input(message)
#     ## 아이디 중복검사
#     find_by_id_query = "select * from tbl_client where email = %s"
#     find_by_id_params = client_email,
#     result = find_by_id(find_by_id_query, find_by_id_params)
#
#     if not result:
#         message = "비밀번호: "
#         client_password = input(message)
#         encryption = hashlib.sha256()
#         encryption.update(client_password.encode('utf-8'))
#         client_password = encryption.hexdigest()
#
#         message = "이름: "
#         client_name = input(message)
#
#         save_query = "insert into tbl_client(email, password, name) values(%s, %s, %s)"
#         save_params = (client_email, client_password, client_name)
#         save(save_query, save_params)
#         print(f"{client_name}님 환영합니다~!")
#
#     else:
#         print("이미 사용중인 이메일입니다.")
#
    # 회사 추가
    # save_many_query = "insert into tbl_office(name, location) \
    #                    values(%s, %s)"
    # save_many_params = (
    #     ('네이버','서울시 역삼동'),
    #     ('코리아IT','서울시 서초동'),
    #     ('KAKAO','경기도 의정부시')
    # )
    # save_many(save_many_query, save_many_params)

# # 회의실 추가
# find_by_id_query = "select id from tbl_office where id = %s"
# # find_by_id_params = 1,
# # find_by_id_params = 2,
# find_by_id_params = 3,
# office = find_by_id(find_by_id_query, find_by_id_params)
# # print(office)
# office_id = office.get("id")
# save_many_query = "insert into tbl_conference_room(office_id) \
#                    values(%s)"
# save_many_params = (
#     (office_id),
#     (office_id),
#     (office_id),
# )
# save_many(save_many_query, save_many_params)
