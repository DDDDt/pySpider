import pandas as pd
from ast import literal_eval
if __name__ == '__main__':
    # s = '[{"labelTaskActivityEffectId":59,"activityId":1000011111,"sendType":0,"mebId":255959027,"phone":"13941474803","finish":false},{"labelTaskActivityEffectId":59,"activityId":1000011111,"sendType":0,"mebId":255959027,"phone":"13941474803","finish":false},{"labelTaskActivityEffectId":59,"activityId":1000011111,"sendType":0,"mebId":255959027,"phone":"13941474803","finish":true}]'.replace("false","False").replace("true","True")
    # print(s)
    # df = pd.Series(literal_eval(s))
    # df.to_csv('D:\\excel\\test.csv',mode='a', header=False,index = False)
    s = None
    if not s:
        print(123)
