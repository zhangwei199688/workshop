############## a program to reply We-chat messages automaticlly
#coding=utf8
import itchat
import requests

function_list="1:自定义回复内容,2:聊天机器人，3:退出"
Model =1
defaultReply="您好，我现在有事不在，一会儿与您联系"


def get_response(msg):
    KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

if __name__ == '__main__':
        itchat.auto_login(hotReload=True)
        itchat.send(function_list, toUserName="filehelper")

        @itchat.msg_register(itchat.content.TEXT)
        def main(msg):
            global Model
            global defaultReply
            if msg["ToUserName"] == "filehelper" :
                Model=msg.text
            print(Model)
            if Model == '1':
                return defaultReply
            if Model == '2':
                DefaultReply = 'I received: ' + msg['Text']
                reply = get_response(msg['Text'])
                return reply or DefaultReply
            if Model == "3":
                itchat.logout()

        itchat.run()






