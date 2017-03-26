import pymysql

class mysql_utils:
    def __init__(self, host='127.0.0.1', username='root', password='root', port='3306', database = ''):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database

    def get_cursor(self):
        conn = pymysql.connect(host=self.host,user=self.username,passwd=self.password,db=self.database,charset='utf8')
        cursor = conn.cursor()
        return cursor
    def insert(self,sql):
        try:
            cursor = mysql_utils.get_cursor(self)
            cursor.execute(sql)
        except:
            raise pymysql.Error
        finally:
            cursor.close()



