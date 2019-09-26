from django.shortcuts import render, redirect, get_object_or_404
from main.models import Issue, Type, Status
from django.http import HttpResponseRedirect
from main.forms import IssueForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,  DeleteView

# Create your views here.

class IssueListView(ListView):
    model = Issue
    template_name = 'index.html'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_view.html'

class IssueCreateView(CreateView):
   model = Issue
   form_class = IssueForm
   template_name = 'add_issue.html'
   success_url = reverse_lazy('index')    

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'del_issue.html'
    success_url = reverse_lazy('index')
