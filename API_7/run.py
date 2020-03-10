import sys
sys.path.append('./')
print(sys.path)
from API_7.common import project_path
from API_7.common import test_recharge
from API_7.common import test_register
from API_7.common import test2_recharge
from API_7.test_case import old_test_addloan, test_invest
import unittest
import HTMLTestRunnerNew


# 新建测试集
suite = unittest.TestSuite()

# 添加用例
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test2_recharge))
# suite.addTest(loader.loadTestsFromModule(old_test_addloan))
suite.addTest(loader.loadTestsFromModule(test_invest))

# 执行测试用例
with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="2020年2月份API_6测试用例",
                                              description='温习时写的',
                                              tester='liyusheng')
    runner.run(suite)  # 执行用例（容易忘记,不写的话测试报告会空白.）
