from selenium import webdriver

browser = webdriver.Firefox(executable_path='E:\FIREFOX\geckodriver')

browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close()