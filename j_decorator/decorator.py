# import datetime
#
#
# def log_time(original_function):
#     print('log_time 들어옴')
#
#     def logging(*args):
#         print('logging 들어옴')
#         print(args)
#         print(datetime.datetime.now()) #현재 시간 출력하는 함수
#         print('logging 함수 종료')
#         return original_function(*args)
#
#     print('log_time 함수 종료')
#     return logging
#
# # 데코레이터로 뺏어왔다고 생각해야함. 그래서 return으로 원래 함수로 돌려줘야함.
# @log_time
# def add(*args):
#
#     total = 0
#     for i in args:
#         total += i
#
#     return total
#
#
# result = add(1, 2, 3)
# print(result)

# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)

        if count != 0:
            total = 0
            for i in args:
                total += i
            average = total / count

        else:
            total = kwargs.get('total')
            length = kwargs.get('count')
            average = total / length
        print(f"평균: {average}")
        return original_function(*args, **kwargs)

    return operate

@average
def set_datas(*args, **kwargs):
    count = len(args)
    if count != 0:
        total = 0
        for i in args:
            total += i
    else:
        total = kwargs.get('total')
    print(f'총 합: {total}')


set_datas(1, 2, 3, 4, 5)
set_datas(total = 100, count = 5)





