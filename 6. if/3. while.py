# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 음료가 준비되었습니다. {1}번 호출 숫자가 남았습니다.".format(customer, index-1))
    index -= 1
    if index == 1:
        print("{0}님, 마지막 호출입니다. 이번에도 음료 수령하지 않으시면 폐기처분합니다.".format(customer))
    if index == 0:
        print("음료가 폐기처분 되었습니다.")
        
customer2 = "아이언맨"
index2 = 1
# while True:
#     print("{0}님, 음료가 준비되었습니다. {1}번 호출 숫자가 남았습니다.".format(customer2, index2-1))
#     index2 += 1

customer3 = "그루트"
person = "Unknown"
while person != customer3:
    print("{0}님, 커피가 준비되었습니다.".format(customer3))
    person = input("이름이 어떻게 되세요? ")