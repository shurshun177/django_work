from django.db import models
from .values import HOSPITAL_TYPES, VERSION_TYPES,\
    ACTIVE_STATUS, BS_CODE, MEASURE_TYPES, FREQUENCY


# Create your models here.
class Version(models.Model):
    version_number = models.IntegerField(unique=True, verbose_name='Version_No')
    version_name = models.CharField(max_length=72, verbose_name='Version_Name')
    version_type = models.CharField(max_length=1, choices=VERSION_TYPES,
                                    verbose_name='Version_Types')

    hospital_type = models.CharField(max_length=1, choices=HOSPITAL_TYPES,
                                     verbose_name='Hospital_Type')
    active = models.CharField(max_length=1, choices=ACTIVE_STATUS,
                              verbose_name='Active')
    #business_subject = models.ManyToManyField('BusinessSubject')
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      verbose_name='Created_At')
    updated_at = models.DateTimeField(verbose_name='Update_At')
    measure = models.ManyToManyField('Measure')

class Measure(models.Model):
    bs_code = models.CharField(max_length=1, choices=BS_CODE)
    #version = models.ManyToManyField('Version')
    measure_code = models.CharField(max_length=32, verbose_name='Measure_Code')
    measure_name = models.CharField(max_length=64,
                                    verbose_name='Measure_Name')
    measure_desc = models.TextField(max_length=200,
                                    verbose_name='Measure_Desc')
    criteria_inclusion = models.CharField(max_length=72,
                                          verbose_name='Criteria_Inclusion')
    removal_criteria = models.CharField(max_length=72,
                                        verbose_name='Removal_Criteria')
    numerator = models.CharField(max_length=64,
                                 verbose_name='Numerator')
    denominator = models.CharField(max_length=64,
                                   verbose_name='denominator')
    hospital_type = models.CharField(max_length=1, choices=HOSPITAL_TYPES)
    measure_type = models.CharField(max_length=64, choices=MEASURE_TYPES,
                                    verbose_name='Measure_Type')
    measuring_frequency = models.CharField(max_length=64,choices=FREQUENCY,
                                           verbose_name='Measuring_Frequency')
    unit_measure = models.CharField(max_length=64, verbose_name='Unit_Measure')
    digit_num = models.IntegerField(verbose_name='Num_Of_Digits')
    separate_thousands = models.BooleanField(max_length=1, verbose_name='Separate_Thousands')
    active = models.BooleanField(max_length=1, choices=ACTIVE_STATUS,
                              verbose_name='Active')
    from_date = models.DateTimeField(verbose_name='From_Date')
    to_date = models.DateTimeField(verbose_name='To_Date')
    target = models.CharField(max_length=64,verbose_name='Target')
    remarks = models.TextField(max_length=484, blank=True, null=True,
                               verbose_name='Remarks')