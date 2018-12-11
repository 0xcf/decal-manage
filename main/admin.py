from django.contrib import admin

from .models import Semester, Facilitator, Student, Assignment, Checkoff

for model in (Semester,):
    admin.site.register(model)

    
@admin.register(Facilitator)
class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('username', 'semester')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'track', 'semester')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'track', 'semester')


@admin.register(Checkoff)
class CheckoffAdmin(admin.ModelAdmin):
    list_display = ('semester', 'assignment', 'student', 'facilitator', 'timestamp')
