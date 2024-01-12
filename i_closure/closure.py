# def set_key(key):
#     formatting = ''
#
#     #클로저
#     def set_value(value):
#         #global 이 아니라 formatting을 수정(write)/(not read)하기 위해서는 nonlocal로 선언해야함
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formatting = set_name("한동석")
# # print(formatting)
#
# # '나이: 00살'
# set_age = set_key('나이')
# formatting1 = set_age('30살')
# # print(formatting1)
#
# print(f'{formatting}\n{formatting1}')
#

#실습
# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

# def set_topic(**kwargs):
#     if 'name' in kwargs:
#         def set_format(sep=' ,'):
#             formatting = f'name{sep}{kwargs.get("name")}'
#             return formatting
#
#         result =set_format
#
#
#     else:
#         def set_format(sep=', '):
#             formatting = f'{kwargs.get("topic")}{sep}{kwargs.get("point")}'
#             return formatting
#         result = set_format
#
#
#     return set_format
#
# print(set_topic(name = '도강현')(': '))
# print(set_topic(topic = '지구 온난화', point = '오존층 파괴를 막기위해 인간이 할일')("\n"))

# 상품 정보(상품명, 가격)를 여러 개 전달 받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

######## 공부해볼것 #############
# def set_product(*args):
#     products = []
#
#     def add_product(product_name, price):
#
#         product = {"name": product_name, "price": price}
#         products.append(product)
#         return f'{product_name} added'
#
#     def update_product(product_number, new_name, new_price):
#         if 0 <= product_number <= len(products):
#             products[product_number - 1]["name"] = new_name
#             products[product_number - 1]["price"] = new_price
#             return f'product updated'
#         else:
#             return f'invalid product number'
#
#     def select_all():
#         if not products:
#             return 'no products'
#         else:
#             return products
#
#     results = []
#     for arg in args:
#         if arg["action"] == "add":
#             results.append(add_product(arg["name"], arg["price"]))
#         elif arg["action"] == "update":
#             results.append(update_product(arg["product_number"], arg["new_name"], arg["new_price"]))
#         elif arg["action"] == "select_all":
#             results.append(select_all())
#
#     return results
#
#
# result = set_product(
#     {"action": "add", "name": "냉장고", "price": 1200},
#     {"action": "add", "name": "자동차", "price": 1500},
#     {"action": "update", "product_number": 2, "new_name": "비행기", "new_price": 1800},
#     {"action": "select_all"}
# )
#
# print(result)

#############강사님 답안 #######################
# 상품 정보(상품명, 가격)를 여러 개 전달 받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

def set_product(*args):
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number}, # 튜플형태로 전달되어야하기에 콤마를 붙여줬음.

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break


    def select_all():
        return args

    return {'insert' : insert, 'update' : update, 'select_all' : select_all} #closuer 중에 언제든 골라쓸수있게 함, return의 새로운 표현방식

products = [
    {'name': '마우스', 'price' : 5000},
    {'name': '키보드', 'price' : 25000}
]
product_service = set_product(*products)
print(products)
product_service.get('insert')(name = '모니터', price = 80000)
print(product_service.get('select_all')())
product_service.get('update')(name = '키보드', price = 20000, number = 2)

print(product_service.get('select_all')())

