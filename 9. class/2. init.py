class Unit:
    def __init__(self, name, hp, damage): # __init__은 생성자임.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린") self를 제외한 나머지 인자들 만큼 instance를 생성해야함.