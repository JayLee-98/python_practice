# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
    
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift")

# 그런데 유재석의 언어가 하나가 더 늘어난다면, 함수 자체를 변경해야하는 상황이 생김.
# 이때 가변인자를 활용할 수 있음.

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift")