from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(ProjectMember)
admin.site.register(TaskAssignee)
admin.site.register(Comment)
admin.site.register(Notification)
