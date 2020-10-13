import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')  # 웹드라이버 실행 경로 지정, chromedriver는 폴더가 아니라 파일명
driver.get('https://www.google.co.kr/')

time.sleep(2)  # 2초간의 동작 확인
search_box = driver.find_element_by_name('q')  # element name이 q인 곳을 찾아서
search_box.send_keys('ChromeDriver')  # 키워드 입력
search_box.submit()  # 실행
time.sleep(2)  # 2초간의 동작 확인
driver.quit()  # 실행 후엔 웹드라이버 종료