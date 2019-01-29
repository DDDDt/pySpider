#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient
import hashlib
from pymongo import errors
import time


# 爬取动漫花园的数据类, 用语保存数据信息
class DmhyInfo:
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
    def __init__(self,_id: str,date: str,dataType: str,dataName: str,dataUrl: str,dataSize: str,dataTor: str,dataDow: str,dataCom: str,dataCreater:str):
        self._id = _id
        self.date = date
        self.dataType = dataType
        self.dataName = dataName
        self.dataUrl = dataUrl
        self.dataSize = dataSize
        self.dataTor = dataTor
        self.dataDow = dataDow
        self.dataCom = dataCom
        self.dataCreater = dataCreater

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Connection': 'close'
    }

# 读取的数据存入 mongodb
class AddMongo(object):
    def getCon(self):
        client = MongoClient('mongodb://root:/admin')
        return client
    # 插入 相关信息, -> 目前是同步, 以后可以改为异步
    def addMongoInfo(self,dmhyInfo: DmhyInfo) -> bool:
        bol = True
        client = self.getCon()
        try:
            # 库
            db = client.pySpider
            # 集合
            col = db.animation_info
            col.insert_one(dmhyInfo.__dict__)
        # 通过 id 判断有无重复
        except errors.DuplicateKeyError as e:
            print(e)
            bol = False
        finally:
            client.close()
            return bol

# 爬取动漫花园
class SpiderAnimation(object):
    ## 查询
    def getHtml(self,url: str,**headers) -> str:
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            return req.text
        else:
            print(req)
            return None
    
    def getResultHeml(self,trPq: pq) -> DmhyInfo:
        date = trPq('td:first span').text()
        dataType = trPq('td:eq(1) font').text()
        dataName = trPq('td.title > a').text()
        dataUrl = trPq('td:eq(3) a').attr('href')
        if not dataUrl:
            url = trPq('td.title > a').attr('href')
            dataUrl = self.getMagnet("https://www.dmhy.org"+url)
        dataSize = trPq('td:eq(4)').text()
        dataTor = trPq('td:eq(5)').text()
        dataDow = trPq('td:eq(6) span').text()
        dataCom = trPq('td:eq(7) a').text()
        dataCreater = trPq('td:eq(8) a').text()
        md = hashlib.md5()
        md.update((','.join(dataName)+dataUrl).encode('utf-8'))
        _id = md.hexdigest()
        return DmhyInfo(_id,date,dataType,dataName,dataUrl,dataSize,dataTor,dataDow,dataCom,dataCreater)

    # 得到磁力链接    
    def getMagnet(self,url: str) -> str:
        html = self.getHtml(url,**headers)
        if not html:
            print("未获取磁力链接: "+url)
            return ''
        pqHtml = pq(html)
        magnet = pqHtml("#a_magnet").text()
        return magnet

    # 获取爬虫爬取的相关信息
    def getRegexHtml(self,html: str) -> list:
        pqHtml = pq(html)
        tabPq = pqHtml('#topic_list')
        rePq = tabPq('tbody tr')
        res = rePq.map(lambda i,e : self.getResultHeml(pq(e)))
        return res

if __name__ == "__main__":
    spiderAnimation = SpiderAnimation()
    # 当前分页
    pageNum = 1
    # 阈值
    sameCodeNum = 6
    bol = True
    while bol:
        html = spiderAnimation.getHtml("https://www.dmhy.org/topics/list/page/{0}".format(pageNum),**headers)
        if not html:
            print("https://www.dmhy.org/topics/list/page/{0} -> 为空".format(pageNum))
            break
        result = spiderAnimation.getRegexHtml(html)
        if not result:
            print("{0}为空".format(pageNum))
            bol = False
            pageNum+=1
            break
        else:
            sameCodeErrorNum = 0
            mongo = AddMongo()
            for i in result:
                sameCodeErrorNum += 1
                bol = mongo.addMongoInfo(i)
                if not bol:
                    if sameCodeNum < sameCodeErrorNum:
                        break
        print("完成 -> {0}".format(pageNum))
        pageNum+=1
        # 做人要良心, 就算单线程爬, 也不能影响别人
        time.sleep(10)
            