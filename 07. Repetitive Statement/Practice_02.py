idx = 0
while idx < 9:
    idx += 1
    print("%d * %d = %d" %(2,idx,2*idx))
    #print("2","*",idx,"=",2*idx)


# for문으로 구구단 2단 출력

# for문으로 내가 입력한 단수의 구구단을 출력
getGrade = int(input("# grade : "))

for i in range(1,10):
    print("%d * %d = %d" % (getGrade, i , getGrade*i))

# while문으로 내가 입력한 단수의 구구단을 출력

# for문으로 1부터 1000까지의 총합 구하기
total = 0
for i in range(1000):
    total += i
print(total)

# while문으로 1부터 1000까지의 총합 구하기

# for문으로 1부터 내가 입력한 값까지의 총합 구하기
getNumber = int(input("# input Number : "))
total = 0
for i in range(1,getNumber+1):
    total += i
print(total)


# while문으로 1부터 내가 입력한 값까지의 총합 구하기





