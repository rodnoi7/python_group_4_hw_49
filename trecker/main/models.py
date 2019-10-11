from django.db import models

# Create your models here.

class Issue(models.Model):
	summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
	description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
	status = models.ForeignKey('Status', on_delete=models.PROTECT, related_name='issue', verbose_name='Статус')
	issue_type = models.ForeignKey('Type', on_delete=models.PROTECT, related_name='issue', verbose_name='Тип')
	project = models.ForeignKey('Project', null=True, blank=False, on_delete=models.SET_NULL, related_name='issue', verbose_name="Проект")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

	def __str__(self):
		return '%s (%s)' % (self.summary, self.status)

class Project(models.Model):
	ACTIVE = 'Active'
	DEACTIVE = 'Deactive'

	STATUS_CHOICES = (
		(ACTIVE, 'Active'),
		(DEACTIVE, 'Deactive')
	)

	name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название проекта')
	description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус", default=ACTIVE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.name)

class Type(models.Model):
    issue_type = models.CharField(max_length=20, verbose_name='Тип задачи')

    def __str__(self):
        return "%s" % self.issue_type

class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус задачи')

    def __str__(self):
        return "%s" %  self.status
