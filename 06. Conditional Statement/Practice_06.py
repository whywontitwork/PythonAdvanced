'''

id와 pwd를 입력받고 기존의 문자열과 비교하여 모두 일치하면
'성공적으로 로그인 되었습니다.' 출력
그렇지 않으면
'로그인에 실패하였습니다.' 출력

'''

db_id  = "funPython"
db_pwd = "qwer1234"

getId  = input("ID :")
getPwd = input("PWD : ")

if getId == db_id and getPwd == db_pwd:
    print("성공적으로 로그인 되었습니다.")
else:
    print("로그인에 실패하였습니다.")




