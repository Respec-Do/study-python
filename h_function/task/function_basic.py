# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.
# 쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수
#
# coupon=40
# count=5
#
# 아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
# 40%쿠폰 5개
#
# 아래와 같은 상황은 없다.
# 10%쿠폰 1개, 20%쿠폰 2개

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]


# def order_info(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += i
#
#     print(f'{kwargs["name"]}님의 총 주문 가격 : {total}원')
#
# order_info(3000,2000,1000, name = '한동석')
#
# pay = map(int, input().split(','))
#
# coupon = int(input('coupon: '))
# count = int(input('count= '))

# print(*pay, coupon, count)

# def coupon_discount(*pay, coupon, count):
#     discount_rate = coupon/100
#     cash_list = []
#     for i in range(count):
#         cash_list.append(pay[i]*discount_rate)
#     print (cash_list)
#
# coupon_discount(*pay, coupon, count)

# pay = map(int, input().split(','))
# coupon = int(input('coupon: '))
# count = int(input('count= '))
#
#
# def coupon_discount(coupon, count, *pay):
#     discount_rate = 1 - coupon / 100
#     cash_list = []
#
#     cash_list = [pay[i] for i in range(len(pay))] + [0] * count
#     return [round(cash_list[i] * discount_rate) for i in range(count) if cash_list[i] != 0]
#
#
# result = coupon_discount(coupon, count, *pay)
# print(result)

#강사님 답안

def use_coupon(*pay, **kwargs):

    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''

    if 'coupon' in kwargs:
        return[
            int((100 - kwargs.get('coupon')) * 0.01* pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))

        ]
    pass

help(use_coupon)
result = use_coupon(1000,2000,3000, coupon = 50, count = 2)
if result:
    print(result)
else:
    print('쿠폰이 없습니다')




































