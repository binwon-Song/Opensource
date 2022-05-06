from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
browser=webdriver.Chrome()
browser.maximize_window()

url='https://m-flight.naver.com/'
browser.get(url)

browser.find_element_by_class_name('r').click()
browser.find_elements_by_link_text('27')[0].click()
browser.find_elements_by_link_text('28')[0].click()

#제주도 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[8]/div/ul/li[1]/button/figure/img").click()
try:
    elem=WebDriverWait(browser,10).until(EC.presence_of_element_located(By.XPATH,""))
    print(elem.text )
#로딩시간 처리
#10초동안 대기 xpath 가 가르키는 동작이 나올때까지 대기
finally:
    browser.quit()

# elem=browser.find_element_by_xpath('')
# print(elem.text )

