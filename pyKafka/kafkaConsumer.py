# 读取 kafka 消息
from kafka import KafkaConsumer
# import pandas as pd
from ast import literal_eval
import json,xlwt

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
        comsumer = KafkaConsumer('bigdata-marketing-user',group_id = 'test-jy-group',bootstrap_servers=[])        
        return comsumer

    def write_excel(self,path):            # path
        # 创建工作簿
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建sheet
        data_sheet = workbook.add_sheet('sheet1')
        # row0 = [u'酒店ID',"BIG_DATA_HOTEL_ID", u'酒店名称', '倒挂产品', '限定最高价',"实际标价","酒店地址","url","抓取时间","入住时间","退房时间"]

        # for j, q in enumerate(row0):
        #     data_sheet.write(0, j, q)
        workbook.save(path)            # 第一次调用，创建文件
        index = 1
        while True:
            record = yield "ok"
            if record == "close":
                workbook.save(path)
                return
            for i,q in enumerate(record):
                data_sheet.write(index, i, q)
            index += 1
            workbook.save(path)
    # 保存到 mysql 
    def save_mysql(self,message):



    
# 执行程序
if __name__ == "__main__":
    dict_ = {}
    kafkaUtils = KafkaUtils()
    consumer = kafkaUtils.getKafkaConsumer()
    for msg in consumer:
        if msg.value:
            messageList = msg.value.decode()
            jsonMessageList = json.loads(messageList)
            for message in jsonMessageList:
                labelTaskActivityEffectId = message["labelTaskActivityEffectId"]
                if labelTaskActivityEffectId not in dict_.keys():
                    excel_path = "labelTaskActivityEffectId_{}.xls".format(labelTaskActivityEffectId)
                    excel = write_excel(excel_path)
                    excel.__next__()  # 创建文件
                    dict_[labelTaskActivityEffectId] = excel
                else:
                    excel = dict_[labelTaskActivityEffectId]

                excel.send(message.values())  # record是个列表，元素索引位置与excel对应
                print(msg.value)
    # for msg in consumer:
    #     if msg.value:
    #         print(msg.value)
    #         value = msg.value.replace("false","False").replace("true","True")
    #         df = pd.Series(literal_eval(value))
    #         df.to_csv('D:\\excel\\test.csv',mode='a', header = False, index = False)

    
