class NameCard:
    def print_info(self,name):
        print(name)
    # __enter__ 에 self를 리턴해줘야함
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('del')

with NameCard() as name_card: # 이런식으로 객체화 가능
    name_card.print_info('han')