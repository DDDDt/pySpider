import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient
import hashlib

# 爬取动漫花园的数据类, 用语保存数据信息
class DmhyInfo(object):

    """
        id -> 用作 mongodb id
        date -> 日期
        dataType -> 分类
        dataName -> 动漫名
        dataUrl -> 下载地址
        dataSize -> 文件大小
        dataTor -> 种子
        dataDow -> 下载
        dataCom -> 完成
        dataCreater -> 发布人
        具体结构查看动漫花园表结构 -> http://share.dmhy.org/
    """
    def __init__(self,id,date,dataType,dataName,dataUrl,dataSize,dataTor,dataDow,dataCom,dataCreater):
        self._id = id
        self.date = date
        self.dataType = dataType
        self.dataName = dataName
        self.dataUrl = dataUrl
        self.dataSize = dataSize
        self.dataTor = dataTor
        self.dataDow = dataDow
        self.dataCom = dataCom
        self.dataCreater = dataCreater
# 读取的数据存入 mongodb
class addMongo(object):
    def getCon(self):
        client = MongoClient('mongodb://:27017/')
        return client
    # 插入 相关信息
    def addMongoInfo(self):
        client = self.getCon()
        db = client.pySpider
        col = db.animation_info

        

# 爬取动漫花园
class SpiderAnimation(object):
    ## 查询
    def getHtml(self,url: str,**headers) -> str:
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            return req.text
        else:
            return None
    
    def getResultHeml(self,trPq: pq) -> DmhyInfo:
        date = trPq('td:first span').text()
        print(date)
        dataType = trPq('td:eq(1) font').text().split()
        dataName = trPq('td:eq(2) a').text().split()
        dataUrl = trPq('td:eq(3) a').attr('href')
        dataSize = trPq('td:eq(4)').text().split()
        dataTor = trPq('td:eq(5)').text().split()
        dataDow = trPq('td:eq(6) span').text().split()
        dataCom = trPq('td:eq(7) a').text().split()
        dataCreater = trPq('td:eq(8) a').text().split()
        md = hashlib.md5()
        md.update(dataName+dataUrl)
        _id = md.digest()
        return DmhyInfo(_id,date,dataType,dataName,dataUrl,dataSize,dataTor,dataDow,dataCom,dataCreater)

    def getRegexHtml(self,html: str) -> list:
        pqHtml = pq(html)
        tabPq = pqHtml('#topic_list')
        rePq = tabPq('tbody tr')
        res = rePq.map(lambda i,e : self.getResultHeml(pq(e)))
        return res

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    spiderAnimation = SpiderAnimation()
    html = spiderAnimation.getHtml("https://www.dmhy.org/topics/list/page/1")
    result = spiderAnimation.getRegexHtml(html)
        
