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






# cnt = 0
# jae = 0
# while 1:
#     retaking = input("재수강 해볼텨? 0.아니 1.응")
#     cnt+=1
#
#     if retaking == '0':
#        cnt= cnt-1
#        passmain2.py
#
#
#     elif retaking == '1':
#         re_credit = int(input("그 과목 몇 학점짜리임:"))
#         if re_credit>0 :
#             last_score = float(input("기존점수 말해봐(ex-2.0):"))
#             re_score = float(input("예상점수 말해봐(ex-4.0):"))
#             updated_score = ((all_credit * score+(re_score-last_score) * re_credit) / all_credit)
#             print("* 재수강 후 졸업평점:", round(updated_score, 3), "\n* 이수학점:", all_credit)
#             new_score = updated_score
#             jae += re_credit
#         else:
#             cnt = cnt - 1
#             repeat = cnt
#             updated_score = new_score
#             print("재수강 과목", repeat, "개", jae, "학점")
#             print("* 최종 졸업평점:", round(updated_score, 3), "\n* 총 이수학점:", new_credit)
#             break
#
#
#     else:
#         print('잘못눌렀어 임마')
#         cnt=cnt-1
#
#
#         continue
#
#     add_credit = int(input("그럼 앞으로 몇 학점 들을겨:"))
#     if (cnt==0 and add_credit<0):
#
#      break
#
#     else:
#         if add_credit>0 :
#             if cnt>0:
#                 possible_score = float(input("예상 학기 평점은:"))
#                 new_credit = all_credit+add_credit
#                 new_score = ((all_credit*new_score)+(add_credit*possible_score))/(all_credit+add_credit)
#                 print("이수학점:",new_credit,"\n졸업평점:",round(new_score,3))
#                 all_credit = new_credit
#                 old_score = score
#                 score = new_score
#             else:
#                 possible_score = float(input("예상 학기 평점은:"))
#                 old_score = score
#                 all_credit = all_credit+add_credit
#                 score = ((all_credit * score) + (add_credit * possible_score)) / (all_credit + add_credit)
#                 print("* 재수강",cnt,"개","\n* 추가 이수학점:",add_credit,"학점")
#                 print("* 최종 졸업평점:", round(score, 3),"\n* 졸업평점 상승:",score- old_score,"\n* 총 이수학점:", all_credit)
#                 print(old_score)
#                 print(score)
#
#         else :
#             new_credit = all_credit
#             repeat = cnt
#             updated_score = new_score
#             print("재수강 과목", repeat, "개", jae, "학점")
#             print("* 최종 졸업평점:", round(updated_score, 3),"\n* 졸업평점 상승:",updated_score-score, "\n* 총 이수학점:", new_credit)
#             break
#
#
