from django.db import models
import datetime

class Facility(models.Model):
    facilityid = models.AutoField(db_column='FacilityID', primary_key=True) 
    siteid = models.ForeignKey('siteApp.Sites', on_delete=models.CASCADE, db_column='SiteID')  
    facilityname = models.CharField(db_column='FacilityName', max_length=100) 
    managementfactor = models.FloatField(db_column='ManagementFactor')  
    create = models.DateTimeField(db_column='Created', default= datetime.datetime.now()) 
    time = models.DateTimeField(db_column='Time', default = datetime.datetime.now())
    def __str__(self):
        return self.facilityname
    class Meta:
        managed = True
        db_table = 'facility'
        ordering = ('facilityid',)