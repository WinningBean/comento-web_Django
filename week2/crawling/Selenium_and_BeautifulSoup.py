import time
import pandas as pd  # pandas는 dataframe을 주고 다루기 위한 라이브러리이다.

from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('./chromedriver')  # 웹드라이버 실행 경로 지정, chromedriver는 폴더가 아니라 파일명
driver.get('https://oscar.go.com/winners')
time.sleep(1)  # 1초간의 동작 확인

html = driver.page_source  # 연결한 웹사이트의 소스 가져오기
soup = bs(html, 'html.parser')  # BeautifulSoup 객체 생성

category = soup.select('div.winners-list__info > a')  # BeautifulSoup 객체의 select()를 이용해 html 내에 필요한 부분 선택하기
movie = soup.select('div.winners-list__info > h3 > a')
content = soup.select('div.winners-list__info > p')

oscars_2020 = []
for item in zip(category, movie, content):  # zip()은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
    oscars_2020.append({'카테고리' : item[0].text, '영화' : item[1].text, '수상내역' : item[2].text})

data = pd.DataFrame(oscars_2020)  # pandas의 DataFrame()을 이용하여 DataFrame 객체를 생성한다.
print(data)
data.to_csv('oscars_2020.csv')  # pandas의 DataFrame.to_csv()를 이용하여 DataFrame을 csv 파일로 내보냅니다.

driver.quit()  # 실행 후엔 웹드라이버 종료