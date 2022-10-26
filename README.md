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
------------------------------------------------------------------------------------------------------------------------------------


8월 31일

# URL 관련 : 아래의 예시와 같은 URL에서 web site 명을 추출하고 콘텐츠 명을 제출 하세요[크롤링 함수를 사용하여]
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=smilecat007&logNo=220860851649



url = "https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=smilecat007&logNo=220860851649"
url = '문자코드 value : 50 : 문자 :[2]'
def crawling(s) :      #함수의 가장 큰 역활은 #url 을 문자열로 받아서 구문분석을 통해 Site 명을 추출하여 반환 한다
                        #https <--- s가 붙을 경우는 디도스 공격을 쉽게 못하게 하기위해 인증을 해야만 할수있게 인증서로 방어하는 기능
    x = s.split('/')   #def 을 인식하며 들여쓰기한 부분의 전체적인걸 지나 크롤링이란 변수명으로 불러옴 url을
    print(x)           #http <--- P 프로토콜의 약자
    return x[2]

s1 = crawling(url)
print(f'URL : {url}')
print(f'Site 이름 : {s1}')

#↑↑↑ url 주소만 빼오기

#------------------------------------------------------------------------------------------
url = '문자코드 value : 50 : 문자 :[2]'
def crawling(s) : 
    if s.find('://') == -1:     # //가 없다면 -1 오류를 내며 return에서 No site 출력하여 돌아감
        return 'No Site'        #입력 문자열이 url 이 아니라면 ' No Site' 반환 하여 준다
    x = s.split('/')            #'/' 를 구문 하여 분해 한다 /를 기준으로 좌우 분해
    #print(x)        
    return x[2]

s1 = crawling(url)
print(f'URL : {url}')
print(f'Site 이름 : {s1}')

#↑↑↑ 비정상 적인 사이트를 추출하여 No Site 라는 문자열을 가져온다

#-------------------------------------------------------------------------------------------
url = "https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=smilecat007&logNo=220860851649"
def crawling(s) : 
    if s.find('://') == -1:     # //가 없다면 -1 오류를 내며 return에서 No site 출력하여 돌아감
        return 'No Site'        #입력 문자열이 url 이 아니라면 ' No Site' 반환 하여 준다
    x = s.split('/')            #'/' 를 구문 하여 분해 한다 /를 기준으로 좌우 분해
    #print(x)        
    return x[2]

s1 = crawling(url)
print(f'URL : {url}')
print(f'Site 이름 : {s1}')

#↑↑↑ 정상 적인 사이트를 추출 하여 원하던 문자열인 m.blog.naver.com 을 가져온다

#-------------------------------------------------------------------------------------------

문자열 [] <===== 인덱싱은 단일 계체로 자르고
      [몇에서부터:몇번째 까지] <----- 슬라이싱 의 경우 지정하여 잘라줄수있다
      + 로 문자열을 합칠수도 있다
      
★★★ find 함수는 문자열에서 특정 문자를 탐색을 한다
★★★ strip 함수를 이용하여 공백을 제거 한다

#--------------------------------------------------------------------------------------------
문제 예시
#예시
#아래의 예시와 같은 문자열에서 '/'로 구분된 각각의 옵션을 표시하고
#특히 PZ 옵션의 값을 x,y,w,h로 구분하여 표기하세요,단 , 최종 출력물은 다음과 같이 표기해 주세요.
#옵션의 순서는 변경 가능합니다 PZ 먼저 나올수도 있다

#결과물
#PS = 121
#PZ.x = 2
#PZ.h = 100
#FILE = test.py

#↓ 교수님 zip                                  #\ <-----이스케이프 시퀀스 특수문자 \\r 는<-----CR 이라고 부른다

str = "/PS:121 /PZ:2,3,100,100 /FILE=test.py" # \\n[줄바꿈] 는 문자열에서 특수기호를 나타낼때 많이 쓰인다
                                              # FILE :콜론 대신 =이퀄을 사용하여 구성해보았
def get_PS(s) : # /PS 옵션을 인수로 받아서 옵션의 값을 리턴 한다, s=/PS:121
    x = s.split(':') # (/PS 값이 담기고 : 121 이 담긴다)
    return(x[1]]

def get_PZ(s) : # /PZ 옵션을 인수로 받아서 옵션의 값을 x,y,w,h 리스트 값을 받아서 리턴한다, s=/PZ:2,3,100,100
    x = s.split(':')
    y = x[1].split(',') # 결과값  y = ['2', '3', '100', '100'] 
    return(y)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
