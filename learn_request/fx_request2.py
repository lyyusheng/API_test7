import requests
url='http://192.168.114.130:8585/futureloan/mvc/api/member//login'    #注意空格、大小写等别写错
param={'mobilephone':'18300070752','pwd':'12345678'}
#头部
headers={'User-Agent':'Mozilla/5.0 '}   #在请求头伪装发起请求的软件，伪装成firefox浏览器发起的请求  #不要打个空格进去
#模拟从firefox浏览器发送的请求，参数可以浏览器F12或者抓包工具抓请求头
#发送post请求
resp=requests.post(url,data=param,headers=headers)#post请求用data，headers是关键字参数，必须键值对的形式传入
print(resp.text)

#获取响应结果：状态码、响应报文，响应头、cookis
print('状态码：',resp.status_code)
print('响应头:',resp.headers)
print('cookie:',resp.cookies)

print('请求头:',resp.request.headers)
#返回结果请求头： {'User-Agent':'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#中的 ： {'User-Agent': 'python-requests/2.21.0'是代理，是由python发起的请求

#充值 需要用到cookies
url='http://192.168.114.130:8585/futureloan/mvc/api/member//recharge'
param={'mobilephone':'18300070752','pwd':'12345678','amount':'15000'}
resp1=requests.get(url,params=param,cookies=resp.cookies)#把登陆时的cookis传进来
print('充值结果是：',resp1.text)#字符串类型