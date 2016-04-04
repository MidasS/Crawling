from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib
import http.client
import csv

# Http 1.1에서 에러가 나서 아래 코드로 설정을 바꿨습니다. 코드에 영향을 안미쳐서 신경안쓰셔도됩니다
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


#  전체 헤드라인 제목하고 내용 담을 변수를 설정
title =[]
content = []

# 첫 도메인 URL 할당
urlString = 'http://www.marketwatch.com/search?q=oil&m=Keyword&rpp=100&mp=806&bd=true&bd=false&bdv=02%2f9%2f2016&rs=true&o='
with urllib.request.urlopen(urlString) as url:
    s = url.read().decode('utf-8')

soup = BeautifulSoup(s)

# 페이지 소스보기에서 헤드라인 관련 div 클래스 설정
resultlist = soup.find_all("div","searchresult")


#  각헤드라인별로 URL 하이퍼링크 가져오기
def get_main_href():

    # 해당 a 태그안에서 하이퍼링크 내용만 뽑아서 루프 돌기
    main_href = [div.a.get('href') for div in resultlist]
    
    # 각 하이퍼링크를 리스트로 반환
    return main_href

#     각 헤드라인의 하이퍼링크를 변수로 받음
def get_sub_title_content(url2):

    # 첫 번수 선언 타입은 문자열
    title = ''
    content = ''
    
    # 각 헤드라인 뉴스안의 url 설정
    with urllib.request.urlopen(url2) as url:
        s2 = url.read().decode('utf-8')

    soup2 = BeautifulSoup(s2)
    
    ''' 페이지 소스보기에서 id 가 article-headline인 부분 찾기, 제목 할당
        [0] 이부분은 soup2.fin~~~~ 이부분의 아웃풋이 2중 배열이라 첫번쨰 인자를 가르키는 겁니다.
        이부분이 조금 까다로운데 descendants 는 해당 태그 안의 자식노드들을 generator 타입으로 반환합니다.
        그래서 그것을 리스트로 바꿔서 루프를 돌린겁니다.
        조금 어려우시겠지만 중간중간 Print 섞어서 코드 바꿔가면서 타입확인해보시면 이해되실꺼에요.
        try except는 try에서 시행하고 에러나면 except에서 실행하는데 공백제거를 안해도 되면 패스 시킵니다
    '''
    
    raw_title = list(soup2.find_all(id="article-headline")[0].descendants)
    for i in raw_title:
        try:
            # .string 은 해당 태그 안에 값만 가져옵니다, 그 후 공백제거
            title += i.string.strip()
        except:
            pass

    # 이번엔 내용에 해당되는 값찾고 위에 제목 이랑 똑같은 알고리즘
    raw_content = soup2.find_all(id="article-body")
    raw_content2 = list(raw_content[0].descendants)


    for i in raw_content2:
        try:
            content += i.string.strip()
        except:
            pass
    #  루프 도는거 확인하기 위한 출력
    print("Just finished Downloading %s"%title)

    # 반환값은 해당 기사의 제목과 내용을 반환함
    return title, content

# 해당 기사 번호 테스트할 때 아래코드 주석 풀어 해보면 됩니다
# print(get_sub_title_content(get_main_href()[6]))

# 총 메인 해드라인의 개수 만큼 루프를 도는데 각 세보 내용가져오는 곳에서 결과값으로 제목과 내용을 가져와서 전역 변수에 있는 title, content 리스트에 합쳐줌
for i in range(len(get_main_href())):
    get_title, get_content = get_sub_title_content(get_main_href()[i])
    title.append(get_title)
    content.append(get_content)

# 확인용 출력
print(title)
print(content)

#  혹시몰라 csv 로 저장하는 코드도 첨부해 놨습니다, 안쓰실때는 주석처리해서 위에 리스트 데이터만 사용하시면 될 꺼에요
csv_file = open('datatest.csv', 'w', encoding='UTF-8')
cw = csv.writer(csv_file , delimiter=',')

data = [title, content]

cw.writerows(data)


# 디테일하게 수정해야 하는부분이 계속 생깁니다. 불완전한 코드고 최대한 이해하실수 있도록 구조를 단순화 했습니다. 