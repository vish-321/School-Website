from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Notice, School, Year, Student
from django.contrib.auth.models import User

# Register your models here.
# Register your models here.

# class StudentAdmin(UserAdmin):
# 	list_display = ('studentname', )
# 	search_fields = ('studentname', )
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()

admin.site.register(School)
admin.site.register(Notice)
# admin.site.register(Standard)
# admin.site.register(Divison)
admin.site.register(Year)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Student)





# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Students'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)