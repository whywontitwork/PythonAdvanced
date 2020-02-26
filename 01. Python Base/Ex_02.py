### 출력함수 print() ###

#1) print()함수는 ()안에 있는 데이터를 화면에 출력한다.
#   print()함수는 개행(new line)기능이 내장되어 있다.

print(1)                # 정수
print(3.14)             # 실수
print('C')              # 문자 ( 파이썬은 문자열과 같다 )
print("String")         # 문자열
print([1,2,3])          # 리스트
print((1,2,3))          # 튜플
print({"key":"value"})  # 사전(딕셔너리)
print()                 # 한줄 개행


#2) print()함수는 복수의 데이터를 ,로 구분하여 출력이 가능하다.
#  , 를 사용했을 경우 띄어쓰기 형태로 출력된다.

print("start",1,2,3,4,5,"end")
print()

#3) sep(seperator) : print()함수 안의 , 의 출력서식을 지정한다.

print("start",1,2,3,4,5,"end" , sep="/")
print("start",1,2,3,4,5,"end" , sep="@")
print("start",1,2,3,4,5,"end" , sep="")
print("start",1,2,3,4,5,"end" , sep=">")

#4) end : print()함수와 print()함수 사이의 출력서식을 지정한다.
print("start",1,2,3,4,5,"end" , end="")
print("start",1,2,3,4,5,"end" , end="###")
print("start",1,2,3,4,5,"end" , end="@@@")
print("start",1,2,3,4,5,"end")








