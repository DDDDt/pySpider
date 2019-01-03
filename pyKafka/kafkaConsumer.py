# 读取 kafka 消息
from kafka import KafkaConsumer

class KafkaConsumerInfo(object):
    """
    labelTaskActivityEffectId -> 对应的表 member_label_task_activity_effect 的 id
    activityId -> 营销活动 id
    sendType -> 营销活动类型 营销活动类型.0-优惠券营销(coupon_rule),1-短信营销(market_activity)
    mebId -> 会员 id
    phone -> 手机号
    finish -> 发送结束
    """
    def __init__(self,labelTaskActivityEffectId: int,activityId: int,sendType: int,mebId: int,phone: str,finish: bool):
        self.labelTaskActivityEffectId = labelTaskActivityEffectId
        self.activityId = activityId
        self.sendType = sendType
        self.mebId = mebId
        self.phone = phone
        self.finish = finish


# 获取 kafka 实例
class KafkaUtils(object):

    # 得到 kafka 消费者
    def getKafkaConsumer(self) -> KafkaConsumer:
        comsumer = KafkaConsumer('',group_id = 'test-jy-group',bootstrap_servers=[])        
        comsumer
        return comsumer

# 执行
if __name__ == "__main__":
    kafkaUtils = KafkaUtils()
    consumer = kafkaUtils.getKafkaConsumer()
    for msg in consumer:
        print(msg.value)

    
