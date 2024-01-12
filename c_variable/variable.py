# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30

print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

# temp = a
# a = b
# b = temp
# print(a, b)

# 튜플을 이용한 바꾸기
a, b = b, a
print(a, b)

# 동적 바인딩
# a = 10
# print(type(a))
#
# a = 10.5
# print(type(a))
#
# a = 'A'
# print(type(a))
#
# a = "ABC"
# print(type(a))
#
# a = ['A', 'B', 'C']
# print(type(a))
#
# a = {'A': 1, 'B': 2, 'C': 3}
# print(type(a))
#
# a = True
# print(type(a))

# 변수명 주의 사항
age = 10
print(type(age))

ratio = 10.5
print(type(ratio))

score = 'A'
print(type(score))

chocolate = "ABC"
print(type(chocolate))

players = ['A', 'B', 'C']
print(type(players))

point = {'A': 1, 'B': 2, 'C': 3}
print(type(point))

condition = True
print(type(condition))

# 서식문자
# 반올림에서 5 미만의 숫자는 버림, 5 초과의 숫자는 올림한다
# 5의 경우에는 5의 앞자리가 홀수인 경우에는 올림, 짝수인 경우에는 버림을 하여 짝수로 만들어준다
# ex) 53.45 -> 53.4, 32.75 -> 32.8
# 이를 오사오입(round-to-nearest-even)이라고 한다
name = '김광협'
age = 25
height = 168.45

# print('이름: %s' % name)
# print('나이: %d' % age)
# print('키: %.1f' % height)
print('이름: %s\n나이: %d살\n키: %.1fcm' % (name, age, height))

print('=' * 20)

formatting = '이름: %s\n나이: %d살\n키: %.1fcm' % (name, age, height)
print(formatting)

print('=' * 20)

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4

# format 함수
name = 'KGH'
age = 27
height = 170.51

formatting1 = '이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height)
formatting2 = '이름: {1}\n나이: {0}\n키: {2:.1f}'.format(name, age, height)
formatting3 = '이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height)

print(formatting1)
print(formatting2)
print(formatting3)

# format string
name = '김광협'
age = 25
height = 168.36

# round(실수값, 반올림 자리수)
print(f'이름: {name}')
print(f'나이: {age}살')
print(f'키: 약 {round(height, 1)}cm')

# 실습
# 아래 메세지를 .format 함수를 이용해서 출력한다
# Hello 파이썬, Python is Fantastic!
# Hello 장고, Django is Fantastic!
# Hello 리액트, React is Fantastic!

# 공통 부분을 변수화한다면?

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4
number1 = 10
number2 = 8
total = number1 + number2
formatting = "%d + %d = %d" % (number1, number2, total)

print(formatting)

# 실습
# 아래 메세지를 format함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

# 자동으로 해당 순서에 값이 반영된다.
python_formatting = 'Hello {}, {} is fantastic !'.format(python_kor, python_eng)

# 값에 할당된 번호를 작성하면 해당 값이 반영된다.
django_formatting = 'Hello {0}, {1} is fantastic !'.format(django_kor, django_eng)

# 값에 이름을 붙이면 해당 이름에 있는 값이 반영된다.
react_formatting = 'Hello {kor}, {eng} is fantastic !'.format(kor=react_kor, eng=react_eng)

print(python_formatting, django_formatting, react_formatting, sep='\n')

# 실습
# 아래 메세지를 format함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

python_formatting = f'Hello {python_kor}, {python_eng} is fantastic !'
django_formatting = f'Hello {django_kor}, {django_eng} is fantastic !'
react_formatting = f'Hello {react_kor}, {react_eng} is fantastic !'

print(python_formatting, django_formatting, react_formatting, sep='\n')