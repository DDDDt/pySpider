# 读取 kafka 消息
from kafka import KafkaConsumer
import json
import pymysql

class KafkaConsumerInfo(object):
    """
    labelTaskActivityEffectId -> 对应的表 member_label_task_activity_effect 的 id
    activityId -> 营销活动 id
    sendType -> 营销活动类型 营销活动类型.0-优惠券营销(coupon_rule),1-短信营销(market_activity)
    mebId -> 会员 id
    phone -> 手机号
    finish -> 发送结束
    """
    def __init__(self,labelTaskActivityEffectId: int,taskId: int,activityId: int,sendType: int,mebId: int,phone: str,finish: bool):
        self.labelTaskActivityEffectId = labelTaskActivityEffectId
        self.taskId = taskId
        self.activityId = activityId
        self.sendType = sendType
        self.mebId = mebId
        self.phone = phone
        self.finish = finish


# 获取 kafka 实例
class KafkaUtils(object):

    # 得到 kafka 消费者
    def getKafkaConsumer(self) -> KafkaConsumer:
        comsumer = KafkaConsumer('',group_id = 'test-dt-group',bootstrap_servers=[])
        return comsumer
    # 保存到 mysql 
    def save_mysql(self,usersvalues: list):
        config = {
            # 数据库
            "db": "marketing_db",
            #服务器IP
            "host": "",
            #账号
            "user": "bigdata",
            #密码
            "passwd": "",
            #端口号
            "port": 3306
        }
        con = pymysql.connect(**config)
        cur = con.cursor()
        sql = "INSERT INTO member_label_task_test(labelTaskActivityEffectId,taskId,activityId,sendType,mebId,phone,finish) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cur.executemany(sql,usersvalues)
        con.commit()
        cur.close()
        con.close()
        print(usersvalues)
        

# 执行程序
if __name__ == "__main__":
    kafkaUtils = KafkaUtils()
    consumer = kafkaUtils.getKafkaConsumer()
    for msg in consumer:
        if msg.value:
            print(msg.value)
            messageList = msg.value.decode()
            jsonMessageList = json.loads(messageList)
            usersvalues = map(lambda message: (message["labelTaskActivityEffectId"],message["taskId"],message["activityId"],message["sendType"],message["mebId"],message["phone"],message["finish"]),jsonMessageList)
            kafkaUtils.save_mysql(list(usersvalues))

                

