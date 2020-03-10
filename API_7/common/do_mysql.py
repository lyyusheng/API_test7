from mysql import connector
from API_7.common.read_config import ReadConfig
from API_7.common import project_path


class DoMysql:
    """操作数据库的类，专门用于数据库读取"""

    def do_mysql(self, query, flag):
        """
        query:sql查询语句
        flag:1表示获取第一条数据，2表示获取多条数据"""
        db_config = ReadConfig(project_path.conf_path).get_data('DB', 'db_config')
        cnn = connector.connect(**db_config)  # 建立连接
        cursor = cnn.cursor()
        cursor.execute(query)

        if flag == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res


if __name__ == '__main__':
    query = 'select * from member where MobilePhone=18300070752'
    res = DoMysql().do_mysql(query, 2)
    print('数据库的查询结果:{}'.format(res))