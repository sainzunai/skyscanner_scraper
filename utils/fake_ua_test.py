# Codigo para comprobar el correcto funcionamiento del User Agent (UA) escogido.

from selenium import webdriver
from fake_useragent import UserAgent
import os
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Codigo compaatible con Windows y Linux
useragent = UserAgent()
user_agent = 'Mozilla/5.0 (Linux; ; )AppleWebKit/ (KHTML, like Gecko) Chrome/Mobile Safari/'#'Opera/9.61 (X11; Linux i686; U; ru) Presto/2.1.1' --> este user agent no sirve para cualquier URL
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)#useragent.random --> se pueden generar user agents que no son compatibles con la web

# Windows: configurar geckodriver
firefox_driver = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
firefox_service = Service(firefox_driver)
driver = webdriver.Firefox(firefox_profile=profile, service=firefox_service)

# Linux: configurara geckodriver
#driver = webdriver.Firefox(firefox_profile=profile)

# Generico:
driver.get("http://www.whatsmyua.info/")
driver.get("https://www.skyscanner.es/transport/flights/bio/ibz/230222/230225/config/9925-2302221530--31685-0-12404-2302221655|12404-2302251935--31685-1-9925-2302252300?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=1")




# firefox_options = Options()
# firefox_options.set_preference("browser.privatebrowsing.autostart")

# Codigo original:
# useragent = UserAgent()
# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override", useragent.random)
# driver = webdriver.Firefox(firefox_profile=profile)
