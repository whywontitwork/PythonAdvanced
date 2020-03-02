### Continue ###

'''

    - 반복문 안에 위치하여 반복문의 다음 조건으로 점프합니다.
    - 반복문 없이 단독으로 올 수 없습니다.

'''

while True:
    getData = input("아무키나 입력 : ")
    if getData == 'q':
        continue
    print("명령어1")
    print("명령어2")
    print("명령어3")
    print(getData)
