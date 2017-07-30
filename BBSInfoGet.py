#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

class Item(object):
    post_author=None
    post_title=None
    post_content=None
    post_publish_date=None
    replys_content=None
    replys_author=None
    replys_publish_date=None

class BBSInfoGet(object):
    def __init__(self,url):
        self.url=url
        self.pagenum=self.PageNumGet(url)
        self.urllist=self.urlget(self.pagenum)
        self.item1,self.item2=self.spider(self.urllist)
        self.pipelines(self.item1,self.item2)

    def PageNumGet(self,url):
        list=[]
        a=requests.get(url)
        a.encoding="gb2312"
        soup=BeautifulSoup(a.content,"lxml")
        b=soup.find("div",attrs={"class":"fn_0209"})
        c=b.find_all("a")
        for tip in c:
            list.append(tip.get_text())
        return int(list[-2])
    def urlget(self,pagenum):
        urllist=[]
        i=1
        while(i<pagenum+1):
            url1=url+"&page="+str(i)
            urllist.append(url1)
            i=i+1
        return urllist

    def spider(self,urllist):
        post_dict={"content":None,"title":None,"Author":None,"publish_date":None}
        reply_list=[]
        reply_content_list=[]
        reply_author_list=[]
        reply_time_list=[]
        item=Item()
        html=requests.get(urllist[0])
        html.encoding="gb2312"
        htmlcontent=html.content
        soup=BeautifulSoup(htmlcontent,"lxml")
        item.post_author = soup.find("a",attrs={"class":"bold"}).get_text()
        item.post_title = soup.find("span",attrs={"class":"t_title1"}).get_text()
        date=soup.find("div",style="padding-top: 4px;float:left").get_text().split()[1].split("-")
        item.post_publish_date=''.join(date)
        item.post_content=soup.find("td",attrs={"class":"line"}).get_text().strip("\n")
        post_dict["content"]=item.post_content
        post_dict["title"]=item.post_title
        post_dict["Author"]=item.post_author
        post_dict["publish_date"]=item.post_publish_date
        for url in urllist:
            htmlreply=requests.get(url)
            htmlreply.encoding="gb2312"
            htmlreplycontent=htmlreply.content
            soup1=BeautifulSoup(htmlreplycontent,"lxml")
            postlistcontent=soup1.find_all("td",attrs={"class":"line"})
            for post in postlistcontent:
                item.replys_content=post.get_text().strip()
                reply_content_list.append(item.replys_content)
            postlistauthor=soup1.find_all("td",attrs={"class":"t_user"})
            for post in postlistauthor:
                item.replys_author=post.find("a",attrs={"class":"bold"}).get_text()
                reply_author_list.append(item.replys_author)
            postlisttime=soup1.find_all("div",style="padding-top: 4px;float:left")
            for post in postlisttime:
                time=post.get_text().split()[1].split("-")
                item.replys_publish_date="".join(time)
                reply_time_list.append(item.replys_publish_date)
        del reply_content_list[0]
        del reply_author_list[0]
        del reply_time_list[0]
        num=len(reply_content_list)

        for i in range(num):
            reply_dict={"content":None,"author":None,"publish_date":None}
            reply_dict["content"]=reply_content_list[i]
            reply_dict["author"]=reply_author_list[i]
            reply_dict["publish_date"]=reply_time_list[i]
            reply_list.append(reply_dict)

        str1=self.quotechange(str(post_dict))
        str2=self.quotechange(str(reply_list))
        return str1,str2


    def pipelines(self,post,reply):
        with open(r"D:\result.txt","a") as fp:
            fp.write("%s {\"post\":%s,\"replys\":%s}\n"%(self.url,post,reply))

    def quotechange(self,str):
        strinfo = re.compile('\'')
        b = strinfo.sub('\"',str)
        return b
if __name__=="__main__":
    InputUrlList=["http://www.xcar.com.cn/bbs/viewthread.php?tid=11939671","http://www.xcar.com.cn/bbs/viewthread.php?tid=17791218"]
    for url in InputUrlList:
        GTI=BBSInfoGet(url)








