for i in range(1, 11, 1):
    print(f'{i + 1}. 한동석')

for i in range(1, 11):
    print(f'{i + 1}. 도강현')

for i in range(10, 0, -1):
    print(f'{i}. 도강현')

for i in range(10):
    print(f'{i+1}')

# 1 ~ 10까지 중 3까지만 출력
for i in range(1, 11):
    print(i, end=' ')
    if i == 3:
        break
print()
# 1~ 10까지 중 4를 제외하고 출력
for i in range(1, 11):
    if i ==4:
        continue
    print(i, end=' ')