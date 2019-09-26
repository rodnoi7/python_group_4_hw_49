from django.db import models

# Create your models here.

class Issue(models.Model):
	summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
	description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
	status = models.ForeignKey('Status', on_delete=models.PROTECT, related_name='issue', verbose_name='Статус')
	issue_type = models.ForeignKey('Type', on_delete=models.PROTECT, related_name='issue', verbose_name='Тип')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

class Type(models.Model):
    issue_type = models.CharField(max_length=20, verbose_name='Тип задачи')

    def __str__(self):
        return "%s" %  self.issue_type

class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус задачи')

    def __str__(self):
        return "%s" %  self.status
