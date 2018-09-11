import requests,re,time
# 抓取猫眼电影 Top 100
class SpiderTop100(object):
    def getHtml(self,page) -> str:
        headers = {
            'Cookie':'mta=142471821.1536676595061.1536676673019.1536676846231.6; _lxsdk_cuid=165c90ffb56c8-0e181e7a88554-1033685c-1aeaa0-165c90ffb56c8; uuid_n_v=v1; uuid=14B150B0B5D011E8B7A18DF63F03337FD2B573E90F984FF9AD41767DA6C9FC7C; _csrf=a97c5d3b44909dba120ea5041839d5114278d89ec86559e92f6dc3df2a8fc9fd; _lxsdk=14B150B0B5D011E8B7A18DF63F03337FD2B573E90F984FF9AD41767DA6C9FC7C; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=142471821.1536676595061.1536676673019.1536676839811.6; _lxsdk_s=165c90ffb57-e85-530-21d%7C%7C23',

            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'Upgrade-Insecure-Requests':'1',
            'Host':'maoyan.com',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive'
        }
        try:
            rep = requests.get("http://maoyan.com/board/4?offset="+str(page),headers=headers)
            print(rep.text)
            if rep.status_code == 200:
                return rep.text
            return None
        except requests.RequestException as e:
            print(e)
            return None

if __name__ == "__main__":
    spider = SpiderTop100()
    for i in range(10):
        print(i)
        maoyanHtml = spider.getHtml(i*10)
        print(maoyanHtml)
        reStr = re.findall('<dd>.*?board-index.*?>(.*?)</i>.*?movieId:(.*?)}.*?data-src="(.*?)".*?<p.*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>',maoyanHtml,re.S)
        print(reStr)
        time.sleep(10)