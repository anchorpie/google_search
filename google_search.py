from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

link = 'https://www.google.com'
browser.get(link)
