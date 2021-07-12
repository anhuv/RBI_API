from django.db import models
import datetime

class InspecPlan(models.Model):
    id = models.AutoField(primary_key=True,db_column='PlanID')
    siteid = models.ForeignKey('siteApp.ites', on_delete=models.CASCADE, db_column='SiteID')
    inspectionplanname = models.CharField(db_column='InspPlanName', blank=True, max_length=150)
    inspectionplandate = models.DateTimeField(db_column='InspPlanDate', blank=True, null=True)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'inspection_plan'
        ordering = ('id',)

class InspectionCoverage(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null= False, db_column='ID')
    planid = models.ForeignKey('InspecPlan',db_column='PlanID', on_delete=models.CASCADE, blank=True, null=True)
    equipmentid = models.ForeignKey('equipment.EquipmentMaster', db_column='EquipmentID', on_delete=models.CASCADE, blank=True, null=True)
    componentid = models.ForeignKey('component.ComponentMaster', db_column='ComponentID', on_delete=models.CASCADE, blank=True, null=True)
    proposalid = models.ForeignKey('proposal.RwAssessment', db_column='ProposalID', on_delete=models.CASCADE, blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', blank=True, max_length=250, null=True)
    findings = models.TextField(db_column='Findings',blank=True, null=True)
    findingrtf = models.TextField(db_column='FindingRTF', blank=True, null=True)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'inspection_coverage'
        ordering = ('id',)

class IMType(models.Model):
    imtypeid = models.IntegerField(db_column='IMTypeID',primary_key=True)
    imitemid = models.ForeignKey('IMItem', db_column='IMItemID', on_delete=models.CASCADE, blank=True, null=True)
    imtypename = models.CharField(db_column='IMTypeName', blank=True, max_length=100)
    imtypecode = models.CharField(db_column='IMTypeCode', blank=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'im_type'
        ordering = ('imtypeid',)

class IMItem(models.Model):
    imitemid = models.IntegerField(primary_key=True, db_column='IMItemID')
    imdescription = models.CharField(db_column='IMDescription', blank=True, max_length=100)
    imcode = models.CharField(db_column='IMCode', blank=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'im_items'
        ordering = ('imitemid',)

class DMCategory(models.Model):
    dmcategoryid = models.IntegerField(db_column='DMCategoryID', blank=True, null=True)
    dmcategoryname = models.CharField(db_column='DMCategoryName', blank=True, null=True, max_length=100)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'dm_category'

class DMItems(models.Model):
    dmitemid = models.IntegerField(primary_key=True, db_column='DMItemID')
    dmdescription = models.CharField(db_column='DMDescription', max_length=250, blank=True)
    dmseq = models.IntegerField(db_column='DMSeq', blank=True, null=True)
    dmcategoryid = models.IntegerField(db_column='DMCategoryID', blank=True, null=True)
    dmcode = models.CharField(db_column='DMCode', max_length=50)
    hasdf = models.IntegerField(db_column='HasDF', blank=True, null=True)
    hasrule = models.IntegerField(db_column='HasRule', blank=True, null=True)
    failuremode = models.CharField(db_column='FailureMode', max_length=50)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'dm_items'

class InspectionCoverageDetail(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='ID')
    coverageid = models.ForeignKey('InspectionCoverage',db_column="CoverageID", on_delete=models.CASCADE, blank=True, null=True)
    dmitemid = models.ForeignKey('DMItems', db_column='DMItemID', on_delete=models.CASCADE, blank=True, null=True )
    inspectiondate = models.DateTimeField(db_column='InspectionDate', blank=True, null=True)
    effcode = models.CharField(db_column='EffectivenessCode',max_length=50, blank=True, null=True)
    inspsummary = models.CharField(db_column='InspectionSummary',max_length=500, blank=True, null=True)
    iscarriedout = models.IntegerField(db_column='IsCarriedOut', blank=True, null=True)
    carriedoutdate = models.DateTimeField(db_column='CarriedOutDate', blank=True, null=True)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'inspection_coverage_detail'

class InspectionDMRule(models.Model):
    dmitemid = models.ForeignKey('DmItems', db_column='DMItemID', on_delete=models.CASCADE, primary_key=True )
    imitemid = models.ForeignKey('IMItem', db_column='IMItemID', on_delete=models.CASCADE, blank=True, null=True)
    imtypeid = models.ForeignKey('IMType', db_column='IMTypeID', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'inspection_dm_rule'

class InspectionTechnique(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='ID')
    coverageid = models.ForeignKey('InspectionCoverage',db_column="CoverageID", on_delete=models.CASCADE, blank=True, null=True)
    imitemid = models.ForeignKey('IMItem', db_column='IMItemID', on_delete=models.CASCADE, blank=True, null=True)
    imtypeid = models.ForeignKey('IMType', db_column='IMTypeID', on_delete=models.CASCADE, blank=True, null=True)
    inspectiontype = models.IntegerField(db_column='InspectionType', blank=True, null=True)
    coverage = models.IntegerField(db_column='Coverage', blank=True, null=True,default=0)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())
    class Meta:
        managed = False
        db_table = 'inspection_detail_technique'

class RwInspectionDetail(models.Model):
    id = models.IntegerField(blank=True, null=True, db_column='ID')
    detailid = models.AutoField(db_column='DetailID', blank=True, null=False, primary_key=True)
    equipmentid = models.IntegerField(db_column='EquipmentID', blank=True, null=True)
    componentid = models.IntegerField(db_column='ComponentID', blank=True, null=True)
    coverageiddetail = models.IntegerField(db_column='Coverage_DetailID', blank=True, null=True)
    inspplanname = models.CharField(db_column='InspPlanName', blank=True, null=True, max_length=150)
    inspectiondate = models.DateTimeField(db_column='InspectionDate',blank=True, null=True )
    dmitemid = models.IntegerField(db_column='DMItemID', blank=True, null=True)
    effcode = models.CharField(db_column='EffectivenessCode', max_length=50, blank=True, null=True)
    inspsum = models.CharField(db_column='InspectionSummary', blank=True, null=True, max_length=500)
    iscarriedout = models.IntegerField(db_column='IsCarriedOut', blank=True, null=True)
    carriedoutdate = models.DateTimeField(db_column='CarriedOutDate', blank=True, null=True)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'rw_inspection_detail'
