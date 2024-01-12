# check 함수를 선언하여 계좌번호와 핸드폰번호를 입력받는다.
def check(account_number, phone_number):
    for bank_list in Bank.banks:            # 아래 선언해둔 Bank.banks라는 리스트안에서 bank_list로 가져온 다음
        for bank_instance in bank_list:     # bank_list안에 bank_instance를 각각 검사하도록 한후
            if bank_instance.account_number == account_number or bank_instance.phone_number == phone_number:    # 만약 bank_instance에 있는 계좌번호나 핸드폰번호가 같다면 True를 리턴
                return True
    return False    # 아니라면 False를 리턴
# 비밀번호와 핸드폰번호를 확인하는 def 생성
def check_password(phone_number, password):
    for bank_list in Bank.banks:
        for bank_instance in bank_list:
            if bank_instance.password == password and bank_instance.phone_number == phone_number:
                return True
    return False
# 클래스 Bank 선언
class Bank:
    total_count = 3
    banks = [[] for _ in range(total_count)] #컴프리헨션을 이용, [[신한],[국민],[카카오]]
    # __init__ 으로 초기화 및 생성자
    def __init__(self, name, account_number, phone_number, password, balance=0):
        self.name = name
        self.account_number = account_number
        self.phone_number = phone_number
        self.password = password
        self.balance = balance
    # classmethod 인 open_account를 이용해서 선언시 bank_index를 받아 계좌를 개설하도록함.
    @classmethod
    def open_account(cls,bank_index, name, account_number, phone_number, password, balance=0):
        # bank_instance 로 선언후에 banks로 선언해둔 리스트에 append 하여 저장
        bank_instance = cls(name, account_number, phone_number, password, balance)
        cls.banks[bank_index].append(bank_instance)
        return bank_instance
    # check_account_number : 계좌번호 중복검사
    @staticmethod
    # 위에서 만들어둔 check라는 함수를 호출하여 각각 계좌번호와 핸드폰 번호를 중복검사하도록 함.
    def check_account_number(account_number):
        # 만일 계좌번호가 중복된다면 True를 리턴하고 아니면 False를 리턴함
        return check(account_number, "")
    # check_phone : 핸드폰 번호 중복 검사
    @staticmethod
    def check_phone(phone_number):
        # 핸드폰번호가 중복된다면 True를 리턴, 아니면 False를 리턴함.
        # 위의 check 함수가 계좌번호와 핸드폰번호를 둘다 검사하도록 하게했기에 각각 빈자리는 ""를 넣어줌
        return check("", phone_number)
    # 핸드폰, 비밀번호 확인
    @staticmethod
    def check_phone_password(phone_number, password):
        #핸드폰 번호, 비밀번호 입력 후
        #정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
        return check_password(phone_number, password) # phone_number와 password 둘다 일치하면 True 반환
    # 계좌재설정
    def reset_account(self, account_number):
        self.account_number = account_number
    # 입금
    def deposit(self, money):
        self.balance += money
    # 출금
    def withdraw(self, money):
        self.balance -= money
    # 잔액조회
    def get_balance(self):
        return self.balance
    # 전체출력
    def __str__(self):
        return f'name : {self.name}, account_number : {self.account_number}, phone_number: {self.phone_number}, password: {self.password}, balance: {self.balance}'
# 자식클래스로 신한, 국민, 카카오 은행 선언
class ShinHan(Bank):
    def __init__(self, name, account_number, phone_number, password, balance):
        super().__init__(name, account_number, phone_number, password, balance)
    # 입금시 50프로 수수료를 적용함. overriding 사용
    def deposit(self, money):
        # super().deposit(money)
        self.balance +=  round(0.5 * money)
class KookMin(Bank):
    def __init__(self, name, account_number, phone_number, password, balance):
        super().__init__(name, account_number, phone_number, password, balance)
    # 출금시 50프로 수수료를 적용함. overriding 사용.
    def withdraw(self, money):
        super().withdraw(money)
        self.balance -= round(0.5 * money)
class KaKao(Bank):
    def __init__(self, name, account_number, phone_number, password, balance):
        super().__init__(name, account_number, phone_number, password, balance)
    # 잔액조회시 50프로 차감, overriding 사용.
    def get_balance(self):
        self.balance = round(0.5 * self.balance)
        print(self.balance)
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"
    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 재설정\n" \
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
        # 은행 메뉴
        print(bank_menu)
        bank_index = int(input())       #bank_index로 은행선택
        # 은행 선택
        if bank_index == 1:
            bank_class = ShinHan
        elif bank_index == 2:
            bank_class = KookMin
        elif bank_index == 3:
            bank_class = KaKao
        elif bank_index == 4:
            break
        else:
            print(error_message)
            continue
        while True:
            # 서비스 메뉴
            print(menu)
            user_menu_num = int(input())
            # 1. 개설
            if user_menu_num == 1:
                owner = input(owner_message)
                account_number = input(account_number_message)
                phone_number = input(phone_message)
                password = input(password_message)
                money = int(input(money_message))
                # 개설하기전 check를 호출하여 중복되는지 확인
                if bank_class.check_account_number(account_number) == True:
                    print('중복된 계좌')
                elif bank_class.check_phone(phone_number) == True:
                    print('중복된 번호')
                else:
                    user = bank_class.open_account(bank_index - 1, owner, account_number, phone_number, password, money)
                # 개설
            # 2. 입금
            if user_menu_num == 2:
                deposit = int(input(deposit_message))
                user.deposit(deposit)
            # 3. 출금
            if user_menu_num == 3:
                withdraw = int(input(withdraw_message))
                user.withdraw(withdraw)
            # 4. 잔액
            if user_menu_num == 4:
                user.get_balance()
                print(user)
            # 5. 계좌번호 재설정
            if user_menu_num == 5:
                print('계좌번호를 재설정합니다.\n')
                # 휴대폰번호와 비밀번호를 입력
                checking_phone_num = input(phone_message)
                checking_password = input(password_message)
                if len(checking_password) > 4 :
                # 계좌번호 재설정 전 check_password를 호출하여 True 인지 확인
                    print(error_message)
                    continue

                else:
                    if user.check_phone_password(checking_phone_num, checking_password) == True:
                        # 새 계좌번호 입력
                        new_account_number = input(account_number_message)
                        user.reset_account(new_account_number)
                        print("계좌번호 변경완료")
                    else:
                        print(error_message)
                        continue

            # 6. 은행 선택 메뉴 돌아가기
            if user_menu_num == 6:
                break