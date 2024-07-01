# 리스트보다 빠른게 장점
# 리스트와 다르게 내용 변경이나 추가할 수 없음.

menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 튜플에 새롭게 추가할 수 없음.

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)