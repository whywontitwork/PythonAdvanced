### 함수의 4가지 형태 ###

'''

    - 입력값(입력인수)과 결과값(return)의
      유무에 따라 4가지 형태로 나뉩니다.

      1) 입력값이 있고 결과값이 있다. 11
      2) 입력값이 없고 결과값이 있다. 01
      3) 입력값이 있고 결과값이 없다. 10
      4) 입력값이 없고 결과값이 없다. 00

'''


# 1) 입력값이 있고 결과값이 있다. 11
def def_type_11(param1,param2):
    return param1 + param2

res = def_type_11(100,10)
print(res)
print()


# 2) 입력값이 없고 결과값이 있다. 01
def def_type_22():
    return 3.14

res = def_type_22()
print(res)
print()

# 3) 입력값이 있고 결과값이 없다. 10
def def_type_10(param1,param2):
    return param1 *param1

def_type_10(777,77)
# print(def_type_10(777,77))    #None
print()

# 4) 입력값이 없고 결과값이 없다. 00
def def_type_00():
    print("================================")

def_type_00()