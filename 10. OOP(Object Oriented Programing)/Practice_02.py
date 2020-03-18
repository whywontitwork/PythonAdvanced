# 헷갈리기 쉬운 생성자,메소드 비교
class Calc1:
    def add(self,arg1,arg2):
        return arg1+arg2

myCal = Calc1()
print(myCal.add(10,5))         # 15
print(myCal.add(100,50))       # 150


class Calc2():

    def setData(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def add(self):
        return self.arg1 + self.arg2

myCal = Calc2()
myCal.setData(10,5)
print(myCal.add())      # 15
print(myCal.add())      # 15


class Calc3:
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def add(self):
        return self.arg1 + self.arg2

myCal = Calc3(10,5)
print(myCal.add())      # 15
