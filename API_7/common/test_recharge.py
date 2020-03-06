import unittest
import json
import warnings  # 解决出现“ResourceWarning: Enable tracemalloc to get the object allocation traceback”
from API_test.API_7.common.do_excel import DoExcel
from API_test.API_7.common import project_path
from API_test.API_7.common.http_request import HttpRequest
from API_test.API_7.common.my_log import MyLog
from ddt import ddt, unpack, data

# 这是第一种获取cookies的方式，设置全局变量
my_log = MyLog()
test_data = DoExcel(project_path.case_path, 'recharge').read_case('RechargeCase')
COOKIES = None
TestResult = None
null = None  # 为了解决出现“NameError: name ‘null’ is not defined”


@ddt
class TestCase(unittest.TestCase):  # 光标要移到最底下执行
    def setUp(self):  # 每條用例執行之前執行
        warnings.simplefilter("ignore",
                              ResourceWarning)  # 为解决出现“ResourceWarning: Enable tracemalloc to get the object allocation traceback”
        self.t = DoExcel(project_path.case_path, 'recharge')  # 赋值给对象属性self.t,在整个类里面都可以调用
        print('開始執行新一條測試了')  # 準備工作

    def tearDown(self):  # 每條用例執行之後執行
        print('一條測試用例執行完畢')  # 清場工作，把占用的環境資源關掉

    @data(*test_data)
    def test_send_request(self, case):
        global COOKIES, TestResult, null  # 声明为全局变量

        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])  # 讀出來是個字符串，必須eval()變回原來字典類型
        my_log.info('-----正在测试{}模块里面第{}条测试用例：{},'.format(case['Module'], case['CaseId'], case['Title']))
        my_log.info('测试数据是：{}'.format(case['Params']))
        resp = HttpRequest().http_request(method, url, param, COOKIES)  # 注意是cookies还是COOKIES
        if resp.cookies:  # 如果存在cookies,则进去更新COOKIES，因为声明过全局变量，所以上面COOKIES=None也会被更新
            COOKIES = resp.cookies
            print("cookies是:{}".format(COOKIES))
        else:
            print("没有cookies")
        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())  # 本来是用eval（）,但是出现“NameError: name
            # ‘null’ is not defined”，换成json.loads()可以解决，但是json.loads()不支持单引号''必须用双引号""
            TestResult = "Pass"  # 上面断言成功才会进这里
        except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('http请求出错了，错误是：{}'.format(e))
            raise e  # 抛出错误，否则测试报告那里全部都是通过
        finally:
            self.t.write_back(case['CaseId'] + 1, 9, resp.text)  # 写回实际结果字符串类型不能用json，参数：行 列 实际结果
            self.t.write_back(case['CaseId'] + 1, 10, TestResult)
            # 涉及excel写操作的必须手动关闭excel，否则会出现些奇怪的问题
        my_log.info('实际结果是:{}'.format(resp.json()))
