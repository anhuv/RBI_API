from django.db import models
import datetime

# bo sung bang rwcatank 30/11/2019
class RwCaTank(models.Model):
    id= models.ForeignKey('RwAssessment', on_delete=models.CASCADE, db_column='ID',primary_key=True)
    hydraulic_water =  models.FloatField(db_column='Hydraulic_Water', blank=True,null=True,default=0)
    hydraulic_fluid = models.FloatField(db_column='Hydraulic_Fluid', blank=True,null=True,default=0)
    seepage_velocity = models.FloatField(db_column='Seepage_Velocity', blank=True,null=True,default=0)
    flow_rate_d1 = models.FloatField(db_column='Flow_Rate_D1', blank=True,null=True,default=0)
    flow_rate_d2 = models.FloatField(db_column='Flow_Rate_D2', blank=True, null=True,default=0)
    flow_rate_d3 = models.FloatField(db_column='Flow_Rate_D3', blank=True, null=True,default=0)
    flow_rate_d4 = models.FloatField(db_column='Flow_Rate_D4', blank=True, null=True,default=0)
    leak_duration_d1 = models.FloatField(db_column='Leak_Duration_D1', blank=True, null=True,default=0)
    leak_duration_d2 = models.FloatField(db_column='Leak_Duration_D2', blank=True, null=True,default=0)
    leak_duration_d3 = models.FloatField(db_column='Leak_Duration_D3', blank=True, null=True,default=0)
    leak_duration_d4 = models.FloatField(db_column='Leak_Duration_D4', blank=True, null=True,default=0)
    release_volume_leak_d1 = models.FloatField(db_column='Release_Volume_Leak_D1', blank=True, null=True,default=0)
    release_volume_leak_d2 = models.FloatField(db_column='Release_Volume_Leak_D2', blank=True, null=True,default=0)
    release_volume_leak_d3 = models.FloatField(db_column='Release_Volume_Leak_D3', blank=True, null=True,default=0)
    release_volume_leak_d4 = models.FloatField(db_column='Release_Volume_Leak_D4', blank=True, null=True,default=0)
    release_volume_rupture = models.FloatField(db_column='Release_Volume_Rupture', blank=True, null=True,default=0)
    liquid_height = models.FloatField(db_column='Liquid_Height', blank=True, null=True,default=0)
    volume_fluid = models.FloatField(db_column='Volume_Fluid', blank=True, null=True,default=0)
    time_leak_ground = models.FloatField(db_column='Time_Leak_Ground', blank=True, null=True,default=0)
    volume_subsoil_leak_d1 = models.FloatField(db_column='Volume_SubSoil_Leak_D1', blank=True, null=True,default=0)
    volume_subsoil_leak_d4 = models.FloatField(db_column='Volume_SubSoil_Leak_D4', blank=True, null=True,default=0)
    volume_ground_water_leak_d1 = models.FloatField(db_column='Volume_Ground_Water_Leak_D1', blank=True, null=True,default=0)
    volume_ground_water_leak_d4 = models.FloatField(db_column='Volume_Ground_Water_Leak_D4', blank=True, null=True,default=0)
    barrel_dike_rupture = models.FloatField(db_column='Barrel_Dike_Rupture', blank=True, null=True,default=0)
    barrel_dike_leak = models.FloatField(db_column='Barrel_Dike_Leak', blank=True, null=True,default=0)
    barrel_onsite_leak = models.FloatField(db_column='Barrel_Onsite_Leak', blank=True, null=True,default=0)
    barrel_onsite_rupture = models.FloatField(db_column='Barrel_Onsite_Rupture', blank=True, null=True,default=0)
    barrel_offsite_leak = models.FloatField(db_column='Barrel_Offsite_Leak', blank=True, null=True,default=0)
    barrel_dike_leak = models.FloatField(db_column='Barrel_Dike_Leak', blank=True, null=True,default=0)
    barrel_offsite_rupture = models.FloatField(db_column='Barrel_Offsite_Rupture', blank=True, null=True,default=0)
    barrel_water_leak = models.FloatField(db_column='Barrel_Water_Leak', blank=True, null=True,default=0)
    barrel_water_rupture = models.FloatField(db_column='Barrel_Water_Rupture', blank=True, null=True,default=0)
    fc_environ_leak = models.FloatField(db_column='FC_Environ_Leak', blank=True, null=True,default=0)
    fc_environ_rupture = models.FloatField(db_column='FC_Environ_Rupture', blank=True, null=True,default=0)
    fc_environ = models.FloatField(db_column='FC_Environ', blank=True, null=True,default=0)
    material_factor = models.FloatField(db_column='Material_Factor', blank=True, null=True,default=0)
    fc_environ = models.FloatField(db_column='FC_Environ', blank=True, null=True,default=0)
    component_damage_cost = models.FloatField(db_column='Component_Damage_Cost', blank=True, null=True,default=0)
    damage_surrounding_equipment_cost = models.FloatField(db_column='Damage_Surrounding_Equipment_Cost', blank=True, null=True, default=0)
    associated_personnel_injury_cost = models.FloatField(db_column='Associated_Personnel_Injury_Cost', blank=True,null=True, default=0)
    business_cost = models.FloatField(db_column='Business_Cost', blank=True, null=True,default=0)
    consequence = models.FloatField(db_column='Consequence', blank=True, null=True,default=0)
    consequencecategory = models.CharField(db_column='ConsequenceCategory', max_length=150, blank=True, null=True,default=0)
    class Meta:
        managed = False
        db_table = 'rw_ca_tank'
        ordering = ('id',)

