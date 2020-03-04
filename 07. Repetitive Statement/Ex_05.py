### for 문 ###

'''

    - 파이썬의 for문의 다른언어의 for문 문법과 다르다.

    [ 형식 ]
    for 변수 in 반복가능한자료형:
        명령어

    - 반복가능한자료형의 개수만큼 반복문의 수행되며
      반복가능한자료형의 데이터가 한번씩 변수에 담기는 형태로 수행된다.


'''

print("--- start ---")
for i in range(1,11):
    print(i,end=" ")
print()
print("--- end ---")

print("--- start ---")
for i in [1,2,3,4,5]:       # 리스트
    print(i,end=" ")
print()
print("--- end ---")

print("--- start ---")
for i in (6,7,8,9,10):       # 튜플
    print(i,end=" ")
print()
print("--- end ---")


print("--- start ---")
for i in "string data":     # 문자열
    print(i,end=" ")
print()
print("--- end ---")













