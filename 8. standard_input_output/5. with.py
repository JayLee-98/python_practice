import pickle

# with open("profile.pickle", "rb") as profile_file: # "profile.pickle" 파일을 "rb" 읽기로 열어서, profile_file이라는 변수에 값을 담은것임
#     print(pickle.load(profile_file))
# 별도로 .close()해줄 필요없이 with문이 종료되면서 파일이 닫힘.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
