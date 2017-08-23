#帮助忘记CET准考证号的同学找回准考证号
#import json
import requests

url="http://app.cet.edu.cn:7066/baas/app/setuser.do?method=UserVerify"
kind=input("查询CET4准考证号请输入1，CET6请输入2:")

ks_data = {
"ks_xm":input("请输入姓名:"),
"ks_sfz":input("请输入身份证号："),
"jb":kind
}

postdata = {
"action": "",
"params":json.dumps(ks_data)
}

re=requests.post(url,data=postdata)


print(re.json()["ks_bh"])