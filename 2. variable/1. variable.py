# '애완동물1'을 소개해주세요.

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# '애완동물2'를 소개해주세요.

animal = "고양이"
name = "깜깜이"
age = 10
hobby = "늦잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요.")
hobby = "공놀이" 
# 변수를 중간에서 선언할 수도 있음. 뒤에 선언한 변수로 변경됨.
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name,"는 " ,age, "살이며,", hobby, "을 아주 좋아해요.")
# +가 아니라 쉼표로 표현할 수도 있음. 이경우 문자열이 아닌 자료형을 형변환하지 않아도 됨.
# 쉼표를 사용하면 쉼표 앞에 띄워쓰기한것 처럼 공란이 들어간다.
print(name + "는 어른일까요? " + str(is_adult))