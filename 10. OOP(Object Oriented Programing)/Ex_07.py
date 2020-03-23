### 메서드의 호출 ###

'''

    함수의 호출                   : 함수명()
    같은클래스의 다른 메서드 호출 : self.메서드명()
    부모클래스의 메서드 호출      : super().메서드명()

'''
def function():
    print("Call Function")


class Parent:
    def parentMethod(self):
        print("Call parentMethod")

class Child(Parent):

    def childMethod(self):
        print("Call ChildMethod")

    def parentMethod(self):
        print("override parentMethod")

    def testMethod(self):
        print("testMethod")
        self.childMethod()       # 같은 클래스의 메서드 호출
        function()               # 함수 호출
        self.parentMethod()      # 오버라이드 된 부모메서드 호출
        super().parentMethod()   # 부모메서드 직접 호출



obj = Child()
obj.testMethod()







