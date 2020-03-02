'''

 나이를 입력받고
 6세 이하 70세 이상이면 '무료입장'을 출력
 7세부터 69세까지는 '입장료 3000원'을 출력

'''
getAge = int(input("# age: "))

if getAge <= 6 or getAge >= 70:
    print("무료입장")
else:
    print("입장료 3000원")


