import  pymysql

def connDB():               #连接数据库
  conn=pymysql.connect(host="localhost",user="root",passwd="root",db="crawler_web");
  cur=conn.cursor();
  return (conn,cur);

def exeUpdate(conn,cur,sql):        #更新或插入操作
  sta=cur.execute(sql);
  conn.commit();
  return (sta);

def exeDelete(conn,cur,IDs):        #删除操作
  sta=0;
  for eachID in IDs.split(' '):
    sta+=cur.execute("delete from students where Id=%d"%(int(eachID)));
  conn.commit();
  return (sta);


def exeQuery(cur,sql):              #查询语句

    cur.execute(sql);

    return (cur);

def connClose(conn,cur):            #关闭所有连接

    cur.close()

    conn.close()