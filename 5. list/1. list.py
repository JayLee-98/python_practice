# 리스트 []

# 지하철 칸별로 10명, 20명, 30명이 존재함.
subway1 = 10
subway2 = 20
subway3 = 30

# 연속적인 공간에 묶은 것이 리스트임.
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는지?
print(subway.index("조세호")) # 1번째 인덱스 지하철에 조세호가 있음.

# 하하씨가 다음 정류장에서 다음 칸에 탐.
subway.append("하하") # append()는 항상 리스트 맨 뒤에 추가함.
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # insert()가 실행되기 전 유재석, 조세호, 박명수, 하하가 리스트에 있기때문에 변경 전 인덱스 1번 자리인 조세호 자리에 정형돈이 추가된 뒤에 기존에 리스트 안에 있던 값들이 뒤로 한 칸씩 밀리게 됨.
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 맨 뒤에 있던 하하가 pop됨.
print(subway) # 하하가 pop되었기때문에 하하를 제외한 나머지만 리스트에 존재함.

# 같은 이름의 사람이 몇 명인지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 오름차순 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 내림차순 정렬도 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용할 수 있음
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 2, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)