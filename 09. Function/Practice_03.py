# 1부터 내가 입력한 값까지의 합을 반환하는 함수를 만들어보세요.

# def calc_total(getNumber):
#     total = 0
#     for i in range(1,getNumber+1):
#         total += i
#     return total
#
# getNumber = int(input("# input Number : "))
# res = calc_total(getNumber)
# print(res)


# while문으로 구구단 2단 출력하는 함수를 작성해보세요.
def print_gugudan_2dan():
    idx = 0
    while idx < 9:
        idx += 1
        print("2 * %d = %d" % (idx , 2 * idx))

print_gugudan_2dan()

# for문으로 구구단 2단 출력하는 함수를 작성해보세요.
def print_gugudan_2dan():
    for i in range(1,10):
        print("2 * %d = %d" %(i,2*i))

print_gugudan_2dan()


# 내가 입력한 값부터 내가 입력한 값까지의 합을 반환하는 함수를 만들어 보세요.

def adder(startNum , endNum):
    total = 0
    for i in range(startNum,endNum+1):
        total += i
    return total

getStartNum = int(input("# startNum : "))
getEndNum = int(input("# endNum : "))

res = adder(getStartNum,getEndNum)
print(res)

















