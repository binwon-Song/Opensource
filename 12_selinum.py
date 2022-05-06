from selenium import webdriver


browser=webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
browser.get('http://naver.com')

# 로그인 버튼 클릭

elem=browser.find_element_by_class_name('link_login')
elem.click()

browser.find_element_by_id('id').send_keys('qlsndjs236')
browser.find_element_by_id('pw').send_keys('binwon3158')

browser.find_element_by_id('log.login').click()