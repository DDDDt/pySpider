import requests
# 爬取动漫花园
class SpiderAnimation(object):
    ## 查询
    def getHtml(self,url: str,**headers) -> str:
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            return req.text
        else:
            return None

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    spiderAnimation = SpiderAnimation()
    html = spiderAnimation.getHtml("https://www.dmhy.org/topics/list/page/1")
    print(html)
        
