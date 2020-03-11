### 오류,예외 처리 ###
'''

    - 프로그램 개발시 개발자가 예상하지 못했던 동작이나,
      오류에 대해서 대비가 필요합니다.

    - try , except 중 반드시 한 구문은 수행이 됩니다.
    - except는 try 없이 단독으로 올수 없습니다.

'''

try:    # 오류가 발생되지 않았을 때 정상적으로 수행될 명령어
    getSalary = int(input("# salary : "))
    print("\nOk! Salary : %d" % getSalary)

except:  # 오류가 발생했을 때 수행될 명령어
    print("숫자를 입력하세요.")

print()

while True:
    try:    # 오류가 발생되지 않았을 때 정상적으로 수행될 명령어
        getSalary = int(input("# salary : "))
        print("\nOk! Salary : %d" % getSalary)
        break

    except:  # 오류가 발생했을 때 수행될 명령어
        #print("숫자를 입력하세요.")
        pass   # 아무의미없이 비워둘 경우 pass 명령어를 사용






