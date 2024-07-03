class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
    
# class FlyableUnit(Unit, Flyable): # 이 상태로 FlyableUnit을 호출하면, Unit만 타고 Flyable은 타지않음.
# class FlyableUnit(Flyable, Unit): # 이 상태로 FlyableUnit을 호출하면, Flyable만 타고 Unit은 타지않음.
    # def __init__(self):
    #     super().__init__()
    
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self) # super()을 통해서 생성자 작성하지않고 다중상속하고자하는 클래스의 생성자를 모두 명시해줘야 누락되지 않음.
        Flyable.__init__(self)
        
# 드랍쉽
dropship = FlyableUnit() 