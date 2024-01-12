# 이름 10번 출력
count = 0
while count != 10:
    print('도강현')
    count+=1

# 1. 사용자에게 정수를 입력받는다
# 2. 입력받은 정수의 각 자리수를 샌다.
# 3. 자리수를 출력한다.
# 힌트 몫과 나머지
message = '정수를 입력하세요: '
number = int(input(message))
count = 1
num_length = 0

while number // count >0:
    if number // count != 0:
        count *= 10
        num_length += 1

formatting = f'자리수는 {num_length}입니다'
print(formatting)
