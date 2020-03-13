### 지역변수 , 전역변수 ###

var = "global_var"      # 전역변수

def fun1():
    var = "local_var1"   # 지역변수
    print(var)

def fun2():
    var = "local_var2"   # 지역변수
    print(var)

print(var)   # 전역변수
fun1()       # fun1의 지역변수
fun2()       # fun2의 지역변수
print()


global_var = "전역변수"

def show_var1():
    print(global_var)
    local_var1 = "지역변수1"
    print(local_var1)
    #print(local_var2)

def show_var2():
    print(global_var)
    local_var2 = "지역변수2"
    print(local_var2)
    #print(local_var1)

print(global_var)
print()
show_var1()
print()
show_var2()
print()


global_var = 100

def func1():
    global global_var  # 지역변수에서 전역변수를 변경하려면
                       # global 전역변수를 함수 안에서 선언해주고 사용합니다.
    global_var += 100
    print(global_var)

def func2():
    global global_var
    global_var += 100

func1()
print(global_var)      # ?
func2()
print(global_var)      # ?