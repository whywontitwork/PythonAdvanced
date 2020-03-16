### 생성자(Constructor) ###

'''

    1) 인스턴스를 생성할 때 가장 먼저 실행된다.
    2) 인스턴스를 생성할 때 반드시 실행된다.
    3) 모든 클래스는 반드시 1개의 생성자를 가진다.
    4) 생성자를 만들지 않을 경우 기본생성자를 자동으로 생성한다.

    [형식]
    def __init__(self):
        명령어

'''

# 생성자를 만들기 전
class Singer:

    def setData(self,name):
       self.name = name

    def performance(self):
        print("%s는 공연중:)" % self.name)

singer1 = Singer()
#singer1.setData("Adele")
#singer1.performance()

'''

Singer클래스의 잠재적 위험은
setData메소드를 
1) 아예 호출하지 않을 수도 있고,
2) performance메소드 이후에 호출할 수도 있는 '가능성'입니다.
위의 2 가지 가능성을 모두 해결해주는 문법이 생성자 입니다.

'''

# 생성자를 만든 후
class Singer:

    def __init__(self,name):
        self.name = name

    def performance(self):
        print("%s는 공연중:)" % self.name)

singer2 = Singer()
singer2.performance()
