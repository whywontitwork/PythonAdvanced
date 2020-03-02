### 중첩 if문 ###

'''
    - 중첩if문 문법이 별도로 존재하는 것이 아니라
      if 문안의 명령어에 if or elif or else가 포함되어 있는 복합 구조

    - 들여쓰기를 통하여 if문의 범위를 구분한다.
'''

grade = 99

if grade >= 60:
    if grade == 100:
        print("만점")
    print("합격")

else:
    print("불합격")

