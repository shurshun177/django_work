from djongo import models


# Create your models here.
class Version(models.Model):
    version_number = models.AutoField(unique=True, default=1000)
    hospital_type = models.CharField(max_length=1)
    version_name = models.CharField(max_length=72)
    version_type = models.CharField(max_length=1)
    active = models.CharField(max_length=1)
    hospital_code = models.CharField()      #??????????
    #business_topic = models.CharField()            ???????????
    measure = object
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      verbose_name='Created_At')
    updated_at = models.DateTimeField(verbose_name='Update_At')
    create_user = models.CharField(max_length=28)
    update_user = models.CharField(max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateTimeField()
    cancel_user = models.CharField(max_length=28)

    def __str__(self):
        return self.version_name
class Measure(models.Model):
    measure_code = models.CharField(unique=True, max_length=32)
    hospital_type = models.CharField(max_length=1)
    measure_name = models.CharField(max_length=64,
                                    verbose_name='Measure_Name')
    measure_desc = models.TextField(max_length=200,
                                    verbose_name='Measure_Desc')
    business_topic = models.CharField()
    criteria_inclusion = models.CharField(max_length=72)
    removal_criteria = models.CharField(max_length=72)
    numerator = models.CharField(max_length=64)
    denominator = models.CharField(max_length=64)
    measure_type = models.CharField(max_length=64)
    measuring_frequency = models.CharField(max_length=64)
    unit_measure = models.CharField(max_length=1)
    digit_num = models.IntegerField()
    separate_thousands = models.BooleanField(max_length=1)
    active = models.CharField(max_length=1, verbose_name='Active')
    from_date = models.DateTimeField(verbose_name='From_Date')
    to_date = models.DateTimeField(verbose_name='To_Date')
    target = models.CharField(max_length=64,verbose_name='Target')
    remarks = models.TextField(max_length=484, blank=True, null=True)
    create_date = models.DateTimeField()
    create_user = models.CharField(max_length=28)
    change_date = models.DateTimeField()
    change_user = models.CharField(max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateTimeField()
    cancel_user = models.CharField(max_length=28)
    def __str__(self):
        return self.measure_name

class DecryptionTables(models.Model):
    version_type =
    #hospital_type =
    #measure_type =
    #active_status =
    #business_topic =
    #measure_frequency =

class ActualExecution(models.Model):
    version_number = models.IntegerField()
    measure_code = models.CharField(max_length=32)
    hospital_type = models.CharField(max_length=1)
    measure_value = object
    create_date = models.DateTimeField()
    create_user = models.CharField(max_length=28)
    change_date = models.DateTimeField()
    change_user = models.CharField(max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateTimeField()
    cancel_user = models.CharField(max_length=28)
