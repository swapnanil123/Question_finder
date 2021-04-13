from django.contrib import admin
from .models import Subjects, Papers, QuestionPaper, Semester

# Register your models here.

admin.site.register(Subjects)
admin.site.register(Papers)
admin.site.register(QuestionPaper)
admin.site.register(Semester)
