python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # python 변수의 0번째 인덱스 위치의 문자가 isUpper가 맞는지 확인. boolean을 반환함.
print(len(python))
print(python.replace("Python", "Java")) # 첫번째 인자를 찾아서, 두번째 인자로 대체함.

index = python.index("n") # index라는 함수를 이용하여 python 변수안에 'n'에 해당하는 문자가 몇 번째 인덱스 위치에 존재하는지 확인함.
print(index) # 첫번째 n의 위치는 5번째 인덱스
index = python.index("n", index + 1) # 두번째 인자는 start를 인자로 받기때문에, line 8에 선언된 index()의 +1이 시작점이 됨.
print(index) # 두번째 n의 위치는 15번째 인덱스

print(python.find("n")) # find()함수는 index()와 비슷한 함수

print(python.find("Java")) # find() 함수는 python 변수안에서 "Java"가 없다면 -1을 반환하면서 정상 작동하지만,
# print(python.index("Java")) # index() 함수는 검색하려는 인자가 변수안에 없다면 에러를 반환하면서 작동 중지함.

print(python.count("n")) # 변수안에 인자로 검색한 문자의 갯수를 반환함.