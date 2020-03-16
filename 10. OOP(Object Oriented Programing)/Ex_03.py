### 인스턴스 변수 ###


class Person:

    def setData(self,name,age,gender,contact,address,etc):
        self.name    = name
        self.age     = age
        self.gender  = gender
        self.contact = contact
        self.address = address
        self.etc     = etc

    def printInfo(self):
        print("이름 : " + self.name)
        print("나이 : " + str(self.age))
        print("성별 : " + self.gender)
        print("연락처 : " + self.contact)
        print("주소 : "+ self.address)
        print("특이사항 : " + self.etc)
        print()


p1 = Person()
p1.name     = "홍길동"
p1.age      = 35
p1.gender   = "남자"
p1.contact  = "010-9876-5432"
p1.address  = "강남구 역삼동"
p1.etc      = "없음"
p1.printInfo()


p2 = Person()
p2.name     = "성춘향"
p2.age      = 17
p2.gender   = "여자"
p2.contact  = "010-1523-7894"
p2.address  = "강남구 역삼동"
p2.etc      = "따뜻한사람"
p2.printInfo()

p3 = Person()
p3.setData("이몽룡",17,"남자","010-1234-5678","수원 광교","똑똑한 사람")
p3.printInfo()

p4 = Person()
p4.setData("임꺽정",34,"남자","010-9875-5201","용인 흥덕","강한 사람")
p4.printInfo()


