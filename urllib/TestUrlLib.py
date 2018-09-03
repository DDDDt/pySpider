import urllib.request
import urllib.parse
import ssl
class learnUrlLib(object):
    def urlOpen(self):
        # 取消 ssl 验证
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen('https://www.baidu.com')
        print(type(response))
        # 获得状态吗
        print(response.status)
        # 获得请求头
        print(response.getheaders())
        print(response.read().decode("utf-8"))
    def urlOpenDate(self):
        # 取消 ssl 验证                                                          
        ssl._create_default_https_context = ssl._create_unverified_context
        data = bytes(urllib.parse.urlencode({'hello':'word'}),encoding='utf-8')
        # 携带 data 后将转为 post 请求 ol0
        response = urllib.request.urlopen('http://httpbin.org/post',data=data)
        print(response.read())


if __name__ == "__main__":
    lul = learnUrlLib()
    # lul.urlOpen()
    lul.urlOpenDate()
