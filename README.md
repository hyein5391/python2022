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


