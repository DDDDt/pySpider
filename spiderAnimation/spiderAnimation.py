import requests
from pyquery import PyQuery as pq
# 爬取动漫花园
class SpiderAnimation(object):
    ## 查询
    def getHtml(self,url: str,**headers) -> str:
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            return req.text
        else:
            return None
    
    def getResultHeml(self,trPq: pq) -> (str,str,str,str,str,str,str,str,str):
        date = trPq('td:first span').text().split()
        dataType = trPq('td:eq(1) font').text().split()
        dataName = trPq('td:eq(2) a').text().split()
        dataUrl = trPq('td:eq(3) a').attr('href')
        dataSize = trPq('td:eq(4)').text().split()
        dataTor = trPq('td:eq(5)').text().split()
        dataDow = trPq('td:eq(6) span').text().split()
        dataCom = trPq('td:eq(7) a').text().split()
        dataCreater = trPq('td:eq(8) a').text().split()
        return (date,dataType,dataName,dataUrl,dataSize,dataTor,dataDow,dataCom,dataCreater)

    def getRegexHtml(self,html: str) -> list:
        pqHtml = pq(html)
        tabPq = pqHtml('#topic_list')
        rePq = tabPq('tbody tr')
        res = rePq.map(lambda i,e : self.getResultHeml(pq(e)))
        print(res.text)

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    spiderAnimation = SpiderAnimation()
    html = spiderAnimation.getHtml("https://www.dmhy.org/topics/list/page/1")
    spiderAnimation.getRegexHtml(html)
    # print(html)
        
