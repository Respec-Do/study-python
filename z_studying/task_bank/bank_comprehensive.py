#은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막
#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.

# 입금, 출금, 잔액조회, 계좌번호찾기의 서비스는 핸드폰 번호와 비밀번호를 이용하여 로그인하여 이용하도록 구성.
# 로그인시 비밀번호는 4자리여야함.
# 계좌개설, 입금, 출금, 잔액조회, 계좌번호 찾기 서비스를 이용하면 이용한 시간을 로깅하여 그 시간을 출력하도록 구성.

# module로 분리
# 메인 모듈에서 실행하도록 구성.

def check(*, key: str, value: str) -> dict:
    for bank in Bank.banks:
        for user in bank:
            if user[key] == value:
                return user
    return None

class Bank:
    #은행의 개수
    total_count = 3
    # 은행의 개수만큼 저장공간 확보
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone_number: str, password: str, money: int):
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone_number = phone_number
        self.password = password
        self.money = money

    # bank_choice 는 은행선택값.
    # 어떤 은행에서 개설하는지를 bank_choice로 받아옴.
    # 개설에 필요한 정보는 **kwargs로 받아옴
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        # 어떤 은행에서 개설하는 지 알 수 없기에
        # 전달받은 bank_choice를 통해 은행을 선택하게한다.
        user = [ShinHan, KookMin, KaKao][bank_choice](**kwargs)
        # dict의 형태로 담기 위해 __dict__사용
        cls.banks[bank_choice-1].append(user.__dict__)
        return user

    #self에 접근하는 메소드가 아님.
    # staticmethod
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        return check(key = 'account_number', value = account_number)

    @staticmethod
    def check_phone(phone_number: str) -> dict:
        return check(key = 'phone_number', value = phone_number)


    def deposit(self, money: int):
        self.money += money


    def withdraw(self, money: int):
        self.money -= money


    def balance(self):
        return self.money

    def __str__(self):
        return (f'owner : {self.owner},account_number: {self.account_number},phone_number: {self.phone_number},'
                f'password: {self.password},money: {self.money}')



class ShinHan(Bank):
    # Overriding
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)

class KookMin(Bank):
    # Overriding
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    # Overriding
    def balance(self):
        self.money //= 2
        return super().balance()


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌 번호 재설정\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 메뉴 출력
        bank_choice = int(input(bank_menu))

        # 나가기
        if bank_choice == 4:
            break

        # 메뉴의 번호 이외의 번호 입력하면 밑으로 내려가지 못하게 막음
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))

            # 은행메뉴로 돌아기기
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone_number = input(phone_message)
                    if Bank.check_phone(phone_number) is None:
                        break

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break

                money = int(input(money_message))

                #계좌가 개설. 위에 while True 문을 통해 계좌, 및 핸드폰 번호 중복검사를 실행함.
                user = Bank.open_account(bank_choice, owner = owner, account_number = account_number, phone_number = phone_number,
                                         password = password, money = money)
                print(user)


            #입금
            # 개설한 은행에서만 입금 가능하도록 함.
            elif menu_choice == 2:
                account_number = input(account_number_message)
                #계좌번호 검색 결과 user에 담김
                user = Bank.check_account_number(account_number)
                if user is not None:
                    # 비밀번호 검사
                    if user['password'] == input(password_message):
                        # 입금 서비스
                        deposit_money = int(input(deposit_message))
                        user['object'].deposit(deposit_money)
                    else:
                        print('Wrong Password')
                else:
                    print(error_message)
        pass