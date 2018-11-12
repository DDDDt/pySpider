from pymongo import MongoClient
# 连接 Mongodb
class MongodbCon(object):
    
    @staticmethod
    def get_connection(self,userName,passWord,hostlist,database,authSource):
        return MongoClient("mongodb://{userName}:{passWord}@{hostlist}/{database}?authSource={authSource}".format(userName,passWord,hostlist,database,authSource))
