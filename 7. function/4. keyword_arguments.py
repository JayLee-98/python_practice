def profile(name, age, main_lang):
    print(name, age, main_lang)
    
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
# 호출시에 순서를 무시하고 입력해도 함수에 정의되어있는 인자대로 출력됨.