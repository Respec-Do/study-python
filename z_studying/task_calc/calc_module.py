from log_module import *

class Calculator:
    def __init__(self, number: int):
        #사용자가 원하는 연산기호를 oper에 담기위해 준비
        self.oper = None
        self.number = number

    def calc(self, other: int, oper: str, error_code: str=""):
        '''

        :param other: 연산할 두 번째 정수
        :param oper: 연산할 연산 기호
        :param error_code: 오류 발생시 오류 코드
        :return: 결과값
        '''

        # 전달받은 연산기호에 알맞은 인덱스 번호 설정
        oper_number = {'+':0, '-': 1, '*': 2, '/': 3}
        self.oper = oper
        # print(self.oper)
        #실행가능한 함수들을 list에 저장
        operations = [self.__add__, self.__sub__, self.__mul__, self.__floordiv__, self.write_error]
        # 만약 error_code가 있을 경우 write_error함수를 동작시키고
        # error_code가 없을 경우 알맞은 연산 메소드를 실행시킨다.
        return operations[oper_number[oper] if not error_code else 4](other, error_code=error_code)

    # self, other는 *args로 전달되고
    # error_code는 **kwargs로 전달된다.
    @log_time
    def __add__(self, other, **kwargs):

        return self.number + other

    @log_time
    def __sub__(self, other, **kwargs):

        return self.number - other

    @log_time
    def __mul__(self, other, **kwargs):
        return self.number * other

    @log_time
    def __floordiv__(self, other, **kwargs):
        return self.number // other, self.number % other

    #error_code가 있을 때
    # log에 error를 기록할 수 있도록 도와주는 도구로 사용
    # 즉 log_time()을 실행하기 위해 제작된 함수
    @log_time
    def write_error(self, other, **kwargs):
        pass