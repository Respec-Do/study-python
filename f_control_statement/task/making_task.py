#if 문
'''
    미국당뇨병학회에서는 45세 이상 모든 성인에게 당뇨병 선별검사를 위한 혈당검사를 받도록 권고하고있음.
    45세 이전이라도 당뇨병 발생의 위험인자(비만, 임신성당뇨병, 고혈압)이 있으면 매년 혈당검사를 시행할 것을 권고함

    공복상태 혈당검사
    정상치 :  70~99mg/l
    공복혈당장애 : 100~125mg/l
    당뇨병 :  126mg/l

    사용자에게서 이름, 나이, 공복상태 혈당검사 및 이전 검사에서 당뇨병단계(공복혈당장애 포함)의 정보를 받아
    공복상태 혈당검사의 수치에 따른 진단과 매년 혈당검사의 대상인지 아닌지를 판단하시오.
    ----------------------------------------------------------------------------------

    ex) 이름을 입력하세요 : 홍길동
        나이를 입력하세요 : 43세
        공복상태혈당검사 수치를 입력하세요 : 124 mg/l
        당뇨병 발생의 위험인자(비만, 임신성당뇨병, 고혈압) 진단을 받았나요? y/n : y

    ------------------------------------------------------------------------------------

        실행결과
        홍길동 씨는 공복상태혈당검사 수치에서 124 mg/l 로 공복혈당장애 를 판정받으셨습니다.
        또한 위험인자진단을 통해 매년 혈당검사를 시행할 것을 권고합니다.

'''

'''
    for/while 복합문제
    정수를 입력하고 입력한 줄 수만큼 별('*')을 출력하시오
    
    예시
        정수 입력: 4
        
    출력 예시
        정수 입력: 4
         ******* 
          *****  
           ***   
            *    

'''

num = int(input("정수 입력: ")) #2
count = 0
blank = ' '
star = '*'
while num > 0:

    for i in range(1,num+1): #1,2
        count = num * 2 - 1 #3
        for j in range(i):
            print(blank, end='')
        for j in range(count):
            print(star, end='')
        for j in range(i):
            print(blank, end='')
        print()
        num -= 1