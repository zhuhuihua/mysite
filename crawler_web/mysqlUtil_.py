import pymysql

def get_conn(host,user,password,db):
        conn = pymysql.connect(host,user,password,db,charset='utf8')
        print(conn)
        return conn
def insert(sql):
    try:
        conn = get_conn('localhost','root','123456','crawler_web')
        cur = conn.cursor()
        print(cur)
        cur.execute(sql)
        conn.commit()
    except:
        raise pymysql.Error
    finally:
        cur.close()



