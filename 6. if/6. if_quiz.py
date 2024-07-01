# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신의 소요 시간은 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분
from random import *

# 1트 => 내가 작성한 오답을 정답에 맞춰 수정함
count = 0
for customers in range(1, 51):
    riding_time = randrange(5, 50)
    if 5 <= riding_time <= 15:
        print(f"[0] {customers}번째 손님 (소요시간 : {riding_time})분)")
        count += 1
    else:
        print(f"[ ] {customers}번째 손님 (소요시간 : {riding_time}분)")
    # print(f"총 탑승 승객 : {customerNum} 분")
print(f"총 탑승 승객 : {count}")
# 오답노트
# 1. riding_time = randrange(5, 50)에서 randrange 대신 randint를 사용함.
# 2. 탑승한 승객의 수를 for문 안에서 작성함.
# 3. riding_time으로 이중 포문을 사용함.


# 2트
# index = 1
# riding_time = str(randint(5, 50))
# for customers in list(range(1, 51)):
#     while customers[0:]:
#         index += 1
#         if "5" <= riding_time >= "15":
#             print(f"[0] {index}번째 손님 (소요시간 : {riding_time})분)")
#             customersNum = customers + 1
#         else:
#         print(f"[ ] {index}번째 손님 (소요시간 : {riding_time}분)") 

# 정답
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 ~ 50이라는 승객 수
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        
# print("총 탑승 승객 : {0}분".format(cnt))