class RwAssessment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey('equipment.EquipmentMaster', on_delete=models.CASCADE, db_column='EquipmentID')  # Field name made lowercase.
    componentid = models.ForeignKey('component.ComponentMaster', on_delete=models.CASCADE, db_column='ComponentID')  # Field name made lowercase.
    assessmentdate = models.DateTimeField(db_column='AssessmentDate', blank=True, null=True)  # Field name made lowercase.
    commisstiondate = models.DateTimeField(db_column='CommisstionDate', blank=True, null=True)  # Field name made lowercase.
    riskanalysisperiod = models.IntegerField(db_column='RiskAnalysisPeriod')  # Field name made lowercase.
    isequipmentlinked = models.IntegerField(db_column='IsEquipmentLinked', default=0)  # Field name made lowercase.
    proposalname = models.CharField(db_column='ProposalName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create = models.DateTimeField(db_column='Created', default= datetime.datetime.now())
    assessmentmethod = models.CharField(db_column='AssessmentMethod', max_length=100, blank=True,null=True)

    def __str__(self):
        return self.proposalname

    class Meta:
        managed = False
        db_table = 'rw_assessment'
        ordering = ('id',)
        get_latest_by = 'id'

class RwCaLevel1(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    release_phase = models.CharField(db_column='Release_Phase', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fact_di = models.FloatField(blank=True, null=True,default=0)
    fact_mit = models.FloatField(blank=True, null=True,default=0)
    fact_ait = models.FloatField(blank=True, null=True,default=0)
    ca_cmd = models.FloatField(db_column='CA_cmd', blank=True, null=True,default=0)  # Field name made lowercase.
    ca_inj_flame = models.FloatField(db_column='CA_inj_flame', blank=True, null=True,default=0)  # Field name made lowercase.
    ca_inj_toxic = models.FloatField(db_column='CA_inj_toxic', blank=True, null=True,default=0)  # Field name made lowercase.
    ca_inj_ntnf = models.FloatField(db_column='CA_inj_ntnf', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_cmd = models.FloatField(db_column='FC_cmd', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_affa = models.FloatField(db_column='FC_affa', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_prod = models.FloatField(db_column='FC_prod', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_inj = models.FloatField(db_column='FC_inj', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_envi = models.FloatField(db_column='FC_envi', blank=True, null=True,default=0)  # Field name made lowercase.
    fc_total = models.FloatField(db_column='FC_total', blank=True, null=True,default=0)  # Field name made lowercase.
    fcof_category = models.CharField(db_column='FCOF_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_final = models.FloatField(db_column='CA_final', blank=True, null=True,default=0)
    auto_ignition = models.FloatField(db_column='auto_ignition', blank=True, null=True,default=0)
    ideal_gas = models.FloatField(db_column='ideal_gas', blank=True, null=True,default=0)
    ideal_gas_ratio = models.FloatField(db_column='ideal_gas_ratio', blank=True, null=True,default=0)
    liquid_density = models.FloatField(db_column='liquid_density', blank=True, null=True,default=0)
    ambient = models.CharField(db_column='ambient', blank=True, null=True, max_length=50)
    mw = models.FloatField(db_column='mw', blank=True, null=True,default=0)
    nbp = models.FloatField(db_column='NBP', blank=True, null=True,default=0)
    model_fluid_type = models.CharField(db_column='model_fluid_type', max_length=40, blank=True, null=True)
    toxic_fluid_type = models.CharField(db_column='toxic_fluid_type', max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ca_level1'
        ordering = ('id',)

class RwCoating(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    externalcoating = models.IntegerField(db_column='ExternalCoating',default=0, blank=True, null=True)  # Field name made lowercase.
    externalinsulation = models.IntegerField(db_column='ExternalInsulation',default=0, blank=True, null=True)  # Field name made lowercase.
    internalcladding = models.IntegerField(db_column='InternalCladding',default=0, blank=True, null=True)  # Field name made lowercase.
    internalcoating = models.IntegerField(db_column='InternalCoating',default=0, blank=True, null=True)  # Field name made lowercase.
    internallining = models.IntegerField(db_column='InternalLining',default=0, blank=True, null=True)  # Field name made lowercase.
    externalcoatingdate = models.DateTimeField(db_column='ExternalCoatingDate', blank=True, null=True)  # Field name made lowercase.
    externalcoatingquality = models.CharField(db_column='ExternalCoatingQuality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    externalinsulationtype = models.CharField(db_column='ExternalInsulationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulationcondition = models.CharField(db_column='InsulationCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulationcontainschloride = models.IntegerField(db_column='InsulationContainsChloride',default=0, blank=True, null=True)  # Field name made lowercase.
    internallinercondition = models.CharField(db_column='InternalLinerCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    internallinertype = models.CharField(db_column='InternalLinerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    claddingcorrosionrate = models.FloatField(db_column='CladdingCorrosionRate', blank=True, null=True,default=0)  # Field name made lowercase.
    supportconfignotallowcoatingmaint = models.IntegerField(db_column='SupportConfigNotAllowCoatingMaint',default=0, blank=True, null=True)  # Field name made lowercase.
    claddingthickness = models.FloatField(db_column='CladdingThickness', blank=True,null=True,default=0)

    class Meta:
        managed = False
        db_table = 'rw_coating'
        ordering = ('id',)


class CofFluid(models.Model):
    cofluidid = models.AutoField(db_column='COFFluidID',primary_key=True)
    coffluid = models.CharField(db_column='COFFluid' , max_length=250, null=True)
    alisaname = models.CharField(db_column='AliasName' , max_length=250, null=True)
    examplesofapplicable = models.CharField(db_column='ExamplesOfApplicable' , max_length=250, null=True)
    fluidtype = models.IntegerField(db_column='FluidType', null=True)
    mw = models.FloatField(db_column='MW', null=True)
    nbp = models.FloatField(db_column='NBP', null=True)
    density = models.FloatField(db_column='Density', null=True)
    heatequation = models.IntegerField(db_column='HeatEquation', null=True)
    idealconstana = models.FloatField(db_column='IdealConstantA', null=True)
    idealconstantb = models.FloatField(db_column='IdealConstantB', null=True)
    idealconstantc = models.FloatField(db_column='IdealConstantC', null=True)
    idealconstand = models.FloatField(db_column='IdealConstantD', null=True)
    idealconstane = models.FloatField(db_column='IdealConstantE', null=True)
    ambienstate = models.IntegerField(db_column='AmbientState', null=False)
    autoignitiontemperature = models.IntegerField(db_column='AutoIgnitionTemperature', null=True)
    k = models.FloatField(db_column='K', null=True)
    flammable = models.BooleanField(db_column='Flammable', default=1,null=False)
    toxic = models.BooleanField(db_column='Toxic', default=1,null=False)
    created = models.DateTimeField(db_column='Created', default=datetime.datetime.now())


    class Meta:
        managed = False
        db_table = 'cof_fluid'
        ordering = ('cofluidid',)

class RwComponent(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    nominaldiameter = models.FloatField(db_column='NominalDiameter', blank=True, null=True,default=0)  # Field name made lowercase.
    nominalthickness = models.FloatField(db_column='NominalThickness', blank=True, null=True,default=0)  # Field name made lowercase.
    currentthickness = models.FloatField(db_column='CurrentThickness', blank=True, null=True,default=0)  # Field name made lowercase.
    minreqthickness = models.FloatField(db_column='MinReqThickness', blank=True, null=True,default=0)  # Field name made lowercase.
    currentcorrosionrate = models.FloatField(db_column='CurrentCorrosionRate', blank=True, null=True,default=0)  # Field name made lowercase.
    branchdiameter = models.CharField(db_column='BranchDiameter', max_length=50, blank=True, null=True,default=0)  # Field name made lowercase.
    branchjointtype = models.CharField(db_column='BranchJointType', max_length=50, blank=True, null=True,default=0)  # Field name made lowercase.
    brinnelhardness = models.CharField(db_column='BrinnelHardness', max_length=50, blank=True, null=True,default=0)  # Field name made lowercase.
    chemicalinjection = models.IntegerField(db_column='ChemicalInjection', default=0, blank=True, null=True)  # Field name made lowercase.
    highlyinjectioninsp = models.IntegerField(db_column='HighlyInjectionInsp', default=0, blank=True, null=True)  # Field name made lowercase.
    complexityprotrusion = models.CharField(db_column='ComplexityProtrusion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    correctiveaction = models.CharField(db_column='CorrectiveAction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crackspresent = models.IntegerField(db_column='CracksPresent', default=0, blank=True, null=True)  # Field name made lowercase.
    cyclicloadingwitin15_25m = models.CharField(db_column='CyclicLoadingWitin15_25m', max_length=50, blank=True, null=True)  # Field name made lowercase.
    damagefoundinspection = models.IntegerField(db_column='DamageFoundInspection',default=0, blank=True, null=True)  # Field name made lowercase.
    deltafatt = models.FloatField(db_column='DeltaFATT', blank=True, null=True,default=0)  # Field name made lowercase.
    numberpipefittings = models.CharField(db_column='NumberPipeFittings', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pipecondition = models.CharField(db_column='PipeCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    previousfailures = models.CharField(db_column='PreviousFailures', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shakingamount = models.CharField(db_column='ShakingAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shakingdetected = models.IntegerField(db_column='ShakingDetected',default=0, blank=True, null=True)  # Field name made lowercase.
    shakingtime = models.CharField(db_column='ShakingTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shellheight = models.FloatField(db_column='ShellHeight', blank=True, null=True,default=0)  # Field name made lowercase.
    releasepreventionbarrier = models.IntegerField(db_column='ReleasePreventionBarrier',default=0, blank=True, null=True)  # Field name made lowercase.
    concretefoundation = models.IntegerField(db_column='ConcreteFoundation',default=0, blank=True, null=True)  # Field name made lowercase.
    severityofvibration = models.CharField(db_column='SeverityOfVibration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weldjointefficiency = models.FloatField(db_column='WeldJointEfficiency', blank=True,null=True,default=0)
    allowablestress = models.FloatField(db_column='AllowableStress', blank=True,null=True,default=0)
    structuralthickness = models.FloatField(db_column='StructuralThickness', blank=True,null=True,default=0)
    crackscurrentcondition = models.CharField(db_column='CracksCurrentCondition', blank=True,null=True, max_length=100)
    componentvolume = models.FloatField(db_column='ComponentVolume', blank=True,null=True,default=0)
    minstructuralthickness = models.IntegerField(db_column='MinimumStructuralThicknessGoverns',default=0, blank=True,null=True)
    hthadamage = models.IntegerField(db_column='HTHADamageObserved',default=0, blank=True,null=True)
    fabricatedsteel= models.IntegerField(db_column='FabricatedSteel',default=0, blank=True,null=True)
    equipmentsatisfied = models.IntegerField(db_column='EquipmentSatisfied', blank=True,null=True)
    nominaloperatingconditions = models.IntegerField(db_column='NominalOperatingConditions', blank=True,null=True)
    cetgreaterorequal = models.IntegerField(db_column='CETGreaterOrEqual',default=0, blank=True, null=True)
    cyclicservice = models.IntegerField(db_column='CyclicServiceFatigueVibration',default=0, blank=True,null=True)
    equipmentcircuitshock = models.IntegerField(db_column='EquipmentCircuitShock',default=0, blank=True,null=True)
    confidencecorrosionrate = models.CharField(db_column='ConfidenceCorrosionRate',max_length=50,blank=True,null=True)
    brittlefracturethickness = models.FloatField(db_column='BrittleFractureThickness', blank=True,null=True,default=0)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'rw_component'
        ordering = ('id',)

class CorrosionRateTank(models.Model):
    id = models.ForeignKey('RwAssessment', on_delete=models.CASCADE, db_column='ID')
    corrosionid = models.AutoField(db_column='CorrosionID', primary_key=True)
    soilsidecorrosionrate = models.FloatField(db_column='SoilSideCorrosionRate', null=True)
    productsidecorrosionrate = models.FloatField(db_column='ProductSideCorrosionRate', null=True)
    potentialcorrosion = models.CharField(db_column='PotentialCorrosion' , max_length=250, null=True)
    tankpadmaterial = models.CharField(db_column='TankPadMaterial', max_length=250, null=True)
    tankdrainagetype = models.CharField(db_column='TankDrainageType', max_length=250, null=True)
    cathodicprotectiontype = models.CharField(db_column='CathodicProtectionType', max_length=250, null=True)
    tankbottomtype = models.CharField(db_column='TankBottomType', max_length=250, null=True)
    soilsidetemperature = models.CharField(db_column='SoilSideTemperature', max_length=250,null=True)
    productcondition = models.CharField(db_column='ProductCondition', max_length=250, null=True)
    productsidetemp = models.CharField(db_column='ProductSideTemp', max_length=250, null=True)
    steamcoil = models.CharField(db_column='SteamCoil', max_length=250, null=True)
    waterdrawoff = models.CharField(db_column='WaterDrawOff', max_length=250, null=True)
    productsidebottom = models.CharField(db_column='ProductSideBottom', max_length=250, null=True)
    modifiedsoilsidecorrosionrate = models.FloatField(db_column='ModifiedSoilSideCorrosionRate', null=True)
    modifiedproductsidecorrosionrate = models.FloatField(db_column='ModifiedProductSideCorrosionRate', null=True)
    finalestimatedcorrosionrate = models.FloatField(db_column='FinalEstimatedCorrosionRate', null=True)
    create = models.DateTimeField(db_column='Created', default=datetime.datetime.now())


    class Meta:
        managed = False
        db_table = 'rw_corrosion_rate_tank'
        ordering = ('corrosionid',)

class RwEquipment(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    commissiondate = models.DateTimeField(db_column='CommissionDate')  # Field name made lowercase.
    adminupsetmanagement = models.IntegerField(db_column='AdminUpsetManagement', default=0)  # Field name made lowercase.
    containsdeadlegs = models.IntegerField(db_column='ContainsDeadlegs', default=0, blank=True, null=True)  # Field name made lowercase.
    cyclicoperation = models.IntegerField(db_column='CyclicOperation',default= 0, blank=True, null=True)  # Field name made lowercase.
    highlydeadleginsp = models.IntegerField(db_column='HighlyDeadlegInsp',default=0, blank=True, null=True)  # Field name made lowercase.
    downtimeprotectionused = models.IntegerField(db_column='DowntimeProtectionUsed',default=0, blank=True, null=True)  # Field name made lowercase.
    externalenvironment = models.CharField(db_column='ExternalEnvironment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heattraced = models.IntegerField(db_column='HeatTraced',default=0, blank=True, null=True)  # Field name made lowercase.
    interfacesoilwater = models.IntegerField(db_column='InterfaceSoilWater',default=0, blank=True, null=True)  # Field name made lowercase.
    lineronlinemonitoring = models.IntegerField(db_column='LinerOnlineMonitoring',default=0, blank=True, null=True)  # Field name made lowercase.
    materialexposedtoclext = models.IntegerField(db_column='MaterialExposedToClExt',default=0, blank=True, null=True)  # Field name made lowercase.
    minreqtemperaturepressurisation = models.FloatField(db_column='MinReqTemperaturePressurisation', blank=True, null=True)  # Field name made lowercase.
    onlinemonitoring = models.CharField(db_column='OnlineMonitoring', max_length=100, blank=True, null=True)  # Field name made lowercase.
    presencesulphideso2 = models.IntegerField(db_column='PresenceSulphidesO2',default=0, blank=True, null=True)  # Field name made lowercase.
    presencesulphideso2shutdown = models.IntegerField(db_column='PresenceSulphidesO2Shutdown',default=0, blank=True, null=True)  # Field name made lowercase.
    pressurisationcontrolled = models.IntegerField(db_column='PressurisationControlled',default=0, blank=True, null=True)  # Field name made lowercase.
    pwht = models.IntegerField(db_column='PWHT',default=0, blank=True, null=True)  # Field name made lowercase.
    steamoutwaterflush = models.IntegerField(db_column='SteamOutWaterFlush',default=0, blank=True, null=True)  # Field name made lowercase.
    managementfactor = models.FloatField(db_column='ManagementFactor', blank=True, null=True)  # Field name made lowercase.
    thermalhistory = models.CharField(db_column='ThermalHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yearlowestexptemp = models.IntegerField(db_column='YearLowestExpTemp',default=0, blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True,default=0)  # Field name made lowercase.
    typeofsoil = models.CharField(db_column='TypeOfSoil', max_length=50, blank=True, null=True)  # Field name made lowercase.
    environmentsensitivity = models.CharField(db_column='EnvironmentSensitivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    distancetogroundwater = models.FloatField(db_column='DistanceToGroundWater',default=0, blank=True, null=True)  # Field name made lowercase.
    adjustmentsettle = models.CharField(db_column='AdjustmentSettle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    componentiswelded = models.IntegerField(db_column='ComponentIsWelded',default=0, blank=True, null=True)  # Field name made lowercase.
    tankismaintained = models.IntegerField(db_column='TankIsMaintained',default=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_equipment'
        ordering = ('id',)


class RwExtcorTemperature(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    minus12tominus8 = models.FloatField(db_column='Minus12ToMinus8', blank=True, null=True,default=0)  # Field name made lowercase.
    minus8toplus6 = models.FloatField(db_column='Minus8ToPlus6', blank=True, null=True,default=0)  # Field name made lowercase.
    plus6toplus32 = models.FloatField(db_column='Plus6ToPlus32', blank=True, null=True,default=0)  # Field name made lowercase.
    plus32toplus71 = models.FloatField(db_column='Plus32ToPlus71', blank=True, null=True,default=0)  # Field name made lowercase.
    plus71toplus107 = models.FloatField(db_column='Plus71ToPlus107', blank=True, null=True,default=0)  # Field name made lowercase.
    plus107toplus121 = models.FloatField(db_column='Plus107ToPlus121', blank=True, null=True,default=0)  # Field name made lowercase.
    plus121toplus135 = models.FloatField(db_column='Plus121ToPlus135', blank=True, null=True,default=0)  # Field name made lowercase.
    plus135toplus162 = models.FloatField(db_column='Plus135ToPlus162', blank=True, null=True,default=0)  # Field name made lowercase.
    plus162toplus176 = models.FloatField(db_column='Plus162ToPlus176', blank=True, null=True,default=0)  # Field name made lowercase.
    morethanplus176 = models.FloatField(db_column='MoreThanPlus176', blank=True, null=True,default=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_extcor_temperature'
        ordering = ('id',)

class RWFullCofTank(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID',primary_key=True)  # Field name made lowercase.
    cofvalue = models.FloatField(db_column='CoFValue', blank=True, null=True,default=0)  # Field name made lowercase.
    cofcategory = models.CharField(db_column='CoFCategory', max_length=50, blank=True,null=True)  # Field name made lowercase.
    prodcost = models.FloatField(db_column='ProdCost', blank=True, null=True,default=0)   # Field name made lowercase.
    equipoutagemultiplier = models.FloatField(db_column='EquipOutageMultiplier', blank=True, null=True,default=0)  # Field name made lowercase.
    equipcost = models.FloatField(db_column='equipcost', blank=True, null=True,default=0)  # Field name made lowercase.
    popdens = models.FloatField(db_column='popdens', blank=True, null=True,default=0)  # Field name made lowercase.
    injcost = models.FloatField(db_column='injcost', blank=True, null=True,default=0)  # Field name made lowercase.
    cofmatrixvalue = models.FloatField(db_column='CoFMatrixValue', blank=True, null=True,default=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_full_cof_tank'
        ordering = ('id',)

class RwFullFcof(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    fcofvalue = models.FloatField(db_column='FCoFValue', blank=True, null=True)  # Field name made lowercase.
    fcofcategory = models.CharField(db_column='FCoFCategory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ail = models.IntegerField(db_column='AIL', blank=True, null=True)  # Field name made lowercase.
    envcost = models.FloatField(blank=True, null=True)
    equipcost = models.FloatField(blank=True, null=True)
    prodcost = models.FloatField(blank=True, null=True)
    popdens = models.FloatField(blank=True, null=True)
    injcost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rw_full_fcof'
        ordering = ('id',)


class RwFullPof(models.Model):
    try:
        id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID',
                               primary_key=True)  # Field name made lowercase.
        thinningap1 = models.FloatField(db_column='ThinningAP1', blank=True, null=True)  # Field name made lowercase.
        thinningap2 = models.FloatField(db_column='ThinningAP2', blank=True, null=True)  # Field name made lowercase.
        thinningap3 = models.FloatField(db_column='ThinningAP3', blank=True, null=True)  # Field name made lowercase.
        sccap1 = models.FloatField(db_column='SCCAP1', blank=True, null=True)  # Field name made lowercase.
        sccap2 = models.FloatField(db_column='SCCAP2', blank=True, null=True)  # Field name made lowercase.
        sccap3 = models.FloatField(db_column='SCCAP3', blank=True, null=True)  # Field name made lowercase.
        externalap1 = models.FloatField(db_column='ExternalAP1', blank=True, null=True)  # Field name made lowercase.
        externalap2 = models.FloatField(db_column='ExternalAP2', blank=True, null=True)  # Field name made lowercase.
        externalap3 = models.FloatField(db_column='ExternalAP3', blank=True, null=True)  # Field name made lowercase.
        brittleap1 = models.FloatField(db_column='BrittleAP1', blank=True, null=True)  # Field name made lowercase.
        brittleap2 = models.FloatField(db_column='BrittleAP2', blank=True, null=True)  # Field name made lowercase.
        brittleap3 = models.FloatField(db_column='BrittleAP3', blank=True, null=True)  # Field name made lowercase.
        htha_ap1 = models.FloatField(db_column='HTHA_AP1', blank=True, null=True)  # Field name made lowercase.
        htha_ap2 = models.FloatField(db_column='HTHA_AP2', blank=True, null=True)  # Field name made lowercase.
        htha_ap3 = models.FloatField(db_column='HTHA_AP3', blank=True, null=True)  # Field name made lowercase.
        fatigueap1 = models.FloatField(db_column='FatigueAP1', blank=True, null=True)  # Field name made lowercase.
        fatigueap2 = models.FloatField(db_column='FatigueAP2', blank=True, null=True)  # Field name made lowercase.
        fatigueap3 = models.FloatField(db_column='FatigueAP3', blank=True, null=True)  # Field name made lowercase.
        fms = models.FloatField(db_column='FMS', blank=True, null=True)  # Field name made lowercase.
        thinningtype = models.CharField(db_column='ThinningType', max_length=7, blank=True,
                                        null=True)  # Field name made lowercase.
        gfftotal = models.FloatField(db_column='GFFTotal', blank=True, null=True)  # Field name made lowercase.
        thinninglocalap1 = models.FloatField(db_column='ThinningLocalAP1', blank=True,
                                             null=True)  # Field name made lowercase.
        thinninglocalap2 = models.FloatField(db_column='ThinningLocalAP2', blank=True,
                                             null=True)  # Field name made lowercase.
        thinninglocalap3 = models.FloatField(db_column='ThinningLocalAP3', blank=True,
                                             null=True)  # Field name made lowercase.
        thinninggeneralap1 = models.FloatField(db_column='ThinningGeneralAP1', blank=True,
                                               null=True)  # Field name made lowercase.
        thinninggeneralap2 = models.FloatField(db_column='ThinningGeneralAP2', blank=True,
                                               null=True)  # Field name made lowercase.
        thinninggeneralap3 = models.FloatField(db_column='ThinningGeneralAP3', blank=True,
                                               null=True)  # Field name made lowercase.
        totaldfap1 = models.FloatField(db_column='TotalDFAP1', blank=True, null=True)  # Field name made lowercase.
        totaldfap2 = models.FloatField(db_column='TotalDFAP2', blank=True, null=True)  # Field name made lowercase.
        totaldfap3 = models.FloatField(db_column='TotalDFAP3', blank=True, null=True)  # Field name made lowercase.
        pofap1 = models.FloatField(db_column='PoFAP1', blank=True, null=True)  # Field name made lowercase.
        pofap2 = models.FloatField(db_column='PoFAP2', blank=True, null=True)  # Field name made lowercase.
        pofap3 = models.FloatField(db_column='PoFAP3', blank=True, null=True)  # Field name made lowercase.
        pofap1category = models.CharField(db_column='PoFAP1Category', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
        pofap2category = models.CharField(db_column='PoFAP2Category', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
        pofap3category = models.CharField(db_column='PoFAP3Category', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
        semiap1 = models.FloatField(db_column='SemiAP1', blank=True, null=True)
        semiap2 = models.FloatField(db_column='SemiAP2', blank=True, null=True)
        semiap3 = models.FloatField(db_column='SemiAP3', blank=True, null=True)
        cofvalue = models.FloatField(db_column='CoFValue', blank=True, null=True)
        cofcategory = models.CharField(db_column='CoFCategory', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
        coffmatrixvalue = models.FloatField(db_column='CoFMatrixValue', blank=True, null=True)
        rli = models.FloatField(db_column='RLI', blank=True, null=True)
        maxtrixpofapi1 = models.FloatField(db_column='MatrixPoFAP1', blank=True, null=True)
        maxtrixpofapi2 = models.FloatField(db_column='MatrixPoFAP2', blank=True, null=True)
        maxtrixpofapi3 = models.FloatField(db_column='MatrixPoFAP3', blank=True, null=True)
    except Exception as e:
        print(e)

    class Meta:
        managed = False
        db_table = 'rw_full_pof'
        ordering = ('id',)
        get_latest_by = 'id'

class RwInputCaLevel1(models.Model): # đầu vào ca 1+ 2 chỉnh sửa ngày 26/4/2020
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    api_fluid = models.CharField(db_column='API_FLUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    release_duration = models.CharField(db_column='Release_Duration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detection_type = models.CharField(db_column='Detection_Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isulation_type = models.CharField(db_column='Isolation_Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    equipment_cost = models.FloatField(db_column='Equipment_Cost', blank=True, null=True)  # Field name made lowercase.
    injure_cost = models.FloatField(db_column='Injure_Cost', blank=True, null=True)  # Field name made lowercase.
    evironment_cost = models.FloatField(db_column='Evironment_Cost', blank=True, null=True)  # Field name made lowercase.
    toxic_percent = models.FloatField(db_column='Toxic_Percent', blank=True, null=True)  # Field name made lowercase.
    personal_density = models.FloatField(db_column='Personal_Density', blank=True, null=True)  # Field name made lowercase.
    material_cost = models.FloatField(db_column='Material_Cost', blank=True, null=True)  # Field name made lowercase.
    production_cost = models.FloatField(db_column='Production_Cost', blank=True, null=True,default=0)  # Field name made lowercase.
    mass_inventory = models.FloatField(db_column='Mass_Inventory', blank=True, null=True)  # Field name made lowercase.
    mass_component = models.FloatField(db_column='Mass_Component', blank=True, null=True)  # Field name made lowercase.
    stored_pressure = models.FloatField(db_column='Stored_Pressure', blank=True, null=True)  # Field name made lowercase.
    stored_temp = models.FloatField(db_column='Stored_Temp', blank=True, null=True)  # Field name made lowercase.
    model_fluid = models.CharField(db_column='Model_Fluid', max_length=50, blank=True, null=True)
    toxic_fluid = models.CharField(db_column='Toxic_Fluid', max_length=50, blank=True, null=True)
    primary_fluid = models.FloatField(db_column='Primary_Fluid', blank=True, null=True)
    volatile_fluid = models.FloatField(db_column='Volatile_Fluid', blank=True, null=True)
    mitigation_system = models.CharField(db_column='Mitigation', blank=True, null=True,max_length=200)
    process_unit = models.FloatField(db_column='Process_Unit_Component', blank=True, null=True)
    outage_multiplier = models.FloatField(db_column='Outage_Multiplier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rw_input_ca_level1'
        ordering = ('id',)


class RwInputCaTank(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    fluid_height = models.FloatField(db_column='FLUID_HEIGHT', blank=True, null=True)  # Field name made lowercase.
    shell_course_height = models.FloatField(db_column='SHELL_COURSE_HEIGHT', blank=True, null=True)  # Field name made lowercase.
    tank_diametter = models.FloatField(db_column='TANK_DIAMETTER', blank=True, null=True)  # Field name made lowercase.
    prevention_barrier = models.IntegerField(db_column='Prevention_Barrier', default=0, blank=True, null=True)  # Field name made lowercase.
    environ_sensitivity = models.CharField(db_column='Environ_Sensitivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_lvdike = models.FloatField(db_column='P_lvdike', blank=True, null=True)  # Field name made lowercase.
    p_onsite = models.FloatField(db_column='P_onsite', blank=True, null=True)  # Field name made lowercase.
    p_offsite = models.FloatField(db_column='P_offsite', blank=True, null=True)  # Field name made lowercase.
    soil_type = models.CharField(db_column='Soil_Type', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tank_fluid = models.CharField(db_column='TANK_FLUID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    api_fluid = models.CharField(db_column='API_FLUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sw = models.FloatField(db_column='SW', blank=True, null=True)  # Field name made lowercase.
    productioncost = models.FloatField(db_column='ProductionCost', blank=True, null=True,default=0)  # Field name made lowercase.
    primary_fluid = models.FloatField(db_column='Primary_Fluid', blank=True, null=True)
    volatile_fluid = models.FloatField(db_column='Volatile_Fluid', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rw_input_ca_tank'
        ordering = ('id',)


class RwInspectionHistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inspectionplanname = models.CharField(db_column='InspectionPlanName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inspectioncoveragename = models.CharField(db_column='InspectionCoverageName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    equipmentnumber = models.CharField(db_column='EquipmentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    componentnumber = models.CharField(db_column='ComponentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dm = models.CharField(db_column='DM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    inspectiontype = models.CharField(db_column='InspectionType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    inspectiondate = models.DateTimeField(db_column='InspectionDate', blank=True, null=True)  # Field name made lowercase.
    inspectioneffective = models.CharField(db_column='InspectionEffective', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_inspection_history'
        ordering = ('id',)


class RwMaterial(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    materialname = models.CharField(db_column='MaterialName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    designpressure = models.FloatField(db_column='DesignPressure', blank=True, null=True,default=0)  # Field name made lowercase.
    designtemperature = models.FloatField(db_column='DesignTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    mindesigntemperature = models.FloatField(db_column='MinDesignTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    brittlefracturethickness = models.FloatField(db_column='BrittleFractureThickness',blank=True,null=True,default=0)
    corrosionallowance = models.FloatField(db_column='CorrosionAllowance', blank=True, null=True)  # Field name made lowercase.
    sigmaphase = models.FloatField(db_column='SigmaPhase', blank=True, null=True,default=0)  # Field name made lowercase.
    sulfurcontent = models.CharField(db_column='SulfurContent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heattreatment = models.CharField(db_column='HeatTreatment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    steelproductform = models.CharField(db_column='SteelProductForm',max_length=60,blank=True,null=True)
    referencetemperature = models.FloatField(db_column='ReferenceTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    ptamaterialcode = models.CharField(db_column='PTAMaterialCode', max_length=70, blank=True, null=True)  # Field name made lowercase.
    hthamaterialcode = models.CharField(db_column='HTHAMaterialCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispta = models.IntegerField(db_column='IsPTA',default=0, blank=True, null=True)  # Field name made lowercase.
    ishtha = models.IntegerField(db_column='IsHTHA',default=0, blank=True, null=True)  # Field name made lowercase.
    austenitic = models.IntegerField(db_column='Austenitic',default=0, blank=True, null=True)  # Field name made lowercase.
    temper = models.IntegerField(db_column='Temper',default=0, blank=True, null=True)  # Field name made lowercase.
    carbonlowalloy = models.IntegerField(db_column='CarbonLowAlloy',default=0, blank=True, null=True)  # Field name made lowercase.
    nickelbased = models.IntegerField(db_column='NickelBased',default=0, blank=True, null=True)  # Field name made lowercase.
    chromemoreequal12 = models.IntegerField(db_column='ChromeMoreEqual12',default=0, blank=True, null=True)  # Field name made lowercase.
    costfactor = models.FloatField(db_column='CostFactor', blank=True, null=True,default=0)  # Field name made lowercase.
    yieldstrength = models.FloatField(db_column='YieldStrength', blank=True,null=True,default=0)
    tensilestrength = models.FloatField(db_column='TensileStrength', blank=True, null=True,default=0)
    class Meta:
        managed = False
        db_table = 'rw_material'
        ordering = ('id',)


class RwStream(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    aminesolution = models.CharField(db_column='AmineSolution', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aqueousoperation = models.IntegerField(db_column='AqueousOperation',default=0, blank=True, null=True)  # Field name made lowercase.
    aqueousshutdown = models.IntegerField(db_column='AqueousShutdown',default=0, blank=True, null=True)  # Field name made lowercase.
    toxicconstituent = models.IntegerField(db_column='ToxicConstituent',default=0, blank=True, null=True)  # Field name made lowercase.
    caustic = models.IntegerField(db_column='Caustic',default=0, blank=True, null=True)  # Field name made lowercase.
    chloride = models.FloatField(db_column='Chloride', blank=True, null=True,default=0)  # Field name made lowercase.
    co3concentration = models.FloatField(db_column='CO3Concentration', blank=True, null=True,default=0)  # Field name made lowercase.
    cyanide = models.IntegerField(db_column='Cyanide',default=0, blank=True, null=True)  # Field name made lowercase.
    exposedtogasamine = models.IntegerField(db_column='ExposedToGasAmine',default=0, blank=True, null=True)  # Field name made lowercase.
    exposedtosulphur = models.IntegerField(db_column='ExposedToSulphur',default=0, blank=True, null=True)  # Field name made lowercase.
    exposuretoamine = models.CharField(db_column='ExposureToAmine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flammablefluidid = models.IntegerField(db_column='FlammableFluidID', blank=True,null=True,default=0)
    h2s = models.IntegerField(db_column='H2S',default=0, blank=True, null=True)  # Field name made lowercase.
    h2sinwater = models.FloatField(db_column='H2SInWater', blank=True, null=True,default=0)  # Field name made lowercase.
    hydrogen = models.IntegerField(db_column='Hydrogen',default=0, blank=True, null=True)  # Field name made lowercase.
    h2spartialpressure = models.FloatField(db_column='H2SPartialPressure', blank=True, null=True,default=0)  # Field name made lowercase.
    hydrofluoric = models.IntegerField(db_column='Hydrofluoric',default=0, blank=True, null=True)  # Field name made lowercase.
    materialexposedtoclint = models.IntegerField(db_column='MaterialExposedToClInt',default=0, blank=True, null=True)  # Field name made lowercase.
    maxoperatingpressure = models.FloatField(db_column='MaxOperatingPressure', blank=True, null=True,default=0)  # Field name made lowercase.
    maxoperatingtemperature = models.FloatField(db_column='MaxOperatingTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    minoperatingpressure = models.FloatField(db_column='MinOperatingPressure', blank=True, null=True,default=0)  # Field name made lowercase.
    minoperatingtemperature = models.FloatField(db_column='MinOperatingTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    criticalexposuretemperature = models.FloatField(db_column='CriticalExposureTemperature', blank=True, null=True,default=0)  # Field name made lowercase.
    naohconcentration = models.FloatField(db_column='NaOHConcentration', blank=True, null=True,default=0)  # Field name made lowercase.
    releasefluidpercenttoxic = models.FloatField(db_column='ReleaseFluidPercentToxic', blank=True, null=True,default=0)  # Field name made lowercase.
    waterph = models.FloatField(db_column='WaterpH', blank=True, null=True,default=0)  # Field name made lowercase.
    tankfluidname = models.CharField(db_column='TankFluidName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fluidheight = models.FloatField(db_column='FluidHeight', blank=True, null=True,default=0)  # Field name made lowercase.
    fluidleavedikepercent = models.FloatField(db_column='FluidLeaveDikePercent', blank=True, null=True)  # Field name made lowercase.
    fluidleavedikeremainonsitepercent = models.FloatField(db_column='FluidLeaveDikeRemainOnSitePercent', blank=True, null=True)  # Field name made lowercase.
    fluidgooffsitepercent = models.FloatField(db_column='FluidGoOffSitePercent', blank=True, null=True)  # Field name made lowercase.
    flowrate = models.FloatField(db_column='FlowRate', blank=True,null=True,default=0)
    liquidlevel = models.FloatField(db_column='LiquidLevel',blank=True,null=True)
    storagephase = models.CharField(db_column='StoragePhase', max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rw_stream'
        ordering = ('id',)




class RwDamageMechanism(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dmitemid = models.ForeignKey('DmItems', on_delete=models.CASCADE, db_column='DMItemID')
    id_dm = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID_DM',primary_key=True)
    isactive = models.IntegerField(default=1, db_column='IsActive')
    notes = models.TextField(db_column='Notes', null=True)
    expectedtypeid = models.IntegerField(default=0, db_column='ExpectedTypeID')
    isel = models.IntegerField(default=0, db_column='IsEL')
    elvalue = models.IntegerField(default=0, db_column='ELValue')
    isdf = models.IntegerField(default= 1, db_column='IsDF')
    isuserdisabled = models.IntegerField(default=0, db_column='IsUserDisabled')
    df1 = models.FloatField(db_column='DF1')
    df2 = models.FloatField(db_column='DF2')
    df3 = models.FloatField(db_column='DF3')
    dfbase = models.FloatField(db_column='DFBase', default= 0)
    rli = models.FloatField(db_column='RLI', default=0)
    highestinspectioneffectiveness = models.TextField(max_length=50, db_column='HighestInspectionEffectiveness')
    secondinspectioneffectiveness = models.TextField(max_length=50, db_column='SecondInspectionEffectiveness', null=True)
    numberofinspections = models.IntegerField(db_column='NumberOfInspections')
    lastinspdate = models.DateTimeField(db_column='LastInspDate', blank=True)
    inspduedate = models.DateTimeField(db_column='InspDueDate', blank=True)

    class Meta:
        managed = False
        db_table = 'rw_damage_mechanism'
        #unique_together = (("id_dm","dmitemid"),)

class RwDataChart(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)
    riskage0 = models.FloatField(db_column='risk_age_0')
    riskage1 = models.FloatField(db_column='risk_age_1')
    riskage2 = models.FloatField(db_column='risk_age_2')
    riskage3 = models.FloatField(db_column='risk_age_3')
    riskage4 = models.FloatField(db_column='risk_age_4')
    riskage5 = models.FloatField(db_column='risk_age_5')
    riskage6 = models.FloatField(db_column='risk_age_6')
    riskage7 = models.FloatField(db_column='risk_age_7')
    riskage8 = models.FloatField(db_column='risk_age_8')
    riskage9 = models.FloatField(db_column='risk_age_9')
    riskage10 = models.FloatField(db_column='risk_age_10')
    riskage11 = models.FloatField(db_column='risk_age_11')
    riskage12 = models.FloatField(db_column='risk_age_12')
    riskage13 = models.FloatField(db_column='risk_age_13')
    riskage14 = models.FloatField(db_column='risk_age_14')
    riskage15 = models.FloatField(db_column='risk_age_15')
    riskage16 = models.FloatField(db_column='risk_age_16')
    riskage17 = models.FloatField(db_column='risk_age_17')
    riskage18 = models.FloatField(db_column='risk_age_18')
    riskage19 = models.FloatField(db_column='risk_age_19')
    riskage20 = models.FloatField(db_column='risk_age_20')
    riskage21 = models.FloatField(db_column='risk_age_21')
    riskage22 = models.FloatField(db_column='risk_age_22')
    riskage23 = models.FloatField(db_column='risk_age_23')
    riskage24 = models.FloatField(db_column='risk_age_24')
    riskage25 = models.FloatField(db_column='risk_age_25')
    riskage26 = models.FloatField(db_column='risk_age_26')
    riskage27 = models.FloatField(db_column='risk_age_27')
    riskage28 = models.FloatField(db_column='risk_age_28')
    risktarget = models.FloatField(db_column='risk_target')

    class Meta:
        managed = False
        db_table = 'rw_data_chart'
class RwDataDMFactor(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)
    riskage0 = models.FloatField(db_column='risk_age_0')
    riskage1 = models.FloatField(db_column='risk_age_1')
    riskage2 = models.FloatField(db_column='risk_age_2')
    riskage3 = models.FloatField(db_column='risk_age_3')
    riskage4 = models.FloatField(db_column='risk_age_4')
    riskage5 = models.FloatField(db_column='risk_age_5')
    riskage6 = models.FloatField(db_column='risk_age_6')
    riskage7 = models.FloatField(db_column='risk_age_7')
    riskage8 = models.FloatField(db_column='risk_age_8')
    riskage9 = models.FloatField(db_column='risk_age_9')
    riskage10 = models.FloatField(db_column='risk_age_10')
    riskage11 = models.FloatField(db_column='risk_age_11')
    riskage12 = models.FloatField(db_column='risk_age_12')
    riskage13 = models.FloatField(db_column='risk_age_13')
    riskage14 = models.FloatField(db_column='risk_age_14')
    riskage15 = models.FloatField(db_column='risk_age_15')
    riskage16 = models.FloatField(db_column='risk_age_16')
    riskage17 = models.FloatField(db_column='risk_age_17')
    riskage18 = models.FloatField(db_column='risk_age_18')
    riskage19 = models.FloatField(db_column='risk_age_19')
    riskage20 = models.FloatField(db_column='risk_age_20')
    riskage21 = models.FloatField(db_column='risk_age_21')
    riskage22 = models.FloatField(db_column='risk_age_22')
    riskage23 = models.FloatField(db_column='risk_age_23')
    riskage24 = models.FloatField(db_column='risk_age_24')
    riskage25 = models.FloatField(db_column='risk_age_25')
    riskage26 = models.FloatField(db_column='risk_age_26')
    riskage27 = models.FloatField(db_column='risk_age_27')
    riskage28 = models.FloatField(db_column='risk_age_28')
    risktarget = models.FloatField(db_column='risk_target')

    class Meta:
        managed = False
        db_table = 'rw_dmfactor_chart'

class RwDataChartPoF(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)
    riskage0 = models.FloatField(db_column='risk_age_0')
    riskage1 = models.FloatField(db_column='risk_age_1')
    riskage2 = models.FloatField(db_column='risk_age_2')
    riskage3 = models.FloatField(db_column='risk_age_3')
    riskage4 = models.FloatField(db_column='risk_age_4')
    riskage5 = models.FloatField(db_column='risk_age_5')
    riskage6 = models.FloatField(db_column='risk_age_6')
    riskage7 = models.FloatField(db_column='risk_age_7')
    riskage8 = models.FloatField(db_column='risk_age_8')
    riskage9 = models.FloatField(db_column='risk_age_9')
    riskage10 = models.FloatField(db_column='risk_age_10')
    riskage11 = models.FloatField(db_column='risk_age_11')
    riskage12 = models.FloatField(db_column='risk_age_12')
    riskage13 = models.FloatField(db_column='risk_age_13')
    riskage14 = models.FloatField(db_column='risk_age_14')
    riskage15 = models.FloatField(db_column='risk_age_15')
    riskage16 = models.FloatField(db_column='risk_age_16')
    riskage17 = models.FloatField(db_column='risk_age_17')
    riskage18 = models.FloatField(db_column='risk_age_18')
    riskage19 = models.FloatField(db_column='risk_age_19')
    riskage20 = models.FloatField(db_column='risk_age_20')
    riskage21 = models.FloatField(db_column='risk_age_21')
    riskage22 = models.FloatField(db_column='risk_age_22')
    riskage23 = models.FloatField(db_column='risk_age_23')
    riskage24 = models.FloatField(db_column='risk_age_24')
    riskage25 = models.FloatField(db_column='risk_age_25')
    riskage26 = models.FloatField(db_column='risk_age_26')
    riskage27 = models.FloatField(db_column='risk_age_27')
    riskage28 = models.FloatField(db_column='risk_age_28')
    risktarget = models.FloatField(db_column='risk_target')

    class Meta:
        managed = False
        db_table = 'rw_pof_chart'
class ZUser(models.Model):
    id=models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    name = models.CharField(max_length=60, blank=True, null=True,db_column='name')
    email = models.CharField(max_length=100, blank=True, null=True,db_column='email')
    email_service = models.CharField(max_length=100, blank=True, null=True,db_column='email_service')
    phone = models.CharField(max_length=11, blank=True, null=True,db_column='phone')
    adress = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    active = models.IntegerField(blank=True,null=False,default='0')
    reject = models.IntegerField(blank=True,null=False,default='0')
    active_notification = models.IntegerField(blank=True, null=False, default='0')
    other_info = models.IntegerField(blank=True, null=True)
    kind = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'z_user'

class ZTask(models.Model):
    id = id=models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    describle = models.CharField(max_length=60, blank=True, null=True,db_column='describle')

    class Meta:
        managed = False
        db_table = 'z_task'

class ZProfilebisiness(models.Model):
    id= models.AutoField(primary_key=True,blank=True,null=False)
    user = models.ForeignKey(ZUser, on_delete=models.CASCADE)
    organization_detail = models.CharField(blank=True,null=True, max_length=1000)
    image_name = models.CharField(blank=True, null=True, max_length=200, default='noavatar')

    class Meta:
        managed = True
        db_table = 'z_profile_business'


class ZPosts(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_user_2 = models.IntegerField(blank=True, null=True)
    id_component = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=8000, blank=True, null=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_posts'
        ordering = ['-id']

class ZComment(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_posts = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_comment'

class ZNotification(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    object = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    id_link_to_part=models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'z_notification'
        ordering = ['-id']

class Emailsent(models.Model):
    id = models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    content=models.TextField(db_column='content',blank=True,null=False)
    subject = models.TextField(db_column='subject', blank=True, null=False)
    Emails=models.TextField(blank=True,null=False,db_column='emailsent')
    Emailt = models.TextField(blank=True, null=False, db_column='emailto')
    # date = models.DateTimeField(db_column='date', default=datetime.datetime.now())
    date = models.DateTimeField(db_column='date', default=datetime.datetime.now())
    class Meta:
        managed = False
        db_table = 'zm_people_sent'


class Emailto(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False,db_column='id')
    content = models.TextField(db_column='content', blank=True, null=False)
    subject = models.TextField(db_column='subject', blank=True, null=False)
    Emails=models.TextField(blank=True, null=False, db_column='emailsent')
    Emailt = models.TextField(blank=True, null=False, db_column='emailto')
    date = models.DateTimeField(db_column='date', default=datetime.datetime.now())
    Is_see = models.IntegerField(db_column='Is_see', blank=True, null=False)
    date = models.DateTimeField(db_column='date', default=datetime.datetime.now())
    class Meta:
        managed = False
        db_table = 'zm_people_to'

class Zbusiness(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='id')
    compainfor = models.TextField(db_column='compa_infor', blank=True, null=False)
    namecompany = models.TextField(db_column='name_company',blank=True,null=False)
    userID = models.ForeignKey('ZUser', on_delete=models.CASCADE, db_column='userID')

    class Meta:
        managed = False
        db_table = 'z_business'

class FileSystemPath(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='ID')
    siteid = models.ForeignKey('Sites', on_delete=models.CASCADE, db_column='SiteID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=False)
    path = models.TextField(db_column='Path', blank=True, null=False)
    filedescription = models.TextField(db_column='FileDescription', blank=True, null=False)
    filetype = models.TextField(db_column='FileType', blank=True, null=False)
    size = models.TextField(db_column='Size', blank=True, null=False)
    dateuploaded = models.DateTimeField(db_column='DateUploaded', default=datetime.datetime.now())
    system = models.IntegerField(db_column='System', blank=True, null=False, default=0)
    class Meta:
        managed = False
        db_table = 'file_system_path'
        ordering = ('id',)

class VerificationPeriodically(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='ID')
    siteid = models.ForeignKey('Sites', on_delete=models.CASCADE, db_column='SiteID')  # Field name made lowercase.
    facilityid = models.ForeignKey('Facility', on_delete=models.CASCADE, db_column='FacilityID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('EquipmentMaster', on_delete=models.CASCADE, db_column='EquipmentID')  # Field name made lowercase.
    componentid = models.ForeignKey('ComponentMaster', on_delete=models.CASCADE, db_column='ComponentID')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode', blank=True, null=False)
    timer = models.TextField(db_column='Timer', blank=True, null=False)
    interpolation = models.IntegerField(db_column='Interpolation', blank=True, null=False)
    create = models.DateTimeField(db_column='Created', default=datetime.datetime.now())
    class Meta:
        managed = False
        db_table = 'verification_periodically'
        ordering = ('id',) 
        
class Verification(models.Model):
    id = models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    proposal = models.TextField(db_column='proposal',blank=True,null=False)
    date = models.DateTimeField(db_column='date',default=datetime.datetime.now())
    Is_active = models.IntegerField(db_column='Is_active',blank=True,null=False)
    manager = models.TextField(db_column='manager',blank=True,null=False)
    facility = models.IntegerField(db_column='facility',blank=True,null=False)
    com = models.TextField(db_column='com',blank=True,null=False)
    eq = models.TextField(db_column='eq', blank=True, null=False)
    link = models.TextField(db_column='link', blank=True, null=False)
    idcom = models.TextField(db_column='idcom', blank=True, null=False)
    idequip = models.TextField(db_column='idequip', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'verification'
class Report_verification(models.Model):
    id = models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    date = models.DateTimeField(db_column='date',default=datetime.datetime.now())
    damage_factor = models.TextField(db_column='damage_factor',blank=True,null=False)
    pof = models.TextField(db_column='pof', blank=True, null=False)
    cof = models.TextField(db_column='cof', blank=True, null=False)
    risk=models.TextField(db_column='risk', blank=True, null=False)
    inspdudate = models.DateTimeField(db_column='inspdudate', default=datetime.datetime.now())
    lastdudate = models.DateTimeField(db_column='lastdudate', default=datetime.datetime.now())
    idreportsent = models.IntegerField(db_column='idreportsent', blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'report_verification'

class VeriContent(models.Model):
    id = models.AutoField(primary_key=True,blank=True,null=False,db_column='id')
    Verification = models.ForeignKey('Verification',db_column='VeriID',blank=True,null=False,on_delete=models.CASCADE)
    content = models.TextField(db_column='content',blank=True,null=False)
    date = models.DateTimeField(db_column='date',default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'vericontent'

class PRDType(models.Model):
    id = models.IntegerField(primary_key=True,blank=True,db_column='id')
    prdtypename = models.CharField(db_column='PRDTypeName', max_length=50)

    class Meta:
        managed = False
        db_table = 'prd_type'

## inspection plan


### contain data input and output COF

class RwFullCoFFluid(models.Model):
    id = models.ForeignKey('RwAssessment', db_column='ID', on_delete=models.CASCADE, primary_key=True)
    cp = models.FloatField(db_column='Cp', blank=True, null=True )
    k = models.FloatField(db_column='k', blank=True, null=True)
    gfftotal = models.FloatField(db_column='GFFTotal', blank=True, null=True)
    kv_n = models.FloatField(db_column='Kv_n', blank=True, null=True)
    realeasePhase = models.CharField(db_column='ReleasePhase', blank=True, null=True, max_length=100)
    cd = models.FloatField(db_column='Cd', blank=True, null=True)
    Ptrans = models.FloatField(db_column='Ptrans', blank=True, null=True)
    nbp = models.FloatField(db_column='NBP', blank=True,null=True)
    density = models.FloatField(db_column='Density', blank=True, null=True)
    mw = models.FloatField(db_column='MW', blank=True, null=True)
    r = models.FloatField(db_column='R', blank=True, null=True)
    ps = models.FloatField(db_column='Ps', blank=True, null=True)
    ts = models.FloatField(db_column='Ts', blank=True, null=True)
    patm = models.FloatField(db_column='Patm', blank=True, null=True)
    fact_di = models.FloatField(db_column='fact_di', blank=True, null=True)
    fact_mit = models.FloatField(db_column='fact_mit', blank=True, null=True)
    fact_ait = models.FloatField(db_column='fact_AIT', blank=True, null=True)
    g = models.FloatField(db_column='g', blank=True, null=True)
    h = models.FloatField(db_column='h', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rw_full_cof_fluid'

class RwFullCoFHoleSize(models.Model):
    id = models.ForeignKey('RwAssessment', db_column='ID', on_delete=models.CASCADE, primary_key=True)
    gff_small = models.FloatField(db_column='gff_small', null=True, blank=True)
    gff_medium = models.FloatField(db_column='gff_medium', null=True, blank=True)
    gff_large = models.FloatField(db_column='gff_large', null=True, blank=True)
    gff_rupture = models.FloatField(db_column='gff_rupture', null=True, blank=True)
    an_small = models.FloatField(db_column='an_small',blank=True,null=True)
    an_medium = models.FloatField(db_column='an_medium', blank=True, null=True)
    an_large = models.FloatField(db_column='an_large', blank=True, null=True)
    an_rupture = models.FloatField(db_column='an_rupture', blank=True, null=True)
    wn_small = models.FloatField(db_column='wn_small', blank=True, null=True)
    wn_medium = models.FloatField(db_column='wn_medium', blank=True, null=True)
    wn_large = models.FloatField(db_column='wn_large', blank=True, null=True)
    wn_rupture = models.FloatField(db_column='wn_rupture', blank=True, null=True)
    t_n_small  = models.FloatField(db_column='t_n_small', blank=True, null=True)
    t_n_medium = models.FloatField(db_column='t_n_medium', blank=True, null=True)
    t_n_large = models.FloatField(db_column='t_n_large', blank=True, null=True)
    t_n_rupture = models.FloatField(db_column='t_n_rupture', blank=True, null=True)
    ld_max_n_small = models.FloatField(db_column='ld_max_n_small', blank=True, null=True)
    ld_max_n_medium = models.FloatField(db_column='ld_max_n_medium', blank=True, null=True)
    ld_max_n_large = models.FloatField(db_column='ld_max_n_large', blank=True, null=True)
    ld_max_n_rupture = models.FloatField(db_column='ld_max_n_rupture', blank=True, null=True)
    mass_add_n_small = models.FloatField(db_column='mass_add_n_small', blank=True, null=True)
    mass_add_n_medium = models.FloatField(db_column='mass_add_n_medium', blank=True, null=True)
    mass_add_n_large = models.FloatField(db_column='mass_add_n_large', blank=True, null=True)
    mass_add_n_rupture = models.FloatField(db_column='mass_add_n_rupture', blank=True, null=True)
    mass_avail_n_small = models.FloatField(db_column='mass_avail_n_small',blank=True,null=True)
    mass_avail_n_medium = models.FloatField(db_column='mass_avail_n_medium',blank=True,null=True)
    mass_avail_n_large = models.FloatField(db_column='mass_avail_n_large',blank=True,null=True)
    mass_avail_n_rupture = models.FloatField(db_column='mass_avail_n_rupture',blank=True,null=True)
    rate_n_small = models.FloatField(db_column='rate_n_small', blank=True, null=True)
    rate_n_medium = models.FloatField(db_column='rate_n_medium', blank=True, null=True)
    rate_n_large = models.FloatField(db_column='rate_n_large', blank=True, null=True)
    rate_n_rupture = models.FloatField(db_column='rate_n_rupture', blank=True, null=True)
    ld_n_small = models.FloatField(db_column='ld_n_small', blank=True, null=True)
    ld_n_medium = models.FloatField(db_column='ld_n_medium', blank=True, null=True)
    ld_n_large = models.FloatField(db_column='ld_n_large', blank=True, null=True)
    ld_n_rupture = models.FloatField(db_column='ld_n_rupture', blank=True, null=True)
    mass_n_small = models.FloatField(db_column='mass_n_small', blank=True, null=True)
    mass_n_medium = models.FloatField(db_column='mass_n_medium', blank=True, null=True)
    mass_n_large = models.FloatField(db_column='mass_n_large', blank=True, null=True)
    mass_n_rupture = models.FloatField(db_column='mass_n_rupture', blank=True, null=True)
    eneff_n_small = models.FloatField(db_column='eneff_n_small', blank=True, null=True)
    eneff_n_medium = models.FloatField(db_column='eneff_n_medium', blank=True, null=True)
    eneff_n_large = models.FloatField(db_column='eneff_n_large', blank=True, null=True)
    eneff_n_rupture = models.FloatField(db_column='eneff_n_rupture', blank=True, null=True)
    factIC_n_small = models.FloatField(db_column='factIC_n_small', blank=True, null=True)
    factIC_n_medium = models.FloatField(db_column='factIC_n_medium', blank=True, null=True)
    factIC_n_large = models.FloatField(db_column='factIC_n_large', blank=True, null=True)
    factIC_n_rupture = models.FloatField(db_column='factIC_n_rupture', blank=True, null=True)
    releasetype_small = models.CharField(db_column='releasetype_small',max_length=20, blank=True, null=True)
    releasetype_medium = models.CharField(db_column='releasetype_medium', max_length=20, blank=True, null=True)
    releasetype_large = models.CharField(db_column='releasetype_large', max_length=20, blank=True, null=True)
    releasetype_rupture = models.CharField(db_column='releasetype_rupture', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table  = 'rw_full_cof_hole_size'

class RwInputCaLevel2(models.Model): # đầu vào ca 2 ngay 23/11/2020
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    Psat = models.FloatField(db_column='Psat', blank=True, null=True)  # Field name made lowercase.
    Frac_l = models.FloatField(db_column='FRACT_Liquid', blank=True, null=True)  # Field name made lowercase.
    Frac_v = models.FloatField(db_column='FRACT_Vapor', blank=True, null=True)  # Field name made lowercase.
    Lower_flammable = models.FloatField(db_column='LOWER_FLAMABILITY', blank=True, null=True)  # Field name made lowercase.
    Upper_flammable = models.FloatField(db_column='UPPER_FLAMABILITY', blank=True, null=True)  # Field name made lowercase.
    Hcs = models.FloatField(db_column='HEAT_COMBUSTION', blank=True, null=True)  # Field name made lowercase.
    temp_flash = models.FloatField(db_column='TEMP_FLASH', blank=True, null=True)  # Field name made lowercase.
    Fract_flash = models.FloatField(db_column='FRACT_FLASH', blank=True, null=True)  # Field name made lowercase.
    Heat_combustion_l = models.FloatField(db_column='HEAT_COMBUSTION_Liquid', blank=True, null=True)  # Field name made lowercase.
    Heat_combustion_v = models.FloatField(db_column='HEAT_COMBUSTION_Vapor', blank=True, null=True)  # Field name made lowercase.
    temp_bubble = models.FloatField(db_column='TEMP_BUBBLE', blank=True, null=True)  # Field name made lowercase.
    temp_dew = models.FloatField(db_column='TEMP_DEW', blank=True, null=True)  # Field name made lowercase.
    delta = models.FloatField(db_column='deltaHv', blank=True, null=True)  # Field name made lowercase.
    surface = models.CharField(db_column='SURFACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp_ground = models.FloatField(db_column='TEMP_GROUND', blank=True, null=True)  # Field name made lowercase.
    pressure_bp = models.FloatField(db_column='BUBBLE_POINT_PRESSURE', blank=True, null=True)
    wind_speed_measured = models.FloatField(db_column='WIND_SPEED_MEASURED', blank=True, null=True)
    mfrac_flam = models.FloatField(db_column='MFRAC_FLAM', blank=True, null=True)
    temp_fp = models.FloatField(db_column='TEMP_FLASH_POINT', blank=True, null=True)
    atmospheric_temp = models.FloatField(db_column='ATMOSPHERIC_TEMP', blank=True, null=True)
    atmospheric_air_density=models.FloatField(db_column='ATMOSPHERIC_AIR_DENSITY', blank=True, null=True)
    atmospheric_rh = models.FloatField(db_column='ATMOSPHERIC_RELATIVE_HUMIDITY', blank=True, null=True)
    atmospheric_wrp = models.FloatField(db_column='ATMOSPHERIC_WATER_PARTIAL_PRESSURE', blank=True, null=True)
    brust_pressure = models.FloatField(db_column='BRUST_PRESSURE', blank=True, null=True)
    xs_fball = models.FloatField(db_column='XS_FBALL', blank=True, null=True)
    yield_factor = models.FloatField(db_column='YIELD_FACTOR', blank=True, null=True)
    tox_lim = models.FloatField(db_column='TOX_LIM', blank=True, null=True)
    mol_frac_tox = models.FloatField(db_column='MOL_FRAC_TOX', blank=True, null=True)
    equipment_stored_vapor = models.FloatField(db_column='EQUIPMENT_STORED_VAPOR', blank=True, null=True)
    n_v = models.FloatField(db_column='N_V', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rw_input_ca_level2'
        ordering = ('id',)

class Verificationsend(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False, db_column='id')
    id_user = models.IntegerField(db_column='id_user',blank=True,max_length=45)
    subject = models.CharField(db_column='subject',blank=True,max_length=45)
    link = models.IntegerField(db_column='link', blank=True, null=True)
    state = models.IntegerField(db_column='stt', blank=True, null=True)
    id_rep = models.IntegerField(db_column='id_rep', blank=True, null=True)
    facility = models.IntegerField(db_column='facility', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'verification_send'
        ordering = ('id',)

class Mitigation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_proposal = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='id_proposal', primary_key=True)
    risk_change = models.IntegerField(default=0, db_column='risk_change')
    selection = models.TextField(db_column='selection', null=True)
    nameParameter = models.TextField(db_column='nameParameter', null=True)
    priority = models.TextField(db_column='priority', null=True)
    value_now = models.IntegerField(default=0, db_column='value_now')
    pof_now = models.IntegerField(default=0, db_column='pof_now')
    cof_now = models.IntegerField(default=0, db_column='cof_now')
    risk_now = models.IntegerField(default=0, db_column='risk_now')
    value_change = models.IntegerField(default=0, db_column='value_change')
    pof_change = models.IntegerField(default=0, db_column='pof_change')
    cof_change = models.IntegerField(default=0, db_column='cof_change')
    number = models.IntegerField(db_column='number')

    class Meta:
        managed = False
        db_table = 'mitigation'
        