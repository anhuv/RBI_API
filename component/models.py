from django.db import models
import datetime

class ComponentMaster(models.Model):
    componentid = models.AutoField(db_column='ComponentID', primary_key=True)  # Field name made lowercase.
    componentnumber = models.CharField(db_column='ComponentNumber', max_length=100)  # Field name made lowercase.
    equipmentid = models.ForeignKey('equipment.EquipmentMaster', on_delete=models.CASCADE, db_column='EquipmentID')  # Field name made lowercase.
    componenttypeid = models.ForeignKey('ComponentType', on_delete=models.CASCADE, db_column='ComponentTypeID')  # Field name made lowercase.
    componentname = models.CharField(db_column='ComponentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    componentdesc = models.CharField(db_column='ComponentDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isequipmentlinked = models.IntegerField(db_column='IsEquipmentLinked', default=0)  # Field name made lowercase.
    apicomponenttypeid = models.IntegerField(db_column='APIComponentTypeID')  # Field name made lowercase.
    risktarget = models.FloatField(db_column='RiskTarget', default=0)
    create = models.DateTimeField(db_column='Created', default=datetime.datetime.now())
    time = models.DateTimeField(db_column='Time', default=datetime.datetime.now())
    class Meta:
        managed = False
        db_table = 'component_master'
        ordering = ('componentid',)


class ComponentType(models.Model):
    componenttypeid = models.IntegerField(db_column='ComponentTypeID', primary_key=True)  # Field name made lowercase.
    componenttypename = models.CharField(db_column='ComponentTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    componenttypecode = models.CharField(db_column='ComponentTypeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shapefactor = models.FloatField(db_column='ShapeFactor', blank=True,null=True)

    def __str__(self):
        return self.componenttypename
    class Meta:
        managed = False
        db_table = 'component_type'
        ordering = ('componenttypeid',)


