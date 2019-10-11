from django import forms
from main.models import Issue, Type, Status, Project

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_at']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['issue_type']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']