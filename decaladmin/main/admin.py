from django.contrib import admin


from .models import Semester, Facilitator, Student, Assignment, Checkoff, Attendance

admin.site.register(Semester)


@admin.register(Facilitator)
class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('username', 'semester')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'sid', 'track', 'semester')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'track', 'semester')


@admin.register(Checkoff)
class CheckoffAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'facilitator', 'timestamp')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'semester')
