# 중복 검사
def check(i, choice, **kwargs):
    # 계좌번호 중복 검사
    if i == 'account':
        print('계좌 중복 검사 함수 실행')
        for account in range(len(Bank.banks[choice-1])):
            # 매개변수로 받은 번호와 같은 계좌번호가 있다면
            if kwargs.get('user_account') == Bank.banks[choice-1][account].get('user_account'):
                print('중복 계좌')
                # fasle 리턴
                return False
        else:
            return kwargs
    # 핸드폰 번호 중복 검사
    elif i == 'phone':
        print('핸드폰 중복 검사 함수 실행')
        for phone in range(len(Bank.banks[choice-1])):
            # 매개변수로 받은 번호와 같은 전화번호가 있다면
            if kwargs.get('user_phone') == Bank.banks[choice-1][phone].get('user_phone'):
                print('중복 핸드폰')
                # fasle 리턴
                return False
        else:
            return kwargs

class Bank:
    # 전체 은행 수
    total_count = 3
    # 은행 2차원 배열로 생성
    # comprehension 이용
    banks = [
        [] for bank in range(total_count)
    ]
    user_balance = 0
    # def __init__(self, user_name, user_account, user_phone, user_password, user_balance=0):
    #     self.user_name = user_name
    #     self.user_account = user_account
    #     self.user_phone = user_phone
    #     self.user_password = user_password
    #     self.user_balance = user_balance

    def __init__(self, **kwargs):
        global user_balance
        self.user_name = kwargs.get('user_name')
        self.user_account = kwargs.get('user_account')
        self.user_phone =kwargs.get('user_phone')
        self.user_password = kwargs.get('user_password')
        self.user_balance = user_balance
    # 계좌 조회(중복없음)
    @staticmethod
    def check_account_number(choice, **kwargs):
        print('계좌 조회 함수 실행')
        result = check('account', choice, **kwargs)
        return result

    # 핸드폰 번호 조회(중복없음)
    @staticmethod
    def check_phone(choice, **kwargs):
        print('핸드폰 번호 조회 함수 실행')
        return check('phone', choice, **kwargs)

    # 계좌 신규 계설 시, 이용할 생성자
    # @classmethod
    # def open_account(cls, choice, **kwargs):
    #     print(kwargs.get('user_name'))
    #     user_balance = kwargs.pop('user_balance', 0)
    #     if (len(Bank.banks[choice - 1]) == 0):
    #         user = {'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
    #          'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'], "user_balance": kwargs['user_balance']}
    #         Bank.banks[choice - 1].append(user)
    #         # print(type(user))
    #         return cls(choice, user_name, user_account, user_phone, user_password, user_balance)
    #     else:
    #         if((cls.check_account_number(choice, **kwargs) == True) and (cls.check_phone(choice, **kwargs) == True)):
    #             user = {'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
    #                     'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'],
    #                     'user_balance': kwargs['user_balance']}
    #             Bank.banks[choice-1].append(user)
    #             return cls(choice, user_name, user_account, user_phone, user_password, user_balance)
    #         else:
    #             return False
    # @classmethod
    #
    # def open_account(cls, choice, **kwargs):
    #     user_balance = kwargs.pop('user_balance', 0)
    #
    #     if len(Bank.banks[choice - 1]) == 0:
    #         user = {'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
    #                 'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'],
    #                 'user_balance': user_balance}
    #         Bank.banks[choice - 1].append(user)
    #         return cls(choice, **user)  # Pass extracted user details as individual arguments
    #     else:
    #         if cls.check_account_number(choice, **kwargs) and cls.check_phone(choice, **kwargs):
    #             user = {'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
    #                     'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'],
    #                     'user_balance': user_balance}
    #             Bank.banks[choice - 1].append(user)
    #             return cls(choice, **user)  # Pass extracted user details as individual arguments
    #         else:
    #             return False
    # @classmethod
    # def open_account(cls, choice, **kwargs):
    #     user_balance = kwargs.pop('user_balance', 0)
    #
    #     if cls.check_account_number(choice, **kwargs) and cls.check_phone(choice, **kwargs):
    #         user = {'user_name': kwargs['user_name'], 'user_phone': kwargs['user_phone'],
    #                 'user_password': kwargs['user_password'], 'user_account': kwargs['user_account'],
    #                 'user_balance': user_balance}
    #         Bank.banks[choice - 1].append(user)
    #         return cls(choice, **user)  # Pass extracted user details as individual arguments
    #     else:
    #         return False

    @classmethod
    def open_account(cls, choice, **kwargs):
        user_balance = kwargs.pop('user_balance', 0)

        if cls.check_account_number(choice, **kwargs) and cls.check_phone(choice, **kwargs):
            user = {
                'user_name': kwargs['user_name'],
                'user_phone': kwargs['user_phone'],
                'user_password': kwargs['user_password'],
                'user_account': kwargs['user_account'],
                'user_balance': user_balance
            }
            Bank.banks[choice - 1].append(user)
            return cls(choice, **user)  # Pass extracted user details as individual arguments
        else:
            return False

    # 입금
    def deposit(self, choice, money, user):
        for account in range(len(Bank.banks[choice - 1])):
            print(user.user_account)
            if user.user_account == Bank.banks[choice - 1][account]['user_account']:
                if user.user_password == Bank.banks[choice - 1][account]['user_password']:
                    Bank.banks[choice - 1][account]['user_balance'] += money
                    return '입금 성공'
                else:
                    return '비밀번호 불일치'
            else:
                return '해당 계좌 없음'
    # 출금
    def withdraw(self):
        pass

    # 통장 잔고
    def balance(self):
        pass

    # 비밀 번호
    def password(self):
        pass

    def __str__(self):
        return f'name: {self.user_name}'


class ShinHan(Bank):
    pass


class KookMin(Bank):
    pass


class KaKao(Bank):
    pass


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

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
        bank_choice = int(input(bank_menu))

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))

            # 개설
            if menu_choice == 1:
                user_name = input(owner_message)
                user_account = input(account_number_message)
                user_phone = input(phone_message)
                user_password = input(password_message)
                user1 = Bank.open_account(bank_choice, user_name=user_name, user_account=user_account, user_phone=user_phone, user_password=user_password)
                # print(type(user1))
                if user1:
                    print(f'{user_name}님 계좌 개설 성공')
                else:
                    print(f'{user_name}님 계좌 개설 실패')

            # 입금
            elif menu_choice == 2:
                user_name = input(owner_message)
                user_account = input(account_number_message)
                user_phone = input(phone_message)
                user_password = input(password_message)
                user_deposit_money = input(deposit_message)
                user = Bank(user_name, user_account, user_phone, user_password)
                result = user.deposit(bank_choice, user_deposit_money, user)
                print(result)