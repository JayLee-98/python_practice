gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
# 전역변수를 남용하다보면 코드가 지저분해지기 때문에 코드 가독성 저하됨.
# 지역변수를 활용하는 방법은 아래와 같음.
def checkpoint_ret(gun, soldiers): # 전역변수를 함수의 인자로 전달받아서 사용하면 지역변수처럼 사용할 수 있음.
    gun = gun - soldiers
    print("[함수 내] 남은 총 수 : {}".format(gun))
    return gun  # 함수 밖으로 반환하게 될 경우 지역변수를 다시 전역변수처럼 사용할 수 있음.
    
print("전체 총 수 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 수 : {0}".format(gun))