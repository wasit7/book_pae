from django.contrib import admin
from .models import Student, Subject, Enrollment

# Register your models here
class StudentAdmin(admin.ModelAdmin):
	list_display = ('std_id','std_name','province_id','sch_gpa','admit_year')

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('sub_id','sub_name','description','credit')

class EnrollmentAdmin(admin.ModelAdmin):
	list_display = ('std_id','sub_id','grade','term','year')

	def std_id(self,obj):
		return obj.std_name
		
		

admin.site.register(Student,StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)

