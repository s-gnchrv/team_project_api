from django.contrib import admin

# Register your models here.
from myapp import models


class ViolationAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(models.Profile)
admin.site.register(models.Project)
admin.site.register(models.Organization)
admin.site.register(models.ViolationType)
admin.site.register(models.Violation, ViolationAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Attachment)
