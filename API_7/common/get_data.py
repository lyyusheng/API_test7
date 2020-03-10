# 反射
import re

from API_7.common import read_config
from API_7.common import project_path

config = read_config.ReadConfig(project_path.conf_path)


class GetData:
    """类的反射可以动态的查看，增加，删除，更改类或者实例的属性"""
    COOKIE = None
    LOAN_ID = None  # 新添加的标id初始值
    normal_usr = config.get_str('data', 'normal_usr')
    normal_pwd = config.get_str('data', 'normal_pwd')
    normal_member_id = config.get_str('data', 'normal_member_id')


def replace(target):
    p2 = '#(.*?)#'
    while re.search(p2, target):
        m = re.search(p2, target)
        key = m.group(1)
        value = getattr(GetData, key)
        target = re.sub(p2, value, target, count=1)  # 正则表达式替换时要是str类型
    return target