↓ 글자 빼오기

#아래의 예시와 같은 문자열에서 '/'로 구분된 각각의 옵션을 표시하고,
#특히 PZ옵션의 값을 x,y,w,h,로 구분하여 표기하세요.
#옵션의 순서는 변경 가능합니다.
#단, 최종 출력물은 다음과 같이 해주세요.
# PS = 121
# PZ.x = 2 ...
# PZ.h = 100
# FILE = test.py



st0 = '/PS:121 /PZ:2,3,100,100 /FILE=c:\\test.py'
st1 = '/PZ:2,3,100,100 /PS:121 /FILE=c:\\test.py'
st2 = '/FILE=c:\\test.py /PS:121 /PZ:2,3,100,100'

def get_PS(s):                   #PS 옵션을 인수로 받아서 옵션의 값을 리턴 s=/PS:121
    x = s.split(':')
    return(x[1])
def get_PZ(s):                   #/PZ 옵션을 인수로 받아서 옵션으 ㅣ값을
    x = s.split(':')            # x,y,w,h,리스트로 리턴, s=/PZ 2,3,10,100
    y = x[1].split(',')
    return(y)                   # y = ['2', '3', '100', '100' ]
#--------------------------------------------------------------------------------------------
def get_FILE(s) :            # /FILE 윱션을 인수로 받아서 옵션의 값을 리턴. 단, 구분자는'='
    x = s.split('=')
    return(x[1])


def Main() : # 옵션 해석 프로그램 메인 루틴
    s = st0.split('/')
    a = get_PS(s[1])
    print(f"  PS:  {a}")              #f 포멧
Main()


t = [ 1, 2, 3, 4, 5,6, 7, 8, 9] 유한 리스트
배열을 정할때는 append 함수를 자주 사용하여 주어야 한다

이니셜 라이즈 <--- 초기화 함수

>>> some = [1,2,3,4,5,6,7]
>>> 9 in some 이라 할때 리스트 안에 지정한 숫자가 들어가 있지 않을때 T or F 로 나타낸다

자주 사용 하는 함수 언어
insert() 데이터를 중간에 끼워넣고 싶을때 사용
len() 리스트 내 원소 갯수 크기 반환
type(), int(),str(),sum(),max(),min()
round() 소수점 반올림을 몇자리까지 해줄것인가 정할수있음
abs() 절대값
sorted() 크기순으로 정렬
range() 0부터 시작하여 1씩 늘어남 ( 어디부터  , 어디어디까지  , 2(2씩 늘어남))
#--------------------------------------------------------------------------------------------
sort : 정렬
swap : 서로 바꾸어줌 [솔트과 스왑을 구현하시오] 함수를 사용하지말고 





#-----------------------------------------------------------------------------------------------
9월6일

#입력 한 함수를 평균값 

total = 0
count = 0
while True :
    inp = input('Enter a number :')
    if inp == 'done' : break #한개의 명령어는 한줄로 작성이 가능하다
    value = float(inp)
    total = total +  value
    count = count + 1
average = total / count
print('average:', average)
#-------------------------------------------------------------------------------------------------
numlist = list()
while True :
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)


--------------------------------------------------------------------------------------------------
t = [ 1, 2, 3, 4, 5,6, 7, 8, 9] 유한 리스트
배열을 정할때는 append 함수를 자주 사용하여 주어야 한다

이니셜 라이즈 <--- 초기화 함수

>>> some = [1,2,3,4,5,6,7]
>>> 9 in some 이라 할때 리스트 안에 지정한 숫자가 들어가 있지 않을때 T or F 로 나타낸다

자주 사용 하는 함수 언어
insert() 데이터를 중간에 끼워넣고 싶을때 사용
len() 리스트 내 원소 갯수 크기 반환
type(), int(),str(),sum(),max(),min()
round() 소수점 반올림을 몇자리까지 해줄것인가 정할수있음
abs() 절대값
sorted() 크기순으로 정렬
range() 0부터 시작하여 1씩 늘어남 ( 어디부터  , 어디어디까지  , 2(2씩 늘어남))
#--------------------------------------------------------------------------------------------
sort : 정렬
swap : 서로 바꾸어줌 [솔트과 스왑을 구현하시오] 함수를 사용하지말고 
-------------------------------------------------------------------------------------------------
자주 사용하는 함수는 중간중간 계속 기입하는중
d = dick 딕셔너리 (key / val) 키와 벨류 튜플과는 다르게 sort[배열변경]순차적으로 변경 하여 준다[가능하다]
#딕셔너리 사용하기에 좋은 것은 아니다
리스트 와 딕셔너리
리스트는 순서를 유지하는 값들의 선형 컬렉션
딕셔너리는 고유의 라벨을 갖고 있는 값을 넣는 "가방"

