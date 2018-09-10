import requests,re
# 正则表达式
class LearnRegex(object):
    def testMatch(self):
        str = 'Hello 123 456 World_This is a Regex Demo'
        # ^ 是以什么开头
        res = re.match("^Hello\s\d\d\d\s\d\d\d",str)
        print(res)
        print(res.group())
        print(res.span())
        # 用正则表达式求出数字
        numRes = re.match("^Hello\s(\d+)\s(\d+)",str)
        print(numRes.group(1))
        print(numRes.group(2))


    def testBaidu(self):
        rep = requests.get("https://www.baidu.com")
        print(rep.text)
        str = rep.text

        # 只能匹配第一个
        res = re.search("<a\shref=//(.*?)\sname",str,re.S)
        print(res)
        print(res.group(1))

        # 匹配所有的字段
        reall = re.findall("<a\shref=//(.*)\sname",str,re.S)
        print(reall)

    # 修改文本
    def testSub(self):
        rep = requests.get("https://www.baidu.com")
        print(rep.text)
        str = rep.text
        str = re.sub("\d",'',str)
        print(str)

if __name__ == "__main__":
    req = LearnRegex()
    # req.testMatch()
    # req.testBaidu()
    req.testSub()