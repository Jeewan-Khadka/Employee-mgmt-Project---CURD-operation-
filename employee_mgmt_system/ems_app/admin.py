from django.contrib import admin
from .models import Employee,Role,Department

# Register your models here.


admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)

