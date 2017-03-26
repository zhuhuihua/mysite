from django.db import models
import pymysql
import uuid
# Create your models here.

class Task(models.Model):
    t_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    regex = models.TextField('规则')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_date = models.DateTimeField('修改时间', auto_now=True)

class User(models.Model):
    u_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField('姓名',max_length=64)
    password = models.CharField('密码',max_length=64)
    email = models.EmailField('邮箱',max_length=32)
    phone = models.IntegerField('电话')
    ip = models.CharField('用户ip',max_length=64)
    register_time = models.DateTimeField('注册时间',auto_now_add=True)
    Last_login_time = models.DateTimeField('最后登陆时间',auto_now=True)



