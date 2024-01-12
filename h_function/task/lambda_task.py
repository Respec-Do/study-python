# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
# data = ['aPPle', 'BananA', 'meLON']
# print(list(map(lambda x : x.lower(), data)))



# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# # 출력 예: 3519
# data = '삼오일구'
# trans_data = (list(map(lambda x : '1' if x == '일' else '3' if x == '삼' else '5' if x == '오' else '9', data)))
# print(''.join(trans_data))


## 강사님 답안
hangul = "공일이삼사오육칠팔구"
data = "삼오일구"
print(int("".join(list(map(lambda s: str(hangul.index(s)),data)))))



# # 입력받은 정수를 한글로 변경
# # 입력 예: 3519
# # 출력 예: 삼오일구
# data = '3519'
# trans_data = (list(map(lambda x : '일' if x == '1' else '삼' if x == '3' else '오' if x == '5' else '구', data)))
# print(''.join(trans_data))


## 강사님 답안

hangul = "공일이삼사오육칠팔구"
data = 3519
print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))



# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
data = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
# 위 경로 중 회원 서비스가 아닌 경로만 추출
new_data = (list(filter(lambda x : x.split("/")[0] != 'user', data)))
# 1. 서비스명(user, post, order)으로 변경(map)
print(list(map(lambda x : x.split("/")[0], new_data)))

# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)

print(list(filter(lambda service: service != 'user', list(map(lambda url: url[:url.index("/")], data)))))























