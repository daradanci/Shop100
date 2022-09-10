from django.db import models

# Create your models here.


class Range(models.Model):
    rangeid = models.AutoField(db_column='rangeId', primary_key=True)  # Field name made lowercase.
    rangename = models.CharField(db_column='rangeName', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'range'


class Shop100Range(models.Model):
    id = models.BigAutoField(primary_key=True)
    rangename = models.CharField(db_column='rangeName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop100_range'



class Models(models.Model):
    modelid = models.AutoField(db_column='modelId', primary_key=True)  # Field name made lowercase.
    idrange = models.ForeignKey('Range', models.DO_NOTHING, db_column='idRange')  # Field name made lowercase.
    modelname = models.CharField(db_column='modelName', unique=True, max_length=30)  # Field name made lowercase.
    producer = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'models'



class Stock(models.Model):
    itemid = models.AutoField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    idmodel = models.ForeignKey(Models, models.DO_NOTHING, db_column='idModel')  # Field name made lowercase.
    size = models.CharField(max_length=4)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('idmodel', 'size'),)

