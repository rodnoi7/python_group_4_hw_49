from django import forms
from main.models import Issue, Type, Status

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'issue_type']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['issue_type']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']