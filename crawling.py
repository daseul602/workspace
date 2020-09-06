from selenium import webdriver

driver = webdriver.Chrome('C:/Users/다슬/Downloads/chromedriver')

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('ensl0402')
driver.find_element_by_name('pw').send_keys('password11')

driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.implicitly_wait(3)
#sleep

driver.save_screenshot("sucess!.png")
#capture

driver.close()