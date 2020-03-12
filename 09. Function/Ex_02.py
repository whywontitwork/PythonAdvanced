### return ###

'''

    - 값을 반환합니다.
    - 함수를 종료합니다.

'''

def return_ex1():
    print("출력문1")
    print("출력문2")
    print("출력문3")
    return "반환값1" # 첫번째 return을 만나는 순간
                    # 값을 반환하고 함수는 종료됩니다.
    print("출력문4")
    print("출력문5")
    return "반환값2"

res1 = return_ex1()
print(res1)


def return_ex2(param):

    #분기문이 있을 경우 상황에 따라 return을 여러번 사용 할 수 있다.
    if param == True:
        return "switch on"
    else:
        return "switch off"

print(return_ex2(True))
print(return_ex2(False))





