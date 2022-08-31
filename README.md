# python2022
koreaIT
2022-08-30 금일의 학습내용
    ● 깃허브를 이용하여 학습한 내용을 온라인상의 리파지토리(저장장소)에 업로드함
    ● len[내장함수] index[내장함수] Split[자주사용하는 용어] 
    ● Str내장 함수에는 upper[일괄적으로 대문자로 만들어주는 함수] lower[일괄적으로 대문자로 만들어주는 함수]
    
    
    ★ 루프와 개수 세기
    word = 'nanana'
    count = 0
    for letter in word :
      if letter == 'a':
        count = count +1
      print(count)
      
    ★ 문자열[슬라이싱]
    s = 'monty python'
    print(s[0:4]) #mont 4는 0보다 크고 x 4보다는 작다는 의미
    
    print(s[6:7]) #p
    
    print(s[:]) #생략을 하면 전부 나타난다
    # 문자열에서 <크고 > 작다는 의미는 알파벳 순이다 문자는 특수기호도 포함한다\
    null 은 문자로 서의 0을 의미함 [아스키코드]
    한글은 [코드 체계를 보면 완성형이지만 뜯어보면 조합형이 중간에 만들어 질수 있다]
    초성 중성 제성 [ 형식]
    ㄱ   모   ㄱ
    ㄴ
    ㄷ
    ㄹ
    
    
    a = input('다시 시작 하시겠습니까?(Y/N) : ')   #upper [대분자로 바꾸어줌]
                                                 #lower [소문자로 바꾸어줌]
#대문자로 변경
greet = 'hello bob'
nnn = greet.upper()
print(nnn)

#소문자로 변경
greet = 'hello bob'
nnn = greet.lower()
print(nnn)


str.strip <---- 띄워져있는 문자열을 제거 해주는 기능


find() 함수를 이용해서 하위 문자열을 다른 문자열에서 탐색가능

find() 하위 문자열의 첫번째로 나타나는 위치를 검색
하위 문자열을 찾지 못하면 , find()는 -1을 반환 한다

REPLACE 함수는 특정 언어를 찾아서 교체 해주는 언어

#파싱과 추출

def func(s) : #s : ' gooD moring' ==> 'Good Morning'
    str = s.split(' ') # split : 구분자로 구분된 문자열 배열을 되돌려 준다
    print(str)
    ret =''
    for s1 in str :
        ss1 = s1.lower()
        ss2 = ss1[0].upper() + ss1[1:]
        ret = ret + ' '+ ss2
    return ret
print(ret)
x = input('영어 문장을 입력하세요 : ')
func(x)

내장함수 자주 사용하는것
type(),float() int() print(),input(),len()<=문자열의 길이를 알수있다

#아스키 코드 0~31 => 제어코드 32~127 부터는 문자 32는 스페이스<---

#  %(자리수를 넣을수있다) d : 10진정수
     f(lot) : 실수(소수)
     s(tring) : 문자열
     c(캐릭터) : 문자(단일문자)
     x() :16진수로 출력가능

# 아스키 코드 불러 오기 예제
x = 80
s = f'문자코드 value : {x} : 문자 : [{"%c"%x}]'
s
결과 값 : '문자코드 value : 80 : 문자 : [P]'

# find 함수 존재 하는 문자열을 찾아주는 함수 없을 경우 -1로 표기
# str.lower , upper, strip 스트립 함수 lstrip 과 rstrip 두가지 [lstrip <--- 왼쪽 공백 rstrip <-----오른쪽 공백만들때 사용]


