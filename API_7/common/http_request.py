# 1：根据提供的注册登录接口，完成注册登录接口的请求，至少每个接口有5条用例，每个接口要至少有
# 一个正向用例。
#  2：要求如下： 1）http请求类（可以根据传递的method--get/post完成不同的请求），要求有返回值。
# 2）测试用例的数据存储在Excel中，并编写一个从Excel中读取数据的测试类，包含的函数能够读取测试
# 数据，并且能够写回测试结果，要求有返回值。 3）新建一个run.py文件，在这里面完成Excel数据的读
# 取以及完成用例的执行，并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。
import requests

resp1 = None


class HttpRequest:
    """http请求类（可以根据传递的method--get/post完成不同的请求），要求有返回值"""

    def http_request(self, method, url, param, cookies):
        """根据请求方法来决定发起get请求还是post请求
        method: http的请求方式，get或者post
        url:发送请求的接口地址
        param:随接口发送的请求参数，以字典格式传递
        rtype:有返回值，返回值是响应报文"""
        global resp1
        if method.upper() == 'GET':
            try:
                resp1 = requests.get(url, params=param, cookies=cookies)
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper() == 'POST':
            try:
                resp1 = requests.post(url, data=param, cookies=cookies)
            except Exception as e:
                print('post方法出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp1 = None
        return resp1


if __name__ == '__main__':
    method = 'post'
    url = "http://192.168.114.130:8585/futureloan/mvc/api/member/register"
    param = {'mobilephone': '18300070752', 'pwd': '12345678', 'regname': '李大莉'}  # 大括号外面不加引号
    resp = HttpRequest().http_request(method, url, param, cookies=None)  # 这里测试代码需要拿到cookies,None会报错
    print(resp.text)
