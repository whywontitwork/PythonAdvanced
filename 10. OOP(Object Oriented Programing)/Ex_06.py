### 상속 (Inheritance) ###
'''

    1) 상속에 관련된 클래스는 부모(조상,상위,기반)클래스와 자녀(자손,하위,파생)클래스로 구분됩니다.
    2) 자녀클래스는 부모 클래스의 모든 자원(생성자,메서드,변수)등을 상속받아서 그대로 사용할 수 있습니다.
    3) 자녀 클래스는 부모 클래스의 메서드를 수정해서 사용할 수 있습니다. (메소드 오버라이딩,메소드 재정의)
    4) 자녀클래스는 부모 클래스의 메서드 외의 자신만의 메소드를 추가해서 사용할 수 있습니다.
    5) 파이썬에서는 다중상속이 가능합니다.
    6) 파이썬에서는 메서드 오버로딩(중복정의)를 지원하지 않습니다.

'''



class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def printInfo(self):
        print("===================")
        print("이름 : %s" % self.name)
        print("나이 : %d" % self.age)
        print("===================")
    def sleep(self):
        print("sleep method(parent)")

animal = Animal("동물",15)
animal.printInfo()
animal.sleep()
print()


# 상속받는 방법 : class 클래스명()  <- 소괄호 안에 부모클래스의 이름을 넣어줍니다.
class Dog(Animal):
    
    # 메서드 오버라이딩(메서드 재정의)
    # 부모클래스의 메서드를 재정의 사용하는 구문
    def sleep(self):
        print("sleep method (child Dog)")


dog = Dog("기쁨",7)
dog.printInfo()
dog.sleep()
print()

class Cat(Animal):
    # 메소드 오버라이딩(메소드 재정의)
    def sleep(self):
        print("sleep method child Cat")
    # 자신만의 메소드 추가
    def sound(self):
        print("Ya yong")


cat = Cat("노랭이",5)
cat.printInfo()
cat.sleep()
cat.sound()
#dog.sound()    # cat만의 메소드 >  error

