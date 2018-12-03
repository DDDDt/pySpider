# 爬取动漫花园的数据类, 用语保存数据信息
class DmhyInfo(object):

    """
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
    def __init__(self,date,dataType,dataName,dataUrl,dataSize,dataTor,dataDow,dataCom,dataCreater):
        self.date = date
        self.dataType = dataType
        self.dataName = dataName
        self.dataUrl = dataUrl
        self.dataSize = dataSize
        self.dataTor = dataTor
        self.dataDow = dataDow
        self.dataCom = dataCom
        self.dataCreater = dataCreater
