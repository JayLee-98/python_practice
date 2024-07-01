# 집합 (set): 중복 안됨, 순서 없음

my_set = {1, 2, 3, 3, 3}
print(my_set) # 중복된 숫자 3은 최초로 나온 3 하나만 세트에 들어감.

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트를 만들고 set로 () 감싸줄 수 있음. 선언하는 다른 방법임.

# 교집합 출력 (java와 python을 모두 할 수 있는 개발자 출력)
print(java&python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나, python을 할 수 있는 개발자 출력)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자 출력)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 개발자가 늘어남
python.add("김태호")
print(python)

# java를 까먹은 개발자
java.remove("김태호")
print(java)