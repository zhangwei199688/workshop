#A weibo purge script,which can be used to delete all your weibo content

from selenium import webdriver
import time


browser=webdriver.Firefox(executable_path = 'D:\Python\geckodriver')
browser.get("http://weibo.com")
time.sleep(20)#20秒内输入账号密码和验证码#
browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(5)
browser.find_element_by_xpath("//*[@id=\"v6_pl_rightmod_myinfo\"]/div/div/div[2]/ul/li[3]/a").click()
time.sleep(5)
count=0

while True:
    try:
        while True:
            browser.find_element_by_xpath("//*[@id=\"Pl_Official_MyProfileFeed__21\"]//a[@action-type=\"fl_menu\"]").click()
            browser.find_element_by_xpath("//*[@id=\"Pl_Official_MyProfileFeed__21\"]//a[@action-type=\"feed_list_delete\"]").click()
            browser.find_element_by_xpath("//*[@id=\"Pl_Official_MyProfileFeed__21\"]//p[@class=\"btn\"]/a").click()
            browser.refresh()
            time.sleep(10)
            count=0
    except Exception as e:
        count+=1
        print("Processing,%d in total"%count)
        if count>=1000:
            print("Finished")


