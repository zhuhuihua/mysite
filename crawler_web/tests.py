from django.test import TestCase

from mysqlUtil_ import insert
import time
import uuid

sql = 'insert into aa(name) VALUES ( "ggegee")'
insert(sql)
