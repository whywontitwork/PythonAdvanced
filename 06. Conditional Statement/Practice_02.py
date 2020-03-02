# bmi 산출하기
# http://www.marathon.pe.kr/diet/bmi_cal.html

getHeight = float(input("# 키: "))
getWeight = float(input("# 몸무게: "))

getHeight /= 100 # cm -> m

bmi = getWeight / (getHeight * getHeight)
print(bmi)

if bmi >= 30.0:
    print("비만")
elif bmi >= 25.0:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")