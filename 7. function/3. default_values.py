def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2} \
        ".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업일 경우, 이름만 다르고 나이와 언어는 동일함.
# 이럴때 '기본 값'을 사용할 수 있음.

def profile(name, age=17, main_lang="파이썬"): # 따로 인자로 전달받지 않을 경우 기본값이 세팅됨.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2} \
        ".format(name, age, main_lang))
    
profile("유재석")    
profile("김태호")

