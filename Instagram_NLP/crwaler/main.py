import searching
import DB
import time

email = 'Joo_10000___'   ### 사용할 계정 정보 입력
password = 'dnals950205' ### 비번 정보 수정
word = "연남동" #검색할 해시태그. 띄어쓰기를 사용하면 안됩니다


driver = searching.driver

#인스타 접속
driver.get('https://www.instargram.com')
time.sleep(5) #시간을 넉넉히 설정합니다.

#로그인에 필요한 사항을 브라우저 제어를통해 입력합니다.
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()


time.sleep(3)
url = searching.insta_searching(word)
searching.driver.get(url)
time.sleep(2)

# 함수를 차례대로 실행합니다.
searching.select_first(driver)
results = []
target = 50  # 크롤링할 게시글 수
for i in range(target):
    # 게시글 수집에 오류 발생시 2초 대기후 다음글로 넘어갑니다.
    try:
        data = searching.get_content(driver)  # 게시글 정보 가져오기
        results.append(data)
        searching.move_next(driver)
    except:
        time.sleep(2)
        searching.move_next(driver)

# result적당히 출력해보기
print(results[:2])

DB.make_df(results)