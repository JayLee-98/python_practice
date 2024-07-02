print("Python", "Java", sep=",", end="?") # spe 즉, separator를 사용하면 각각의 데이터 사이에 넣을 값을 지정할 수 있음.
print("무엇이 더 재밌을까요?")

# end는 문장의 끝부분을 ?로 바꿔달라고 하는 역할임. 두 문장이 한 문장으로 연달아 출력됨.

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장이 출력됨.
print("Python", "Java", file=sys.stderr) # 표준 에러로 처리가 됨.

# 시험성적
scores = {"수학":0, "영어":50, "코딩":100} # dictionary 자료형
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=": ")   # 콘솔에 출력할때 정렬할 수 있음. 
                                                             # ljust(4)의 의미: 왼쪽으로 정렬하되, 총 4칸의 자리를 확보해라.

# 은행 대기순번표
# 001, 002, 003, ... 
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(3)의 의미: 3칸만큼의 공간을 확보하고, 빈 값은 0으로 채워넣어라.
    
answer = input("아무 값이나 입력하세요 : ") # input을 통해서 입력받는 값의 타입은 모두 문자열임.
print(type(answer))
print("입력하신 값은 " + answer + " 입니다.")