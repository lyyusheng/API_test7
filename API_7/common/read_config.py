# 写配置文件格式
#   [section]
#   #注释（前面用井号）
#   option1=value1      #注意value不要加"",用“=”或者“：”都可以
#   ...

# 读配置文件  引入configparser模块，里面有很多类，其中一个类是Configparser
from configparser import ConfigParser  # 导入ConfigParser类
from API_test.API_7.common import project_path


# 创建对象

class ReadConfig:

    def __init__(self, file_name):
        self.cf = ConfigParser()
        # 第一步：打开文件 调用read()方法，源码里面调用的是open的
        self.cf.read(file_name, encoding='utf-8')  # 内容有中文时要设置encoding

    # 第二步：读取内容,读到的内容不管原来是什么类型，都变成字符串,openpyxl则不一样，数字还是数字，其他的变成字符串或者布尔型
    def get_str(self, section, option):
        value = self.cf.get(section, option)  # 第一种方法
        # res1=cf['StudentName']['stu_1'] #第二种方法
        return value
        # print(type(res))
        # print(type(eval(res)))#eval转换回原来的类型，但是原本就是字符串的，用了eval会报错。也可用于open

    # 想要读取特定数据类型，就要用特定函数
    def get_bool(self, section, option):
        """从配置文件获取bool"""
        value = self.cf.getboolean(section, option)
        return value

    def get_float(self, section, option):
        value = self.cf.getfloat(section, option)
        return value

    def get_int(self, section, option):
        value = self.cf.getint(section, option)
        return value

    def get_data(self, section, option):
        value = self.cf.get(section, option)
        return eval(value)  # eval()可以把value转回原来的数据类型
        # 但是注意，有个玩死人的大坑，配置文件中列表元素如果混入了中文的逗号，就会报错！！！！！


if __name__ == '__main__':
    res = ReadConfig(project_path.conf_path).get_data('CASE', 'case_id')
    print(res)
    print(type(res))
