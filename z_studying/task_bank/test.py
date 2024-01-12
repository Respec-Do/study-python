class ShinHan:
    pass
class KookMin:
    pass
class KaKao:
    pass

bank_choice = int(input())
user = [ShinHan, KookMin, KaKao][bank_choice -1]
print(user)