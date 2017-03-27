from django.test import TestCase

import mysqlUtil
import time
import uuid

conn = mysqlUtil.mysql_utils.get_conn('localhost','root','123456','crawler_web')
sql = 'insert into aa(name) VALUES ( "ggegee")'
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
