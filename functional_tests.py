from selenium import webdriver

br = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
br.get('http://localhost:8000')

assert 'install' in br.title