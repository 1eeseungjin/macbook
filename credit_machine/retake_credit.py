# pass로 들어가는 학점도 반영하기 (재수강)


while 1:
    a = int(input('go? : 0.no 1.yes \n'))
    if a == 0:
        break
    else :
        all_credit = int(input("총 이수 학점을 말해봐:")) #163
        score = float(input("졸업 평점을 말해봐:")) #3.34
        p = int(input("P/F 학점을 말해봐:")) #28
        real =  all_credit - p
        x = all_credit * score
        y = real * score
        re = int(input("재수강 할 학점:"))
        or_score = float(input("원래 성적:"))
        re_score = float(input("재수강 성적:"))
        rising = re*(re_score-or_score)
        y = y + rising
        print("바뀐 평점:",y/real)
        score = y/real
        cnt = 1
        ree = 0
        ree += re
        while 1:
            b = int(input('재수강? : 0.no 1.yes'))
            if b == 0:

                print("재수강 과목 수:",cnt,"재수강 학점:",ree)
                print("최종 평점:",round(score,3))
                break
            else:
                cnt+=1
                re = int(input("재수강 학점:"))
                ree +=re
                or_score = float(input("원래 성적:"))
                re_score = float(input("재수강 성적:"))
                rising = re * (re_score - or_score)
                y = y + rising
                print("바뀐 학점:", y / real)
                score = y / real
                continue
        break



