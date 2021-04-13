from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here


class Subjects(models.Model):
    subjectName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    streamName = models.CharField(
        max_length=50, blank=False, unique=False, default='')


class Papers(models.Model):
    paperName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    subjectName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    semesterName = models.CharField(
        max_length=50, blank=False, unique=False, default='')


class Semester(models.Model):
    semesterName = models.CharField(
        max_length=50, blank=False, unique=False, default='')


class QuestionPaper(models.Model):
    # questionPaperURL = models.CharField(max_length=550, blank=False, unique=False, default='')
    # questionPaperName = models.CharField(max_length=350, blank=False, unique=False, default='')
    questionPaperName = models.FileField(blank=False)
    subjectName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    paperName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    courseName = models.CharField(
        max_length=50, blank=False, unique=False, default='')
    yearOfQuestions = models.CharField(
        max_length=50, blank=False, unique=False, default='')

    def delete(self, *args, **kwargs):
        self.questionPaperName.delete()
        super().delete(*args, **kwargs)
