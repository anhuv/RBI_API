from django.db import models
import datetime

class EquipmentMaster(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  
    equipmentnumber = models.CharField(db_column='EquipmentNumber', max_length=100)  
    equipmenttypeid = models.ForeignKey('equipment.EquipmentType', on_delete=models.CASCADE, db_column='EquipmentTypeID')  
    equipmentname = models.CharField(db_column='EquipmentName', max_length=150, blank=True, null=True)  
    commissiondate = models.DateTimeField(db_column='CommissionDate')  
    designcodeid = models.ForeignKey('siteApp.DesignCode', on_delete=models.CASCADE, db_column='DesignCodeID')  
    siteid = models.ForeignKey('siteApp.Sites', on_delete=models.CASCADE, db_column='SiteID')  
    facilityid = models.ForeignKey('facility.Facility', on_delete=models.CASCADE, db_column='FacilityID')  
    # manufacturerid = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, db_column='ManufacturerID')  
    pfdno = models.CharField(db_column='PFDNo', max_length=100, blank=True, null=True)  
    processdescription = models.CharField(db_column='ProcessDescription', max_length=250, blank=True, null=True)  
    equipmentdesc = models.CharField(db_column='EquipmentDesc', max_length=250, blank=True, null=True)  
    create = models.DateTimeField(db_column='Created', default= datetime.datetime.now())
    time = models.DateTimeField(db_column='Time', default=datetime.datetime.now())
    def __str__(self):
        return self.equipmentnumber

    class Meta:
        managed = False
        db_table = 'equipment_master'
        ordering = ('equipmentid',)

class EquipmentType(models.Model):
    equipmenttypeid = models.IntegerField(db_column='EquipmentTypeID', primary_key=True)  
    equipmenttypecode = models.CharField(db_column='EquipmentTypeCode', max_length=50, blank=True, null=True)  
    equipmenttypename = models.CharField(db_column='EquipmentTypeName', max_length=50, blank=True, null=True)  

    def __str__(self):
        return self.equipmenttypename

    class Meta:
        managed = False
        db_table = 'equipment_type'
        ordering = ('equipmenttypeid',) 