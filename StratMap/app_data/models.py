

from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Version(models.Model):
    version_number = models.IntegerField(default=1000) # ***
    hospital_type = models.CharField(max_length=16) # ***
    version_name = models.CharField(max_length=72) # ***
    version_type = models.CharField(max_length=12) #
    version_desc = models.CharField(max_length=121) #
    active = models.BooleanField(max_length=1) #
    #hospital_code = models.CharField()      #??????????
    #business_topic = models.CharField()
    measure = models.ArrayReferenceField(blank=True, to='Measure') #
    create_date = models.DateField(auto_now=True, blank=True)
    create_user = models.CharField(
        max_length=28,
        #default=auth.user_logged_in
    )

    change_date = models.DateField(
        blank=True,
        null=True
    )
    change_user = models.CharField(blank=True,max_length=28)
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateField(
        blank=True,
        null=True
    )
    cancel_user = models.CharField(
        blank=True,
        max_length=28,
        #default=auth.user_logged_in
    )

    def __repr__(self):
        return '{} {}  {}'.format(
            self.version_name,
            self.hospital_type,
            self.version_number
        )


class Measure(models.Model):
    measure_code = models.CharField(max_length=32) #
    hospital_type = models.CharField(max_length=1) #
    measure_name = models.CharField(max_length=64) #
    measure_desc = models.TextField(max_length=200) #
    business_topic = models.CharField(max_length=24) #
    criteria_inclusion = models.CharField(max_length=72) #
    removal_criteria = models.CharField(max_length=72) #
    numerator = models.CharField(max_length=64) #
    denominator = models.CharField(max_length=64) #
    measure_type = models.CharField(max_length=64) #
    measuring_frequency = models.CharField(max_length=64) #
    measure_unit = models.IntegerField() #
    digit_num = models.IntegerField() #
    separate_thousands = models.BooleanField(max_length=1)
    active = models.BooleanField(max_length=1)
    from_date = models.DateField()
    to_date = models.DateField()
    target_default = models.FloatField(default=100) #
    remarks = models.TextField( #
        max_length=484,
        blank=True,
    )
    create_date = models.DateField(auto_now=True)
    create_user = models.CharField(
        max_length=28,
        #default=auth.user_logged_in
    )
    change_date = models.DateField(
        blank=True,
        null=True
    )
    change_user = models.CharField(
        blank=True,
        max_length=28,
        #default=auth.user_logged_in
    )
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateField(
        blank=True,
        null=True
    )
    cancel_user = models.CharField(
        blank=True,
        max_length=28,
        #default=auth.user_logged_in
    )

    def __str__(self):
        return self.measure_code

    def cancel(self):
        self.cancel = True
        self.cancel_date = timezone.now()
        #self.cancel_user =


class ActualExecution(models.Model):
    version_number = models.IntegerField(default=1000)
    measure_code = models.CharField(max_length=32)
    hospital_type = models.CharField(max_length=1)
    hospital_code = models.CharField(max_length=6)
    actual_value = object
    measure_value = models.IntegerField()
    create_date = models.DateField(auto_now=True)
    create_user = models.CharField(
        max_length=28,
        #default=auth.user_logged_in
    )
    change_date = models.DateField(
        blank=True,
        null=True
    )
    change_user = models.CharField(
        blank=True,
        max_length=28,
        #default=auth.user_logged_in
    )
    cancel = models.BooleanField(max_length=1)
    cancel_date = models.DateField(
        blank=True,
        null=True
    )
    cancel_user = models.CharField(
        blank=True,
        max_length=28
    )


class DecryptionTables(models.Model):
    name = models.CharField(max_length=32)
    values_list = models.ListField()


