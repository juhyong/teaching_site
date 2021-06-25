from django.contrib import admin
from curriculum.models import Standard, Subject, Lesson, Notification
# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Notification)
