weather = "맑음"
# if 조건:
#     실행 명령문

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")
    
# weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")
    
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 실외 활동을 자제하세요.")
elif 10 <= temp and temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기는 것이 좋겠어요.")
else: 
    print("너무 추워요. 나가지 마세요.")