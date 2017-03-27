import pymysql

class mysql_utils(object):
    def get_conn(host,username,password,database):
        conn = pymysql.connect(host,username,password,database,charset='utf8')
        return conn

    def insert(self,sql):
        try:
            cursor = mysql_utils.get_cursor(self)
            cursor.execute(sql)
        except:
            raise pymysql.Error
        finally:
            cursor.close()





