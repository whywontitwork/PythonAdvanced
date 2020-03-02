### if ~ elif문 ###

'''
    - [형식]
    if 조건식:
        명령어
    elif 조건식:
        명령어
    elif 조건식:           ( 필요에 따라 여러개의 elif가 가능합니다. )
        명령어
    else:    ( else는 필요에 따라 사용해도 되고 사용하지 않아도 됩니다. )
        명령어

    - if 조건식이 거짓일 경우 다음 elif문으로 분기한다.
    - if문 없이 단독으로 올 수 없다.
    - else문과 같이 사용 가능하되, else문은 항상 맨 아래 있어야 한다.

'''

getGrade = int(input("#input grade : "))

if getGrade >= 90:
    print("1등급")
elif getGrade >= 80: # 처음 if가 False일 경우 실행
    print("2등급")
elif getGrade >= 70: # 바로 위의 elif가 False일 경우 실행
    print("3등급")

