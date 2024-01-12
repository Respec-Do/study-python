import datetime

# 현재 날짜
now = datetime.date.today()
print(now)

now = datetime.datetime.today()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
# 지정된 날짜

# 절대 외울 수 없음. 구글링을 해야함.

date = datetime.datetime(2024,1,1,12,0,0)
print(date)