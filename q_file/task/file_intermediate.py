# 파일의 단어의 빈도수 구하기
# import re
# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구분없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

content = ""
with open('alice.txt','r',encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.read().lower()
        for char in line:
            if char in "!@#$%^&*()_+-./:`;<=>?,@`-{}[]":
                line = line.replace(char, ' ')
                line = line.replace("'"," ")
                line = line.replace('"'," ")
        content += line


    content = content.replace('\n', ' ')
    content = content.split(' ')

    # 글자수 2개이상 단어 카운트 + 빈도수 100회 이상 카운트
    count = 0
    new_dict = {}
    for i in range(len(content)):
        if len(content[i]) >= 2:
            count = content.count(content[i])
            new_dict[content[i]] = count
    sorted_dict = sorted(new_dict.items(), key = lambda item: item[1], reverse=True)
    for key,value in sorted_dict:
        print(key, value)