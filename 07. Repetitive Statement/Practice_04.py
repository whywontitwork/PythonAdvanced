
# while
idx = 17
while (idx > 0):
    print("현재 배터리의 용량은 %d입니다." % idx)
    if idx == 10:
        print("전원이 부족합니다. 배터리를 충전해주세요.")
    idx -= 1
print("배터리가 부족하여 전원을 종료합니다.")
print()


# for문
for i in range(17,0,-1):
    print("현재 배터리의 용량은 %d입니다." % i)
    if i == 10:
        print("전원이 부족합니다. 배터리를 충전해주세요.")

print("배터리가 부족하여 전원을 종료합니다.")
print()




