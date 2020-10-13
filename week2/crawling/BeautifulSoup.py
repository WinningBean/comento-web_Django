import requests
from bs4 import BeautifulSoup as bs

url = "https://www.daum.net/"
html_text = requests.get(url).text

soup_obj = bs(html_text, "html.parser")  # BeautifulSoup 객체 생성
# 첫번째 인자는 str 형식, html이나 xml로 작성된 문자열이어야 한다.
# 보통 requests나 urllib로 가져온 웹페이지 정보에 .text를 붙여서 넣어준다.
# 두번째 인자는 해석기(parser)를 넣어줘야 한다.

keywords = soup_obj.find_all('span', class_='txt_ranking')  # 데이터에서 태그와 클래스를 찾는 함수
keywords = [each_line.get_text().strip() for each_line in keywords]  # .get_text()를 이용하야 문자열만 추출, .strip()을 이용하여 양옆 공백제거

print(keywords)