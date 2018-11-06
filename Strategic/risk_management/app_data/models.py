from djongo import models


# Create your models here.
class Version(models.Model):
    version_number = models.IntegerField(unique=True, default=1000)
    hospital_type = models.CharField(max_length=1, default='1')
    version_name = models.CharField(blank=True, max_length=72)
    version_type = models.CharField(blank=True, max_length=1)
    version_desc = models.CharField(blank=True, max_length=121)
    active = models.CharField(blank=True, max_length=1)
    #hospital_code = models.CharField()      #??????????
    #business_topic = models.CharField()
    measure = models.ArrayReferenceField(blank=True, to='Measure')
    create_date = models.DateTimeField(blank=True, auto_now_add=True, null=True)
    create_user = models.CharField(blank=True, max_length=28)
    change_date = models.DateTimeField(blank=True)
    change_user = models.CharField(blank=True, max_length=28)
    cancel = models.BooleanField(blank=True, max_length=1)
    cancel_date = models.DateTimeField(blank=True, )
    cancel_user = models.CharField(blank=True, max_length=28)

    def __str__(self):
        return self.version_name
class Measure(models.Model):
    measure_code = models.CharField(unique=True,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                max_length=32)
    hospital_type = models.CharField(max_length=1)
    measure_name = models.CharField(max_length=64)
    measure_desc = models.TextField(max_length=200)
    business_topic = models.CharField(max_length=24)
    criteria_inclusion = models.CharField(max_length=72)
    removal_criteria = models.CharField(max_length=72)
    numerator = models.CharField(max_length=64)
    denominator = models.CharField(max_length=64)
    measure_type = models.CharField(max_length=64)
    measuring_frequency = models.CharField(max_length=64)
    measure_unit = models.IntegerField()
    digit_num = models.IntegerField()
    separate_thousands = models.BooleanField(max_length=1)
    active = models.CharField(max_length=1, verbose_name='Active')
    from_date = models.DateTimeField(verbose_name='From_Date')
    to_date = models.DateTimeField(verbose_name='To_Date')
    target_default = models.FloatField()
    remarks = models.TextField(max_length=484, blank=True, null=True)
    create_date = models.DateTimeField()
    create_user = models.CharField(max_length=28)
    change_date = models.DateTimeField()
    change_user = models.CharField(max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateTimeField()
    cancel_user = models.CharField(max_length=28)
    def __str__(self):
        return self.measure_code



class DecryptionTables(models.Model):
    name = models.CharField(max_length=32)
    values_list = models.ListField()
    def __str__(self):
        return self.name

class ActualExecution(models.Model):
    version_number = models.IntegerField(unique=True, default=1000)
    measure_code = models.CharField(unique=True, max_length=32)
    hospital_type = models.CharField(max_length=1)
    hospital_code = models.CharField(unique=True, max_length=6)
    actual_value = object
    measure_value = models.IntegerField()
    create_date = models.DateTimeField()
    create_user = models.CharField(max_length=28)
    change_date = models.DateTimeField()
    change_user = models.CharField(max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateTimeField()
    cancel_user = models.CharField(max_length=28)
