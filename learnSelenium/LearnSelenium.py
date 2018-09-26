from selenium import webdriver
class LearnSelenium(object):
    def testSeleniumForOne(self):
        driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        driver.get("https://www.baidu.com")
        print("开始--------")
        # 设置浏览器打开大小
        driver.set_window_size(480,800)
        # 前进和后退


        # 得到标题
        title = driver.title
        print(title)
        driver.close()


if __name__ == "__main__":
    sel = LearnSelenium()
    sel.testSeleniumForOne()