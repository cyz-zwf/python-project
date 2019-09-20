# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MfCart(models.Model):
    cid = models.AutoField(primary_key=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mf_cart'


class MfCartDetail(models.Model):
    did = models.AutoField(primary_key=True)
    cartid = models.IntegerField(db_column='cartId', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='productId', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_cart_detail'


class MfNews(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    pubtime = models.BigIntegerField(db_column='pubTime', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_news'


class MfProduct(models.Model):
    pid = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=64, blank=True, null=True)
    title2 = models.CharField(max_length=64, blank=True, null=True)
    pic = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    func = models.CharField(max_length=64, blank=True, null=True)
    noise = models.CharField(max_length=64, blank=True, null=True)
    wind = models.CharField(max_length=64, blank=True, null=True)
    applyto = models.CharField(db_column='applyTo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(max_length=64, blank=True, null=True)
    level = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    detail = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_product'


class MfUser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32, blank=True, null=True)
    upwd = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_user'