딕셔너리
리스트는 리스트 안에서 원소의 위치를 기반으로 인덱스를 매김

딕셔너리는 가방과 같음 순서가 없음
따라서 딕셔너리에 넣는 대산은 조회 태그를 달아 인덱스를 매김
중괄호로 리스트처럼 만들면 그게 딕셔너리
##딕셔너리 예제
putse = dict()
putse['money'] = 12
putse['candy'] = 3
putse['tissues'] = 75
print(purse)

print(purse['candy']




입력, 중간 작업 , 출력
# 텍스트 예제를 이용 하여 단어별로 같은 단어가 몇개가 있는지 개수를 측정하는 프로그램을 만드시오


sDict = {}
def MakeDict(slist):                  #문자열 리스트 slist를 받아서 Dictionary를 구성하는 함수
                                           #slist = ["길동", "길순", "길영", "길민", "길순", "길영"]
                                           #dic = {"길동":1, "길순": 2, "길영": 2, "길민":1}
    for n in slist :
       sDict[n] = sDict.get(n, 0) + 1
def Main() :
    str = "Writing programs (or programming) is a very creative and rewarding activity You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills. We are surrounded in our daily lives with computers ranging from laptops to cell phones. We can think of these computers as our “personal assistants” who can take care of many things on our behalf The hardware in our current-day computers is essentially built to continuously ask us the question, “What would you like me to do next? Our computers are fast and have vast amounts of memory and could be very helpful to us if we only knew the language to speak to explain to the computer what we would like it to do next. If we knew this language we could tell the computer to do tasks on our behalf that were repetitive Interestingly, the kinds of things computers can do best are often the kinds of things that we humans find boring and mind-numbing"
    s1 = str.split(" ") 
    MakeDict(s1)
    print(sDict)
    
Main()


            
            
            
https://kingofbackend.tistory.com/92


#계산기 프로그래머 
HEX : 16진수
DEC : 10진수
OCT : 8진수
BIN : 2진수   #127 입력시 1한개당 비트 라고 이야기 한
아스키 코드는 특수 문자 + 영 숫 해서 0~127개 까지 있고 7bit 체제이다 bit단위는 2진수 를 타나낸다



#=========================================================================================================
아스키 코드를 파이썬으로 만들기

나의 현 해답은  무식함으로 일단 만들기
for문으로 돌려 놓아보자

import pandas as  pd
def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0,col_num):
        col.append(fill)
    for i in range(0,ind_num):
        ind.append(fill)
    for i in range(0,ind_num):
        con.append(col)
    return pd.DataFrame(con, columns=col, index=ind)
