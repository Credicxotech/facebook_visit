from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pickle

HEADLESS = True 
PROXY = "178.62.232.131:24000"

def get_browser():
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path= r"./chromedriver.exe" ,options=chrome_options)
    return browser

if __name__=='__main__':
    browser = get_browser()
    try:
        browser.get("htps://www.facebook.com")
        print("visit successful.....")
    except:
        print("visit failed......")    




# if __name__ == '__main__':
#     browser = get_browser()
#     browser.get('https://www.facebook.com/')
#     sleep(2)
#     with open("fb_cookies.pkl", 'rb') as cookiesfile:
#         cookies = pickle.load(cookiesfile)
#     for cookie in cookies:
#         browser.add_cookie(cookie)  
#     # browser.find_element_by_xpath('//*[@data-testid="royal_email"]').send_keys('SassonLiebermann987@protonmail.com')
#     try:
#         browser.find_element_by_xpath('//*[@data-testid="royal_login_button"]').click()
#         print("Log in Sucessful........")
#     except:
#         print("Login failed.......")    
