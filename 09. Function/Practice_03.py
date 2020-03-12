# 1부터 내가 입력한 값까지의 합을 반환하는 함수를 만들어보세요.

def calc_total(getNumber):
    total = 0
    for i in range(1,getNumber+1):
        total += i
    return total

getNumber = int(input("# input Number : "))
res = calc_total(getNumber)
print(res)


