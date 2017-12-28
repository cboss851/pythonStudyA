import itchat

# 登录
itchat.login()
# 发送消息
itchat.send(u'你好~~~~', 'filehelper')
# itchat.send(u'在上课吗', 'wxid_3p6va0uka5rv22')
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
for i in friends:
  print("-----------")
  print(i)
  print(i["RemarkName"])
  if "悦" == i["RemarkName"] :
    print(i["RemarkName"])
    i.send(u'say hello')
  # if "LP晓晓" == i["RemarkName"] :
  #   print(i["RemarkName"])
  #   i.send(u'Python 学习1')

#name后填微信备注即可
# users = itchat.search_friends(name = '悦')
# users.send(u'Python 学习2')
itchat.run()

