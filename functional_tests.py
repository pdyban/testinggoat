from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://192.168.0.106:8000')

assert 'Django' in browser.title
