import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def inicializarBrowser():
    # intialzie chrome service
    #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    firefox_driver = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
    firefox_service = Service(firefox_driver)
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", user_agent)

    browser = webdriver.Firefox(service=firefox_service, options=firefox_options)


    
    return browser

browser = inicializarBrowser()
browser.get("https://whatsmyua.info")
