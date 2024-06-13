from tortoise import fields, models

from common.Table import Table


class User(Table):
    userAccount = fields.CharField(max_length=256, null=False, description="账号", index=True)
    userPassword = fields.CharField(max_length=512, null=False, description="密码")
    userName = fields.CharField(max_length=256, null=True, description="用户昵称")
    userAvatar = fields.CharField(max_length=1024, null=True, description="用户头像")
    userRole = fields.CharField(max_length=256, default="user", null=False, description="用户角色：user/admin")

    class Meta:
        table_description = "用户表"
        table = "user"