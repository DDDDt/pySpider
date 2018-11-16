## 学习 python 中的正则表达式基础
import re
class LeanRegexBase(object):
    
    def leanrnRegBaseForOne(self):
        html = "<html><body><h1>hello world</h1></body></html>"
        start_index = html.find('<h1>')
        print(start_index)

        p1 = r"<h1>.+</h1>"
        # p1 = r"(?<=<h1>).+?(?=</h1>)"
        pat = re.compile(p1)
        # matcher1 = re.search(pat,html)
        # print(matcher1)
        # print(matcher1.group(0))

        # 返回一个列表
        print(pat.findall(html))
    
    def learnRegBaseForTwo(self):
        html = r"javapythonhtmlvhdl"
        p1 = r"python"
        mat = re.search(p1,html)
        print(mat)

if __name__ == "__main__":
    
    learnRegex = LeanRegexBase()
    learnRegex.leanrnRegBaseForOne()
    # learnRegex.learnRegBaseForTwo()