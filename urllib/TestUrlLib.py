import urllib.request
import urllib.parse
import ssl
import http.cookiejar
class learnUrlLib(object):
    def __init__(self):
        # 取消 ssl 验证
        ssl._create_default_https_context = ssl._create_unverified_context
    # 基础的urllib 请求
    def urlOpen(self):
        response = urllib.request.urlopen('https://www.baidu.com')
        print(type(response))
        # 获得状态吗
        print(response.status)
        # 获得请求头
        print(response.getheaders())
        print(response.read().decode("utf-8"))
    # 携带 data 的请求, 会自动转换为 post 请求
    def urlOpenDate(self):
        # 取消 ssl 验证                                                          
        ssl._create_default_https_context = ssl._create_unverified_context
        data = bytes(urllib.parse.urlencode({'hello':'word'}),encoding='utf-8')
        # 携带 data 后将转为 post 请求 ol0
        response = urllib.request.urlopen('http://httpbin.org/post',data=data)
        print(response.read())
    # 使用 urllib 的 request 请求
    def urllibRequest(self):
        # 使用简单的 request 来定义请求
        request = urllib.request.Request("https://www.baidu.com")
        response = urllib.request.urlopen(request)
        print(response.read().decode('utf-8'))
    # 添加请求头访问
    def urllibRequestHeader(self):
        # 请求头
        headers = {
            'X-Ua-Compatible' : 'IE=Edge,chrome=1',
            'Content-Type' : 'text/html;charset=utf-8'
        }
        # 请求参数
        data = {
            'name':'代陶'
        }
        dataBytes = bytes(urllib.parse.urlencode(data),encoding='utf-8')
        request = urllib.request.Request(url='http://httpbin.org/post',data=dataBytes,headers=headers,method='post')
        response = urllib.request.urlopen(request)
        print(response.read().decode('utf-8'))
    # 带有权限认证
    def urllibBaseAuthHandler(self):
        p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        uri = "https://www.baidu.com"
        userName = "dt"
        passwd = "123"
        p.add_password(None, uri, userName, passwd)
        auth = urllib.request.HTTPBasicAuthHandler(p)
        open = urllib.request.build_opener(auth)
        try:
            response = open.open("https://www.baidu.com")
            html = response.read().decode('utf-8')
            print(html)
        except urllib.request.URLError as e:
            print(e.reason)
    # 使用代理
    def urllibProxyHandler(self):
        proxy_handler = urllib.request.ProxyHandler({
            "http":"http://127.0.0.1:8080",
            "https":"http://127.0.0.1:8080"
        })
        opener = urllib.request.build_opener(proxy_handler)
        try:
            response = opener.open('https://www.baidu.com')
            print(response.read().decode('utf-8'))
        except urllib.request.URLError as e:
            print(e)

    # 获取 cookie
    def getCookie(self):
        cookie = http.cookiejar.CookieJar()
        cookHandler = urllib.request.HTTPCookieProcessor(cookie)
        opencer = urllib.request.build_opener(cookHandler)
        response = opencer.open('https://www.baidu.com')
        print(response)
        for coo in cookie:
            print(coo.name + ":" + coo.value)

if __name__ == "__main__":
    lul = learnUrlLib()
    # lul.urlOpen()
    # lul.urlOpenDate()
    # lul.urllibRequest()
    # lul.urllibRequestHeader()
    # lul.urllibBaseAuthHandler()
    # lul.urllibProxyHandler()
    lul.getCookie()