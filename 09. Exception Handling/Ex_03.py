### try , except , finally ###

'''

    - try 구문 수행도중 예외상황에 관계없이 반드시 동작한다.
    - 주로 외부와의 연결을 안전하게 종료해야 될 경우 사용된다.
        Ex) DB connection close, file close

'''

try:
    getSalary = int(input("#Salary : "))
    print("Ok! Salary : %d" % getSalary)
except:
    print("오류 발생")
finally:
    print("반드시 수행되는 구문!")







