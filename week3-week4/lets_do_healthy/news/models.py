from django.db import models

import time
import pandas as pd  # pandas는 dataframe을 주고 다루기 위한 라이브러리이다.

from selenium import webdriver
from bs4 import BeautifulSoup as bs


class News:

    def getList(main):
        input_select = 'div.newsflash_body > ul.type06_headline' if main == 1 else 'div.newsflash_body > ul.type06'

        driver = webdriver.Chrome('../chromedriver')  # 웹드라이버 실행 경로 지정, chromedriver는 폴더가 아니라 파일명
        driver.get('https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=241')
        time.sleep(1)  # 1초간의 동작 확인

        html = driver.page_source  # 연결한 웹사이트의 소스 가져오기
        soup = bs(html, 'html.parser')  # BeautifulSoup 객체 생성

        newsList = soup.select(input_select)

        driver.quit()  # 실행 후엔 웹드라이버 종료

        return newsList

    def getMainList():
        return getList(1)

    def getSubList():
        return getList(0)