df = df_maker(11,32,0)
col = ["16진a","문자a","10진a","16진b","문자b","10진b","16진c","문자c","10진c","16진d","문자d"]
ind = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
df.columns = col
df.index = ind
df["16진a"] = [hex(0),hex(1),hex(2),hex(3),hex(4),hex(5),hex(6),hex(7),hex(8),hex(9),hex(10),hex(11),hex(12),hex(13),hex(14),hex(15),hex(16),hex(17),hex(18),hex(19),hex(20),hex(21),hex(22),hex(23),hex(24),hex(25),hex(26),hex(27),hex(28),hex(29),hex(30),hex(31)]
df["10진a"] = [32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
df["16진b"] = [hex(32),hex(33),hex(34),hex(35),hex(36),hex(37),hex(38),hex(39),hex(40),hex(41),hex(42),hex(43),hex(44),hex(45),hex(46),hex(47),hex(48),hex(49),hex(50),hex(51),hex(52),hex(53),hex(54),hex(55),hex(56),hex(57),hex(58),hex(59),hex(60),hex(61),hex(62),hex(63)]
df["문자b"] = [chr(32),chr(33),chr(34),chr(35),chr(36),chr(37),chr(38),chr(39),chr(40),chr(41),chr(42),chr(43),chr(44),chr(45),chr(46),chr(47),chr(48),chr(49),chr(50),chr(51),chr(52),chr(53),chr(54),chr(55),chr(56),chr(57),chr(58),chr(59),chr(60),chr(61),chr(62),chr(63)]
df["10진b"] = [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95]
df["16진c"] = [hex(64),hex(65),hex(66),hex(67),hex(68),hex(69),hex(70),hex(71),hex(72),hex(73),hex(74),hex(75),hex(76),hex(77),hex(78),hex(79),hex(80),hex(81),hex(82),hex(83),hex(84),hex(85),hex(86),hex(87),hex(88),hex(89),hex(90),hex(91),hex(92),hex(93),hex(94),hex(95)]
df["문자c"] = [chr(64),chr(65),chr(66),chr(67),chr(68),chr(69),chr(70),chr(71),chr(72),chr(73),chr(74),chr(75),chr(76),chr(77),chr(78),chr(79),chr(80),chr(81),chr(82),chr(83),chr(84),chr(85),chr(86),chr(87),chr(88),chr(89),chr(90),chr(91),chr(92),chr(93),chr(94),chr(95)]
df["10진c"] = [96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
df["16진d"] = [hex(96),hex(97),hex(98),hex(99),hex(100),hex(101),hex(102),hex(103),hex(104),hex(105),hex(106),hex(107),hex(108),hex(109),hex(110),hex(111),hex(112),hex(113),hex(114),hex(115),hex(116),hex(117),hex(118),hex(119),hex(120),hex(121),hex(122),hex(123),hex(124),hex(125),hex(126),hex(127)]
df["문자d"] = [chr(96),chr(97),chr(98),chr(99),chr(100),chr(101),chr(102),chr(103),chr(104),chr(105),chr(106),chr(107),chr(108),chr(109),chr(110),chr(111),chr(112),chr(113),chr(114),chr(115),chr(116),chr(117),chr(118),chr(119),chr(120),chr(121),chr(122),chr(123),chr(124),chr(125),chr(126),chr(127)]
df




#============================================================================================================================================================
DB Browser(SQlite)


CREATE TABLE "UserData" (
	"CODE" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"NAME" TEXT NOT NULL,
	"BUY" TEXT
	)

ALTER TABLE UserData add "PAID" INTEGER;
ALTER TABLE UserData add "ADDRESS" TEXT;

ALTER TABLE UserData DROP "ADDRESS";

INSERT INTO UserData(NAME, PAID) VALUES ("K", 503300);
INSERT INTO UserData(NAME, BUY, PAID) VALUES ("A", "NS", 353300);
INSERT INTO UserData(NAME, PAID) VALUES ("B", 1500000);
INSERT INTO UserData(NAME, PAID) VALUES ("C", 703000);
INSERT INTO UserData(NAME, PAID) VALUES ("D", 900000);
INSERT INTO UserData(NAME, BUY) VALUES ("N", "LP Player");

UPDATE UserData SET BUY = "Laptop" WHERE name = "K";
UPDATE UserData SET CODE = 2 WHERE name = "N";
UPDATE UserData SET BUY = "iPhone14" WHERE name = "B";
UPDATE UserData SET BUY = "MicroWave" WHERE name = "C";
UPDATE UserData SET BUY = "SmartTV" WHERE name = "D";
UPDATE UserData SET PAID = 370000 WHERE BUY = "LP Player";

DELETE FROM UserData WHERE ROWID = 2;

SELECT * FROM UserData ORDER by PAID DESC;

INSERT INTO ProData(ProductName, Price) VALUES ("Laptop", 500000);
INSERT INTO ProData(ProductName, Price) VALUES ("NS", 350000);
INSERT INTO ProData(ProductName, Price) VALUES ("iPhone14", 1500000);
INSERT INTO ProData(ProductName, Price) VALUES ("MicroWave", 700000);
INSERT INTO ProData(ProductName, Price) VALUES ("LP Player", 370000);
INSERT INTO ProData(ProductName, Price) VALUES ("SmartTV", 900000);

SELECT * FROM UserData JOIN ProData;
SELECT CODE, name, ProData.ProductName, PAID FROM UserData JOIN ProData on ProData.ProductName = UserData.BUY;

INSERT INTO ProData(ProductName, Price) VALUES ("ABC", 370000);
INSERT INTO ProData(ProductName, Price) VALUES ("BCDE", 900000);

DELETE FROM ProData WHERE ProductName like "%B%";









