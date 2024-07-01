# 자료구조의 변경
menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu)) # list

menu = tuple(menu)
print(menu, type(menu)) # tuple

menu = set(menu)
print(menu, type(menu)) # set