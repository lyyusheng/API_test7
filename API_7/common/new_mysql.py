from mysql import connector

db_config = {'host': '47.107.168.87',
             'user': 'python',
             'password': 'python666',
             'port': 3306,
             'database': 'future'}
cnn = connector.connect(**db_config)
cursor = cnn.cursor()
query = 'select * from member where MobilePhone=13700000356'
cursor.execute(query)
res = cursor.fetchall()
print(res)
