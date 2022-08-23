# %%

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up Splinter
path = ChromeDriverManager().install()
print(path)
# browser = webdriver.Chrome(service=Service(path))
# browser.get("https://google.com")
# browser.quit()
browser = Browser('chrome', executable_path=path)
browser.visit("http://quotes.toscrape.com/")
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)