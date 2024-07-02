import pickle
# profile_file = open("profile.pickle", "wb") # wb에서 b는 바이너리를 의미하며, pickle을 사용할땐 항상 사용해야함.
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 그대로 가져와서 데이터 형태로 불러온다는 의미임.
                                    # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()