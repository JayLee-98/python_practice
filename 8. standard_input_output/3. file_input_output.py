# score_file = open("score.txt", "w", encoding="utf8") # 인자로는 파일이름, w는 쓰기위한 목적임을 명시, 인코딩으로 utf8을 명시해줘야 한국어 파일이 안깨짐.
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # 두번째 인자로 a를 쓰면 append로 엎어쓰기가 가능함.
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 한번에 모두 읽어오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()