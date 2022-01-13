# pass로 들어가는 학점도 반영하기 (추가학기)

while 1:
    a = int(input('go? : 0.no 1.yes \n'))
    if a == 0:
        break
    else :
        all_credit = int(input("총 이수학점을 말해봐:")) #163
        score = float(input("졸업평점을 말해봐:")) #3.34
        p = int(input("pass 학점을 말해봐")) #28
        real =  all_credit - p
        x = all_credit * score
        y = real * score
        new = int(input("추가신청 학점:"))
        new_pass = float(input("학기 pass 강의 학점:"))
        new_score = float(input("학기 평점:"))
        y = real*score + new_score*(new-new_pass)
        score = y/(real+new-new_pass)
        print("최종 졸업평점은:",score)






