import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver

##
from pyvirtualdisplay import Display 
display = Display(visible=0, size=(1920, 1080))
display.start() 

# path='./chromedriver'
# driver = webdriver.Chrome(path)
# ##

# # driver = webdriver.Chrome("chromedriver")
# driver = webdriver.Chrome(path)##
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "./chromedriver"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver')
driver.get('http://google.com/')


def insta_searching(hashtag):
    url = "https://www.instagram.com/explore/tags/" + hashtag
    return url

#첫게시물을 여는 함수를 정의합니다
def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(3)

# 내용을 가져오는 함수를 정의합니다.
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
        content = ' '
    # 정규표현식을 활용하여 해시태그를 가져옵니다.
    tags = re.findall(r'#[^\s#,\\]+', content)
    # 작성일자를 가져옵니다.
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # 좋아요 수를 가져옵니다.
    try:
        like = soup.select('div.Nm9Fw > button')[0].text[4:-1]
    except:
        like = 0
    # 위치정보를 가져옵니다.
    try:
        place = soup.select('div.M30cS')[0].text
    except:
        place = ''
    # 수집한 정보를 리스트로 저장합니다.
    data = [content, date, like, place, tags]
    return data

    right = driver.find_element_by_css_selector('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

def move_next(driver):
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)