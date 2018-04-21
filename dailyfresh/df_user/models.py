from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel


class User(AbstractUser, BaseModel):
    """用户"""
    class Meta:
        db_table = "df_users"

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 关系

    class Meta:
        db_table = 'df_areainfo'

class Address(BaseModel):
    """地址"""
    user = models.ForeignKey(User, verbose_name="所属用户")
    receiver_name = models.CharField(max_length=20, verbose_name="收件人")
    receiver_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    province=models.ForeignKey(AreaInfo,related_name='provice')
    city = models.ForeignKey(AreaInfo,related_name='city')
    district = models.ForeignKey(AreaInfo,related_name='district')
    detail_addr = models.CharField(max_length=256, verbose_name="详细地址")
    zip_code = models.CharField(max_length=6, verbose_name="邮政编码")

    class Meta:
        db_table = "df_address"
