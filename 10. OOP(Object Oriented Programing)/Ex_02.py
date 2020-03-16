### 클래스 변수 , 인스턴스 변수 ###

'''

    - 클래스 변수
    1) 모든 인스턴스가 공유하는 저장 영역
    2) 인스턴스가 생성되기 이전에 이미 메모리에 상주 되어 있다.
    3) 클래스이름.클래스변수로 접근이 가능하다.

    - 인스턴스 변수
    1) 특정 인스턴스만 사용하는 고유한 저장 영역
    2) 인스턴스가 생성되는 시점에 메모리에 상주한다.
    3) 인스턴스명.변수로 접근이 가능하다.

'''

class Zealot:

    hp     = 100
    shield = 60
    damage = 16

    def status(self):
        print("체력 : " + str(self.hp))
        print("쉴드 : " + str(self.shield))
        print("공격력 : " + str(self.damage))
        print()


print("- 질럿1 -")
unit1 = Zealot()
unit1.status()

unit1.shield -= 17   # unit1의 인스턴스 변수를 수정
print("쉴드 감소후")
unit1.status()

print("-질럿2-")
unit2 = Zealot()
unit2.status()

unit2.shield -= 50     #unit2의 인스턴스 변수를 수정
unit2.hp     -= 100
print("체력,쉴드 감소후")
unit2.status()

Zealot.damage += 2     # 클래스 변수의 수정

print("-질럿3-")
unit3 = Zealot()
unit3.status()



