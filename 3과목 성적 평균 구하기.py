def ok(ko, math, en,count):
    calc = ko+math+en
    mean = calc /3
    result = round(mean,1)

    print(" ")
    print("************************")
    print("# 입력과목 성적")
    print(" ")
    print(" - 국어 성적 : ", ko)
    print(" - 수학 성적 : ", math)
    print(" - 영어 성적 : ", en)
    print("************************")
    print(" ")

    print("************************")
    print("# 결과")
    print(" - 총점 : ", calc)
    print(" - 평균 : ", result)
    print("************************")


def no(ko, math, en):
    print(" ")
    print("************************")
    print("# 입력과목 성적")
    print(" ")
    print(" - 국어 성적 : ", ko)
    print(" - 수학 성적 : ", math)
    print(" - 영어 성적 : ", en)
    print("************************")
    print(" ")
    print("# 입력 점수 오류 --> 확인 후 재입력")


while True:
    try:
        ko = input("국어 성적을 입력하세요 : ")
        math = input("수학 성적을 입력하세요 : ")
        en = input("영어 성적을 입력하세요 : ")
        result_ko = int(ko)
        result_math = int(math)
        result_en = int(en)
    

        if(0 < result_ko <=100) and ( 0< result_math <=100) and (0< result_en <=100) :
          ok(result_zork,result_math, result_en)
          break

        else: # 범위 밖의 경우 오류 출력
            no(ko, math, en)
            
    except ValueError: #문자가 입력된 경우 오류 출력
        no(ko, math, en)
