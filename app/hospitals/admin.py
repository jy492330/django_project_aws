from django.contrib import admin
from hospitals.models import Hospital, Department, Cost_Center

admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Cost_Center)
