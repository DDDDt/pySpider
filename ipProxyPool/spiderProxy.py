# 免费的 ip 代理
from typing import Optional

import requests
class IpSpider(object):
    # 爬取免费代理网站·
    def getSpiderHtml(self,pageNum: int) -> Optional[str]:
        headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9",
                   "Cache-Control":"no-cache",
                   "Connection":"keep-alive",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
                   "Pragma":"no-cache",
                   "Upgrade-Insecure-Requests":"1",
                   "Host":"www.xicidaili.com",
                   "Cookie":"_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTA5ZjFmYzUyZGIxMDhlZDNkYjExNDg1YzZiY2RkNzFlBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXY5ajUxMDlGV3Aycm1VR2dkOTkxejI2TDRSa3h2RHJHWnI5RGFwYk14UkE9BjsARg%3D%3D--3c6eab246265ca678d138f8af5a454dd75ed48fa; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1539664173,1540353947; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1540353965"}
        url = "http://www.xicidaili.com/nn/{0}".format(pageNum)
        print(url)
        rep = requests.get(url,headers=headers)
        if rep.status_code == 200:
            return rep.text
        return None

if __name__ == "__main__":
    ipSpider = IpSpider()
    text = ipSpider.getSpiderHtml(1)
    print(text)
