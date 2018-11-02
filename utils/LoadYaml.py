import yaml

class LoadYaml(object):
    
    @staticmethod
    def getLoadYaml(dirUrl: str) -> dict:
        f = open(dirUrl,'r',encoding='utf-8')
        cfg = f.read()
        print(type(cfg))
        print(cfg)
        d = yaml.load(cfg)
        print(type(d))
        print(d)
        return d

if __name__ == "__main__":
    LoadYaml.getLoadYaml("D:\\github\pySpider\\dataBaseCon\\resource\\application.yml")
