from django.test import TestCase

from mysqlUtil import *
import time
from uuid import uuid4

mysql_util = mysql_utils(host='localhost', username='root', password='root', port=3306, database='crawler_web')
sql = 'insert into crawler_web_task(t_id, regex) VALUES (uuid.uuid4(), "")'
mysql_util.insert(sql)
