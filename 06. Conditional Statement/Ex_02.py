### if ~ else문 ###

'''
    - [형식]
    if 조건식:     (조건식이 True이면 명령어가 수행된다.)
        명령어
    else:          (조건식이 False이면 명령어가 수행된다.)
        명령어

    - else는 if없이 단독으로 올 수 없다.
    - else문 뒤에는 조건을 명시하지 않는다.


'''

print("--- start ---")
data = 60

if data >= 60:
    print("명령어1")
    print("명령어2")
else:
    print("명령어3")
    print("명령어4")

print("--- end ---")