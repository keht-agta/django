from django.contrib import admin

from .models import Student, Teacher

class TeachershipInline(admin.TabularInline):
    model = Student.teacher.through
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display = ['id','name','teacher','group']
    list_display = ['id', 'name', 'group']
    inlines = [TeachershipInline,]
    exclude = ('teacher',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeachershipInline, ]
    list_display = ['id', 'name','subject',]

    pass
