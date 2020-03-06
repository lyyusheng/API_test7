import os

project_path1 = os.path.realpath(__file__)
# print(project_path1)
project_path2 = os.path.split(os.path.realpath(__file__))[0]
# print(project_path2)
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path2)

# 测试用例的路径是：
case_path = os.path.join(project_path, 'test_case', 'api_case_1.xlsx')

# 测试报告的路径
report_path = os.path.join(project_path, 'test_result', 'test_report.html')

# 日志的路径
log_path = os.path.join(project_path, 'test_result', 'test_log', 'test.log')

# 配置文件的路径
conf_path = os.path.join(project_path, 'conf', 'case.conf')
if __name__ == '__main__':
    print('project_path是:', project_path)
    print('测试用例路径是：', case_path)
    print('测试报告的路径是：', report_path)
