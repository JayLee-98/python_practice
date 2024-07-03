class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name   
        self.hp = hp        
        self.damage = damage 
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
        
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self는 자기자신을 의미함
                                                       # 클래스내에서 메소드 앞에는 항상 self를 명시해야함.
                                                       # self.name과 self.damage는 클래스내에 선언된 값을 사용하겠다는 의미고
                                                       # location은 attack() 메소드가 실행될때 전달받는 인자를 사용하겠다는 의미임.
                                                       
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("도시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
