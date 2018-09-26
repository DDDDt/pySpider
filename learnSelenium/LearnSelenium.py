from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LearnSelenium(object):
    def testSeleniumForOne(self):
        driver = webdriver.Chrome(executable_path="/Users/dt/Downloads/chromedriver")
        driver.get("https://www.baidu.com")
        print("开始--------")
        # 设置浏览器打开大小
        # driver.set_window_size(480,800)
        # 前进和后退

        # 得到标题
        title = driver.title
        print(title)

        # 得到具体内容
        source = driver.page_source
        print(source)

        # 操作具体的内容

        # 操作 ID
        input = driver.find_element_by_id("kw")
        input.send_keys("python")
        # input.send_keys(Keys.ENTER)

        # 提交按钮
        su = driver.find_element_by_id("su")
        print(su)
        su.click()
        print(su.get_attribute("class"))
        print(su.text)
        print(su.id)
        print(su.location)
        print(su.size)
        print(su.tag_name)
        # WebDriverWait(driver,100)

        driver.close()


    # 延时等待
    def learnAwit(self):
        driver = webdriver.Chrome(executable_path="/Users/dt/Downloads/chromedriver")
        try:
            # 隐式等待 10 s
            # driver.implicitly_wait(10)
            driver.get("https://www.zhihu.com/explore")
            # input = driver.find_element_by_class_name("zu-top-add-question")
            # 显示等待 10 s, 根据具体条件没有出现就报错，或者在 10 s 内不能点击也报错,根据传入的条件判断 -> TimeoutException: Message:
            wait = WebDriverWait(driver,10)
            input = wait.until(expected_conditions.presence_of_element_located((By.ID,'q')))
            button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
            print(input,button)
            #显示等待时间
        finally:
            driver.close()

if __name__ == "__main__":
    sel = LearnSelenium()
    # sel.testSeleniumForOne()
    sel.learnAwit()