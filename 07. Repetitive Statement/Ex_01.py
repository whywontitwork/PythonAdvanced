### 반복문 ###
'''

    동일한 명령어 혹은 동일한 패턴의 명령어를
    반복적으로 실행해야 할 경우 사용하는 문법

    1) while 문의 형식
        while 조건식:
            명령어
    2) while문은 조건식이 True(참)인 동안에
        while문 안의 들여쓰기된 명령어들을 반복적으로 수행한다.

'''

idx = 0     # while문의 조건식을 False로 만들기 위한 변수

print("---- start of loop ----")

while idx < 10:
    idx += 1
    print("%d. Loop Statement" % idx)
    #idx += 1

print("---- end of loop ----")




