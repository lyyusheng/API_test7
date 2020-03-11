import unittest
from API_7.common.do_excel import DoExcel
from API_7.common import project_path
from API_7.common.http_request import HttpRequest
from API_7.common.my_log import MyLog
from API_7.common.get_data import GetData
from ddt import ddt, unpack, data
from API_7.common.do_pymysql import DoMysql

# 这是获取cookies的第二种方法，使用映射获取cookies，不用全局变量
# 发起测试
my_log = MyLog()
test_data = DoExcel(project_path.case_path, 'recharge').read_case('RechargeCase')
TestResult = None  # 声明一些，颜色不一样看着烦
null = None  # 为了解决出现“NameError: name ‘null’ is not defined”
print(test_data)


@ddt
class TestCase(unittest.TestCase):  # 光标要移到最底下执行
    def setUp(self):  # 每條用例執行之前執行
        self.t = DoExcel(project_path.case_path, 'recharge')  # 赋值给对象属性self.t,在整个类里面都可以调用
        print('開始執行新一條測試了')  # 準備工作

    def tearDown(self):  # 每條用例執行之後執行
        print('一條測試用例執行完畢')  # 清場工作，把占用的環境資源關掉

    @data(*test_data)
    def test_send_request(self, case):
        global TestResult, null
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])  # 讀出來是個字符串，必須eval()變回原來字典類型
        my_log.info('-----正在测试{}模块里面第{}条测试用例：{},'.format(case['Module'], case['CaseId'], case['Title']))
        my_log.info('测试数据是：{}'.format(case['Params']))

        # 查询数据库获得充值前余额，取第一个
        if case['sql'] is not None:
            sql = eval(case['sql'])['sql']
            before_amount = DoMysql().do_pymysql(sql, 1)[0]

        resp = HttpRequest().http_request(method, url, param,
                                          cookies=getattr(GetData, 'COOKIE'))  # 类的反射可以动态的查看，增加，删除，更改类或者实例的属性（COOKIES）
        if resp.cookies:  # 如果存在cookies,则进去更新COOKIES，因为声明过全局变量，所以上面COOKIES=None也会被更新
            setattr(GetData, 'COOKIE', resp.cookies)

        # 查询数据库获得投资后的余额，取第一个
        if case['sql'] is not None:
            sql = eval(case['sql'])['sql']
            after_amount = DoMysql().do_pymysql(sql, 1)[0]
            recharge_amount = int(param['amount'])
            expect_amount = before_amount + recharge_amount
            self.assertEqual(expect_amount, after_amount)

        if case['ExpectedResult'].find('exp_amount') > -1:   # 期望值存在'exp_amount'时要进行期望值替换
            case['ExpectedResult'] = case['ExpectedResult'].replace('exp_amount', str(expect_amount))

        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())
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
