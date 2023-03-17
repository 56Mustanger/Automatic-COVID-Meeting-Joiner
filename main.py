from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

username = ("353877764@educ.dpcdsb.org")
password = ("Mustanger56")

options=Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/Users/indumathy/Desktop/Devesh/Webdriver/chromedriver",chrome_options=options)

driver.get("https://classroom.google.com/u/1/c/MTk5MjQ3Mzk1OTk5")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element_by_name("identifier").send_keys(username)
driver.find_element_by_css_selector(".VfPpkd-LgbsSe").click()


driver.find_element_by_name("UserName").send_keys(username)
driver.find_element_by_name("Password").send_keys(password)
driver.find_element_by_id("submitButton").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id=\"view_container\"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
driver.implicitly_wait(3)
driver.find_element_by_css_selector(".Y5sE8d .l4V7wb, .YhQJj .l4V7wb, .An19kf .l4V7wb").click()
time.sleep(20)
