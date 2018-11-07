from django.contrib import admin
from .models import Version, Measure, ActualExecution, DecryptionTables
# Register your models here.
admin.site.register([Version, Measure, ActualExecution, DecryptionTables])
