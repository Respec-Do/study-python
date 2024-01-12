# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의


class Taxi:
    #정적변수 설정
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    # 거리에 따른 요금 계산 메소드
    def calculate_money(self):
        cost = Taxi.default_fare #클래스 정적변수 호출
        if self.distance > Taxi.default_distance:
            cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km

        return cost


    # 거리에 따른 잔돈 계산 메소드
    def get_change(self):
        return self.money - self.calculate_money()


taxi = Taxi(20000, 1)
print(taxi.calculate_money(), taxi.get_change())



