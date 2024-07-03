# 오버라이딩 : 부모 클래스에서 정의한 메소드가 아닌 자식 클래스에서 정의한 메소드를 사용하고 싶을때 메소드를 새롭게 정의해서 사용할 수 있음.

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name   
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")        
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
                                                       
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
       
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속을 위해서는 콤마로 나열하면 됨.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 0의 의미: 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # (방법 1) Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)   # (방법 2) super를 사용한 생성자 생성.
                                        # 1. super 뒤에 ()를 사용. 
                                        # 2. 인자에 self를 붙이지 않음.
        self.location = location
