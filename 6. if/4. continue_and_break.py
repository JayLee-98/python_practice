absent = [2, 5] # 결석한 학생 번호
no_book = [7] # 책을 깜빡하고 안가져옴
for student in range(1, 11): # 1번부터 10번까지의 학생이 있음
    if student in absent: 
        continue # 스킵하라는 말임.
    elif student in no_book:
        print("{0}번, 너 책이 없다고? 오늘 수업은 여기까지. {0}번, 너는 교무실로 따라와.".format(student))
        break
    print("{0}번아, 책을 읽어봐.".format(student))