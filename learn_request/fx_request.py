import requests
#推荐用text，用json（）容易报错，不好定位到错误，或者先用text再用json()
#=====注册=====
# url='http://192.168.114.130:8585/futureloan/mvc/api/member/register'    #注意空格、大小写等别写错
# param={'mobilephone':'18300070752','pwd':'12345678','regname':'李李莉莉'}

# #发送get请求
# resp=requests.get(url,params=param)
# print(resp.text)    #字符串类型#text是一个类里面的方法，被@property装饰，相当于一个属性所以不是resp.text（）
# print(resp.json())#字典类型
# print(type(resp.text))
# print(type(resp.json()))
#
# #发送post请求
# resp=requests.post(url,data=param)
# print(resp.text)#字符串类型
# print(resp.json())#字典类型 在这里json是一个函数，作用是转换成字典类型，与json语言没啥关系
        #==========登录==============
# url='http://192.168.114.130:8585/futureloan/mvc/api/member//login'    #注意空格、大小写等别写错
# param={'mobilephone':'18300070752','pwd':'12345678'}
# #发送get请求
# # resp=requests.get(url,params=param)
# # print(resp.text)
# # print(resp.json())
# #发送post请求
# resp=requests.post(url,data=param)
# print(resp.text)    #响应信息为空时是null
# print(resp.json())  #响应信息为空时是none
    #====利用json模块进行字符串和字典之间的转换
import json
#字符串转字典，有引号的话，key:value都必须是双引号，null-->>none
s='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'#字符串，python不能识别null
value=json.loads(s)  #字符串转字典，null变none，python才可识别  #要注意是loads（）而不是laod（）
print(value)
print(type(value))

#python字典转字符串，json格式的字符串
s1={'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}#字典
value1=json.dumps(s1,ensure_ascii=False)    #字典转字符串，字典有汉字时要设置 ensure_ascii=False#dumps()不是dump()
print(value1)
print(type(value1))
#python不能识别null，用loads（）转成