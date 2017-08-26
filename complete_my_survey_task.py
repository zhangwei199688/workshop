from selenium import webdriver
import time
from random import choice
import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

def get_ip():
    """获取代理IP"""
    url = "http://www.xicidaili.com/nn"
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                "Referer":"http://www.xicidaili.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                }
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
    ip = re.findall(ip_compile,str(data))       # 获取所有IP
    port = re.findall(port_compile,str(data))   # 获取所有端口
    return [":".join(i) for i in zip(ip,port)]

iplist=get_ip()
print(len(iplist))
for i in range(60):
    selectip=choice(iplist)
    proxy = Proxy(
      {
           'proxyType': ProxyType.MANUAL,  # 用不用都行
          'httpProxy': selectip
      }
    )
    browser=webdriver.Firefox(executable_path = 'D:\Python\geckodriver',proxy=proxy)

#browser=webdriver.PhantomJS(executable_path=r"D:\Anaconda\PhantomJS\phantomjs-1.9.7-windows\phantomjs.exe" )
    browser.get("http://sojump.com/m/16034514.aspx#")
    questions=browser.find_elements_by_xpath("//*[@id=\"fieldset1\"]/div/div[2]")
    for ele in questions:
       ele2=ele.find_elements_by_class_name("ui-radio")
       option=choice(ele2)
       option.find_element_by_class_name("jqradio").click()
    browser.find_element_by_xpath('//*[@id="ctlNext"]').click()
    browser.quit()
    time.sleep(20)



