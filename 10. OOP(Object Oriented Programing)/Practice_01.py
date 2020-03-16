class Cat:

    def info(self,name,age,color):
        self.name  = name
        self.age   = age
        self.color = color
    def printInfo(self):
        print("=======================")
        print("고양이 이름 : " + self.name)
        print("고양이 나이 : " + str(self.age))
        print("고양이 색깔 : " + self.color)
        print("======================")


mycat = Cat()
mycat.info("루비",5,"흰색")
mycat.printInfo()