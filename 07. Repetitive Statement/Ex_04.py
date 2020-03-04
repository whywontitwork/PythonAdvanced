### range 함수 ###

'''

    range(종료값)               : 0 ~ 종료값-1 까지 반복가능한 객체 생성
    range(시작값,종료값)        : 1 ~ 종료값-1 까지 반복가능한 객체 생성
    range(시작값,종료값,증감값) : 시작값 ~ 종료값-1까지 증감값이 반영된
                                  반복 가능한 객체 생성

'''

print(range(10))        # 0 ~ 9
print(type(range(10)))

for i in range(10):
    print(i)

print(range(10,101,10))   # 10,20,30 ... 80,90,100
for i in range(10,101,10):
    print(i)

print(range(10,31))       # 10 ~ 30
for i in range(10,31):
    print(i)


# 예외) 내림차순일 경우에는 증감값에 -1을 반드시 적어줍니다.
#for i in range(100,0):     # X
for i in range(100, 0,-1):  # O
    print(i)

