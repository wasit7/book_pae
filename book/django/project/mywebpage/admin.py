from django.contrib import admin
from .models import Student, Subject, Enrollment, Factor

# Register your models here
class StudentAdmin(admin.ModelAdmin):
	list_display = ('username','std_id','firstname','lastname','email','province_id','sch_gpa','admit_year')
	#list_display = ('username','std_id','province_id','sch_gpa','admit_year')

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('sub_id','sub_name','description','credit')
	#def sub_name(self,obj):
	#	return obj.sub_name

class EnrollmentAdmin(admin.ModelAdmin):
	list_display = ('std_id','sub_id','grade','term','year')

	#def std_id(self,obj):
		#return obj.std_id

class FactorAdmin(admin.ModelAdmin):
	list_display = ('sub_id','subfac_1','subfac_2','subfac_3')
		

admin.site.register(Student,StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Factor,FactorAdmin)

