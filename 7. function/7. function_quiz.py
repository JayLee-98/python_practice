# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#     남자: 키(m) * 키(m) * 22
#     여자: 키(m) * 키(m) * 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#         * 함수명: std_weight
#         * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘재자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

# 오답
# gender = print(input("성별을 입력해주세요. 남자 or 여자"))
# height = print(input("키를 입력해주세요."))
# print("입력하신 성별은 {0}이고, 키는 {1}cm입니다.".format(gender, height))

gender = input("성별을 입력해주세요. 남자 or 여자: ")
height = int(input("키를 입력해주세요: "))
print("입력하신 성별은 {0}이고, 키는 {1}cm입니다.".format(gender, height))

def std_weight(height, gender):
    height = height / 100  # cm를 m로 변환 # 오답 수정
    if "남자" in gender:
        result = pow(height,2) * 22
        """result = result[:3]
        result = result[:2]+ "+" + result[5:]
        print(result) """
        result = round(result, 2)  # 소수점 두 자리까지 반올림 # 오답 수정
        height = height * 100
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,result))

    else:
        result = pow(height, 2) * 21
        """ result = result[:3]
        result = result[:2]+ "+" + result[5:]
        print(result) """
        result = round(result, 2)  # 소수점 두 자리까지 반올림 # 오답수정
        height = height * 100
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height,result))
        
std_weight(height, gender)