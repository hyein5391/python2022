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
