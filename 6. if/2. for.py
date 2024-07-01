# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4]: # for문을 돌때 리스트안의 범위의 숫자를 넣도록 작성함.
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(5): # 0부터 5 미만의 숫자까지의 숫자까지 지정함. 즉 0~4의 숫자가 출력됨.
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(1, 6): # 1부터 6 미만의 숫자까지의 숫자까지 지정함. 즉 1~5의 숫자가 출력됨.
    print("대기번호 : {0}".format(waiting_no))
    
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님, 주문하신 음료가 준비되었습니다.".format(customer))