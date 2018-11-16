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
    
    # 基础正则
    def learnRegBaseForTwo(self):
        html = r"javapythonhtmlvhdl"
        p1 = r"python"
        mat = re.search(p1,html)
        print(mat)

    # 正则 *
    def learnRegBaseForAll(self):
        html = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"
        p1 = r"http*://"
        pat = re.compile(p1)
        print(pat.findall(html))
    
    # 正则，抽取某个字符列表中的任意一个
    def learnRegBaseForOnList(self):
        html = r"lalala<hTml>hello</Html>heiheihei"
        p1 = r"<[hH][tT][mM][lL].+</[hH][tT][mM][lL]>"
        pat = re.compile(p1)
        print(pat.findall(html))
    
    # 正则, 抽取非某个字符 ^
    def learnRegBaseNo(self):
        html = r"mat cat hat pat"
        p1 = r"[^p]at"
        pat = re.compile(p1)
        print(pat.findall(html))
    
    # 解决正则匹配中的贪婪
    def learnRegBaseGreedy(self):
        html = r"chuxiuhong@hit.edu.cn"
        p1 = r"@.+?\."
        # p1 = r"@*?\."
        pat = re.compile(p1)
        print(pat.findall(html))

    # 控制重复次数{}
    def learnRegBaseForMore(self):
        html = r"saas and sas and saaas"
        p1 = r"sa{1,3}s"
        pat = re.compile(p1)
        print(pat.findall(html))



if __name__ == "__main__":
    
    learnRegex = LeanRegexBase()
    # learnRegex.leanrnRegBaseForOne()
    # learnRegex.learnRegBaseForTwo()
    # learnRegex.learnRegBaseFor()
    # learnRegex.learnRegBaseForOnList()
    # learnRegex.learnRegBaseNo()
    # learnRegex.learnRegBaseGreedy()
    learnRegex.learnRegBaseForMore()