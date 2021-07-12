from django.db import models
import datetime

# Create your models here.
class Sites(models.Model):
    siteid = models.AutoField(db_column='SiteID', primary_key=True)  
    sitename = models.CharField(db_column='SiteName', max_length=100, blank=True, null=True) 
    create = models.DateTimeField(db_column='Create', default= datetime.datetime.now())
    userID = models.ForeignKey('user.user', on_delete=models.CASCADE, db_column='userID')

    def __str__(self):
        return self.sitename 

    class Meta:
        managed = True
        db_table = 'sites'
        ordering = ('siteid',)


class DesignCode(models.Model):
    designcodeid = models.AutoField(db_column='DesignCodeID', primary_key=True)  
    siteid = models.ForeignKey('Sites', on_delete=models.CASCADE, db_column='SiteID')
    designcode = models.CharField(db_column='DesignCode', max_length=100)  
    designcodeapp = models.CharField(db_column='DesignCodeApp', max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.designcode

    class Meta:
        managed = False
        db_table = 'design_code'
        ordering = ('designcodeid',)