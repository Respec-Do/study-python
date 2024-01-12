# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = ""
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

number_message = "메뉴 번호를 입력해주세요: "

#메뉴 출력 및 사용자에게 번호 입력
while True:
    print(menu)
    user_number = int(input(number_message))

    #추가
    if user_number == 1:
        print(append_message)
        # 추가화면이 나오고 사용자에게서 추가할 이름과 금액을 받음
        new_name = input(search_name_message)
        new_price = int(input(search_price_message))
        # 추가할 이름이 기존 리스트에 있다면 에러메시지 출력
        if new_name in name_list:
            print(append_error_message)
        # 추가할 이름이 기존 리스트에 없기에 리스트에 append
        else:
            name_list.append(new_name)
            price_list.append(new_price)

    #수정
    elif user_number == 2:
        print(search_name_message_for_update)
        # 수정할 이름을 입력받고 그 인덱스를 바로 찾음
        old_name  = input(search_name_message)
        old_index = name_list.index(old_name)
        # 만약 수정할 이름이 기존리스트에 없다면 에러메시지  출력
        if old_name not in name_list:
            print(update_error_message + '\n'  + error_message + '\n')
        # 수정해서 바꿀 예정인 이름과 금액을 입력받고 위에서 찾읕 인덱스로 그 이름리스트와 가격리스트에 각각 업데이트
        else:
            print(update_message)
            update_name = input(search_name_message)
            update_price = int(input(search_price_message))
            name_list[old_index] = update_name
            price_list[old_index] = update_price
    #삭제
    elif user_number == 3:
        print(delete_message)
        # 삭제할 이름을 입력받고 그 인덱스번호를 찾음
        old_name = input(search_name_message)
        old_index = name_list.index(old_name)
        # 리스트 안에 없다면 에러메시지 출력
        if old_name not  in name_list:
            print(delete_error_message + '\n' + error_message + '\n')
        # 인덱스번호로 기존리스트에서 삭제
        else:
            del name_list[old_index]
            del price_list[old_index]

    #검색
    elif user_number == 4:
        search_select_number = int(input(search_menu))
        #이름 검색
        if search_select_number == 1:
            # 검색할 이름을 입력받음
            searched_name = input(search_name_message)
            # 리스트에 없다면 에러메시지 출력
            if searched_name not in name_list:
                print(search_name_error_message + '\n' + error_message + '\n')
            # 찾은이름의 인덱스번호를 찾은 후 이름리스트와 가격리스트에서 이름과 가격을 찾아 출력함
            else:
                searched_index = name_list.index(searched_name)
                print(search_name_message,name_list[searched_index])
                print(search_price_message,price_list[searched_index])
        #가격 검색
        elif search_select_number == 2:
            # 가격을 입력받음
            searched_price = int(input(search_price_message))
            # 오차범위 설정
            min_searched_price = 0.5*searched_price
            max_searched_price = 1.5*searched_price
            # 오차범위 내에서 검색이 된다면
            for i in price_list:
                if min_searched_price < i < max_searched_price:
                    # 그 금액의 인덱스 번호를 찾고 출력
                    searched_price_index = price_list.index(i)
                    print(name_list[searched_price_index],price_list[searched_price_index])
                else:
                    print(search_error_message + '\n')
        # 이름검색, 가격 검색 둘다 아닌 범주를 입력하면 에러메시지 출력
        else:
            print(search_error_message + '\n' + error_message + '\n')



    #목록
    elif user_number == 5:
        if len(name_list) == 0:
            print(no_item_message)
        else:

            print(search_name_message, name_list )
            print(search_price_message, price_list )

    elif user_number ==  6:
        break

    else:
        print(no_item_message + '\n' + error_message + '\n')







