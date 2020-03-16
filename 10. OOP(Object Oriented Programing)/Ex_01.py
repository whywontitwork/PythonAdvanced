### 클래스의 기초 ###


class Character: # 클래스의 이름은 대문자로 합니다.

    level = 1    # 클래스 변수 , 멤버 변수 : 모든 인스턴스가 공유하는 저장공간
    power = 10
    dex   = 10
    life  = 10
    mana  = 10

    def attack(self):  # 인스턴스 메소드 : 인스턴스가 사용가능 합니다.
        print("기본 공격 (damage 10)")

user1 = Character() # 인스턴스 생성
print(user1.level)
print(user1.power)
print(user1.dex)
print(user1.life)
print(user1.mana)
user1.attack()
print()


user2 = Character()
print(user2.level)
print(user2.power)
print(user2.dex)
print(user2.life)
print(user2.mana)
user2.attack()
print()

# 클래스 변수를 외부에서 수정
Character.power   = 25            # 클래스명.클래스변수명으로 접근
Character.dex     = 25
Character.life    = 25
Character.mana    = 25

user3 = Character()
print(user3.level)       # 변경된 클래스 변수가 적용 됩니다.
print(user3.power)
print(user3.dex)
print(user3.life)
print(user3.mana)
user3.attack()
print()