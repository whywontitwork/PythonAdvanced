### 가변인자 처리 하기 ###

'''
    매개변수,인수,인자,아규먼트,파라메타
'''
def show_data1(arg):
    print("인수 : " , arg)

show_data1('a')
#show_data1('a','b')    # error
#show_data1('a','b','c') # error
print()


def show_data2(*args):     # 가변인자로 받아줄 경우 , 인자 앞에 *를 붙여줍니다.
    print("인수 : " , args)

show_data2('a')
show_data2('a','b')
show_data2('a','b','c')
print()


def show_data3(arg1,arg2,*args): #가변인자처리는 1) 맨뒤에서 2) 한번만 가능하다.
    print("arg1 :", arg1)
    print("arg2 :", arg2)
    print("args :", args)

#show_data3('a')      # error
show_data3('a','b','c')
show_data3('a','b','c','d')
show_data3('a','b','c','d','e')