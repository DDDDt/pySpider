# python 正则中级
import re
class LearnRegexMiddle(object):
    
    
    # \d+.?\d+.?\d+.?\d+
    # \d+{1,3}.?\d+{1,3}.?\d+{1,3}.?+d+{1,3}
    #(\d+{1,3}.?){3}\d+{1,3}\.


    # 向前向后匹配
    # ?<= 表示在被匹配字符前必须的有<h1>, ?= 表示被匹配字符后必须有
    def beforeAndAfter(self):
        html = r'<html><body><h1>hello world</h1></body></html>'
        p1 = r"(?<=<h1>).+?(?=</h1>)"
        pat = re.compile(p1)
        print(pat.findall(html))
    
    # 回溯引用
    def regexMiddle(self):
        html = r"<h1>hello world</h1>"
        p1 = r"<h([1-6])>.*?</h\1>"
        pat = re.compile(p1)
        print(pat.findall(html)[0])

if __name__ == "__main__":
    learnRegexMiddle = LearnRegexMiddle()
    # learnRegexMiddle.beforeAndAfter()
    learnRegexMiddle.regexMiddle()
