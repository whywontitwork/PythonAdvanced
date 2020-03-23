import random


class Beginner:

    def __init__(self):
        self.user_id = input("id를 생성해주세요: ")
        self.level = 1
        self.power = 5
        self.dex = 5
        self.life = 5
        self.mana = 5

        print("\n%s 계정이 생성되었습니다." % self.user_id)

    def attack(self):
        print("\n기본공격 (데미지7)")

    def print_info(self):
        print("\n================")
        print("계정 : %s" % self.user_id)
        print("레벨 : %d" % self.level)
        print("================")
        print("POWER : %d" % self.power)
        print("DEX   : %d" % self.dex)
        print("LIFE  : %d" % self.life)
        print("MANA  : %d" % self.mana)
        print()

    def level_up(self):
        self.level += 1
        self.power += 5
        self.dex += 5
        self.life += 5
        self.mana += 5
        print("\n레벨이 올랐습니다. 현재 레벨 : %d" % self.level)


class Amazon(Beginner):

    # 메서드 오버라이딩
    def level_up(self):
        self.level += 1
        self.power += 8
        self.dex += 15
        self.life += 7
        self.mana += 5
        print("\n레벨이 올랐습니다. 현재 레벨 : %d" % self.level)

    def multyshot(self):
        if self.level >= 3:

            damage = random.randint(30, 50)
            print("multyshot (데미지 %d)" % damage)

            if random.randint(1, 2) == 1:
                cri_damage = random.randint(90, 100)
                print("critical Attack (데미지%d)" % cri_damage)

        else:
            print("아직 스킬을 사용할 수 없습니다.")


class Warrior(Beginner):
    # 메서드 오버라이딩
    def level_up(self):
        self.level += 1
        self.power += 15
        self.dex += 10
        self.life += 8
        self.mana += 5
        print("\n레벨이 올랐습니다. 현재 레벨 : %d" % self.level)


class Wizard(Beginner):
    # 메서드 오버라이딩
    def level_up(self):
        self.level += 1
        self.power += 5
        self.dex += 8
        self.life += 10
        self.mana += 15
        print("\n레벨이 올랐습니다. 현재 레벨 : %d" % self.level)