# 출석번호가 1 ~ 4가 있는데, 교칙이 바뀌어서 앞에 100을 붙이기로 함. => 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students] # i에다가 100을 더한값을 넣어라. 이 i는 students 리스트에 있는 값이다.
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(str) for str in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [str.upper() for str in students]
print(students)