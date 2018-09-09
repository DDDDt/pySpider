import requests
from requests import Request
from requests.auth import HTTPBasicAuth
from requests.cookies import RequestsCookieJar


class learnRequest(object):

    # cookie 请求
    def requestGet(self):
        response = requests.get("https://www.baidu.com")
        print(response)
        print(response.text)
        print(response.cookies)
        # 带有请求参数的 get 请求
        paramData = {
            "name":"dt",
            "age":15
        }
        rep = requests.get("https://www.baidu.com",paramData)
        print(rep)
        print(rep.text)
    # 抓取二进制数据
    def request2(self):
        res = requests.get("https://github.com/favicon.ico")
        print(res.text)
        print(res.content)
        # 将二进制图片保存下来
        with open('favicon.ico','wb') as r:
            r.write(res.content)

    # 带请求头
    def addHeader(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }
        rep = requests.get("https://www.zhihu.com/explore",headers=headers)
        print(rep.text)

    # post 请求
    def postReq(self):
        data = {
            "name":"dt",
            "age":25
        }
        rep = requests.post("http://httpbin.org/post",data=data)
        print(rep.text)
        print(rep.json())
        print(type(rep))
        print(rep.status_code)
        print(rep.history)

    # 上传文件
    def fileReq(self):
        files = {'file':open('favicon.ico','rb')}
        rep = requests.post("http://httpbin.org/post",files=files)
        print(rep.text)

    # 获取 cookie
    def getCookie(self):
        rep = requests.post("https://www.baidu.com")
        print(rep.cookies)
        for key,value in rep.cookies.items():
            print("key = " + key + ",value = "+value)
    # 设置 cookir 访问
    def setHeaderCookie(self):
        headers = {
            'cookie': '_zap = 402708f6 - eb50 - 429b - 89ce - 029b677920ab;__DAYU_PP = FQnMUV3UjZMmqiEYejqZ6219b3cb366f;d_c0 = "AIBu1LttiQ2PTs79Mv4LpVV5fEWA1miHbEk=|1525340979";z_c0 = "2|1:0|10:1528512969|4:z_c0|92:Mi4xbXJ4M0FBQUFBQUFBZ0c3VXUyMkpEU1lBQUFCZ0FsVk55WThJWEFCZXE0Nm1fMEk3WUpyMmRTZEg2NGQzQzlSWDZB|961e2e8dc85de63413e07bec5f11afb4f46e8604762d3e2a6d2c987b74b960f4";tgw_l7_route = 23ddf1acd85bb5988efef95d7382daa0;q_c1 = a6e26fbab832456a8c942c55183a7961 | 1536466860000 | 1517718423000;_xsrf = 931ce46c204a7ccbcdefd3bc406526e4;__utma = 51854390.2143007096.1536466863.1536466863.1536466863.1;__utmb = 51854390.0.10.1536466863;__utmc = 51854390;__utmz = 51854390.1536466863.1.1.utmcsr = (direct) | utmccn = (direct) | utmcmd = (none);__utmv = 51854390.100 - 1 | 2 = registration_date = 20140901 = 1 ^ 3 = entry_date = 20140901 = 1;_xsrf = NF7ybUMiE0WXik7Pk5Xj7oMjZq4Vj3xD',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }
        rep = requests.get("https://www.zhihu.com/explore", headers=headers)
        print(rep.text)

    # 自定义 cookie 对象
    def setCookie(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }
        cookie = 'zap = 402708f6 - eb50 - 429b - 89ce - 029b677920ab;__DAYU_PP = FQnMUV3UjZMmqiEYejqZ6219b3cb366f;d_c0 = "AIBu1LttiQ2PTs79Mv4LpVV5fEWA1miHbEk=|1525340979";z_c0 = "2|1:0|10:1528512969|4:z_c0|92:Mi4xbXJ4M0FBQUFBQUFBZ0c3VXUyMkpEU1lBQUFCZ0FsVk55WThJWEFCZXE0Nm1fMEk3WUpyMmRTZEg2NGQzQzlSWDZB|961e2e8dc85de63413e07bec5f11afb4f46e8604762d3e2a6d2c987b74b960f4";tgw_l7_route = 23ddf1acd85bb5988efef95d7382daa0;q_c1 = a6e26fbab832456a8c942c55183a7961 | 1536466860000 | 1517718423000;_xsrf = 931ce46c204a7ccbcdefd3bc406526e4;__utma = 51854390.2143007096.1536466863.1536466863.1536466863.1;__utmb = 51854390.0.10.1536466863;__utmc = 51854390;__utmz = 51854390.1536466863.1.1.utmcsr = (direct) | utmccn = (direct) | utmcmd = (none);__utmv = 51854390.100 - 1 | 2 = registration_date = 20140901 = 1 ^ 3 = entry_date = 20140901 = 1;_xsrf = NF7ybUMiE0WXik7Pk5Xj7oMjZq4Vj3xD'
        jar = RequestsCookieJar()
        for coo in cookie.replace(" ","").split(";"):
            print(coo)
            key,value = coo.split("=",1)
            print(key,value)
            jar.set(key,value)
        rep = requests.get("https://www.zhihu.com/explore",cookies = jar,headers=headers)
        print(rep.text)

    # 保持同一会话 session
    def setSession(self):
        session = requests.Session()
        session.get("http://httpbin.org/cookies/set/number/123456")
        r = session.get("http://httpbin.org/cookies")
        print(r.text)

    # 取消 ssl
    def isSssl(self):
        rep = requests.get("http://www.12306.cn/mormhweb/",verify=False)
        print(rep.status_code)

    # 代理
    def proxyHttp(self):
        # 请使用可用代理
        proxys = {
            'http':'http://127.0.0.1:3128',
            'https':'http://127.0.0.1:3128'
        }
        rep = requests.get("https://taobao.com",proxies=proxys)
        print(rep.text)

    # 设置超时时间
    def timeOutHttp(self):
        # 设置请求超时间
        # rep = requests.get("https://taobao.com",timeout=1)
        # 单独为请求和响应设置时间
        rep = requests.get("https://taobao.com",timeout=(10,30))
        print(rep.text)

    # 身份认证
    def baseAuth(self):
        rep = requests.get("https://www.baidu.com",auth=HTTPBasicAuth('username','password'))
        print(rep.text)

    # 和 urllib 一样 设置 request 请求
    def requestReq(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }
        paramData = {
            "name": "dt",
            "age": 15
        }
        url = 'http://httpbin.org/post'
        req = Request('POST',url,data = paramData,headers = headers)
        s = requests.Session()
        pre = s.prepare_request(req)
        rep = s.send(pre)
        print(rep.text)

if __name__ == "__main__":
    req = learnRequest()
    # req.requestGet()
    # req.request2()
    # req.addHeader()
    # req.postReq()
    # req.fileReq()
    # req.getCookie()
    # req.setHeaderCookie()
    # req.setCookie()
    # req.setSession()
    # req.isSssl()
    # req.proxyHttp()
    # req.timeOutHttp()
    req.requestReq()