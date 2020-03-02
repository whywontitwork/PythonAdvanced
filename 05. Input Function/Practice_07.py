# 화폐매수를 계산하는 코드를 '해석'해 보세요.

#1번
salary = int(input("# how ? :"))

print("5만원권: %d장" %(salary // 50000))
print("1만원권: %d장" %(salary % 50000 // 10000))
print("5천원권: %d장" %(salary % 50000 % 10000 // 5000))
print("1천원권: %d장" %(salary % 50000 % 10000 % 5000 // 1000))
print("잔   금: %d원" %(salary % 50000 % 10000 % 5000 % 1000))
print()

#2번
salary = int(input("# how ? :"))

w50000 = salary // 50000  # 5만권 개수
salary %= 50000  #50000으로 나눈 나머지

w10000 = salary // 10000 # 1만권 개수
salary %= 10000 # 10000으로 나눈 나머지

w5000 = salary // 5000  # 5천원권 개수
salary %= 5000  # 5000으로 나눈 나머지

w1000 = salary // 1000 # 1천원권 개수
salary %= 1000  # 1000으로 나눈 나머지

print("5만원권 : %d장" % w50000)
print("1만원권 : %d장" % w10000)
print("5천원권 : %d장" % w5000)
print("1천원권 : %d장" % w1000)
print("잔   금 : %d원" % salary)



