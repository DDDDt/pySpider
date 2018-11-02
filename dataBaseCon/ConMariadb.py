import pymysql
import DBUtils.PooledDB
import utils.LoadYaml
# 连接 mariadb
class MariadbCon(object):

    dataSourcePool = None
    
    # host='localhost',
    # user='user',
    # password='passwd',
    # db='db',
    # charset='utf8mb4',
    # cursorclass=pymysql.cursors.DictCursor
    # 得到数据连接
    @staticmethod
    def getCon():
        if dataSourcePool == None:
            dataSourcePool = mariadbCon.getDataSource(**keys)
            return dataSourcePool.connection()
        else:
            return dataSourcePool.connection()

# mincached，最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接
# maxcached，最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
# maxconnections，最大的连接数，
# blocking，当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错，
# maxshared 当连接数达到这个数，新请求的连接会分享已经分配出去的连接
    def getDataSource(self):
        mysqlResource = LoadYaml.getLoadYaml("D:\\github\pySpider\\dataBaseCon\\resource\\application.yml")
        host = mysqlResource['mariadb.host']
        port = mysqlResource['mariadb.port']
        user = mysqlResource['mariadb.username']
        pwd = mysqlResource['mariadb.password']
        mincached = mysqlResource['mariadb.mincached']
        maxcached = mysqlResource['mariadb.maxcached']
        maxconnections = mysqlResource['mariadb.maxconnections']
        blocking = mysqlResource['mariadb.blocking']
        maxshared = mysqlResource['mariadb.maxshared']
        db = mysqlResource['mariadb.db']
        poolDb = PooledDB(creator=pymysql,mincached=mincached,maxcached=maxcached,maxshared=maxshared,maxconnections=maxconnections,blocking=blocking,host=host,port=port,user=user,passwd=pwd,db=db)
        return poolDb

if __name__ == '__main__':
    con = MariadbCon.getCon()
    print("...")