class Unit:
    def __init__(self, name, hp, damage): # __init__은 생성자임.
        self.name = name        # 클래스내에서 선언된 변수가 멤버변수임.
        self.hp = hp            # 클래스내에서 선언된 변수가 멤버변수임.
        self.damage = damage    # 클래스내에서 선언된 변수가 멤버변수임.
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 능력 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 클래스를 선언할때 클로킹이라는 변수를 추가로 할당한 것임.
                        # 하지만 내가 확장된 변수는 내가 확장한 변수에만 적용이 됨.
                        # 그렇기 떄문에 wraith1.clocking은 사용할 수가 없는 것임.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))