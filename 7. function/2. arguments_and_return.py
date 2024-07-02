def open_account():
    print("새로운 계좌가 생성되었습니다.")
    
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance > money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금에 실패하였습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 이는 파이썬의 다중 반환 기능으로, 함수에서 여러 값을 반환할 수 있고, 이를 여러 변수에 각각 저장할 수 있는 기능을함.

balance = 0 # 초기 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission,balance = withdraw_night(balance, 400)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 파이썬의 다중 반환 기능
def return_multiple_values():
    return 1, 2, 3

a, b, c = return_multiple_values()
print(a)  # 1
print(b)  # 2
print(c)  # 3