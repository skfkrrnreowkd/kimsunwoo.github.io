import requests
from bs4 import BeautifulSoup

# 스크래핑할 웹 페이지 URL
url = "https://news.naver.com/"

# 웹 페이지 HTML 코드 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 헤드라인 뉴스 정보 수집
headlines = soup.select('.hdline_article_tit > a')

# 헤드라인 뉴스 제목과 내용 출력
for headline in headlines:
    title = headline.get_text().strip()
    link = headline['href']
    print("제목:", title)
    print("링크:", link)
    print()
