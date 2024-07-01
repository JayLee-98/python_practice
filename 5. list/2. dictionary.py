cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 딕셔너리 리스트.get('key')을 통해 접근할 수도 있음.
print(cabinet.get(5)) # get()을 했을때 키값이 존재하지 않는 경우 None을 반환함.
print('hi')
# print(cabinet[5]) # 딕셔너리 리스트['키']를 통해 접근할때 키값이 존재하지 않는 경우 에러를 반환하며 실행 정지됨.

print(cabinet.get(5, "사용가능")) # 키값이 존재하지 않는경우, key값 옆에 None 대신 출력할 값을 작성할 수 있음.

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# values 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 영업종료
cabinet.clear()
print(cabinet)
