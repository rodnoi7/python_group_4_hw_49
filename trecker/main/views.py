from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from main.forms import IssueForm, TypeForm, StatusForm, ProjectForm
from django.urls import reverse_lazy, reverse
from main.models import Issue, Type, Status, Project
from django.shortcuts import render, redirect, get_object_or_404

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
    template_name = 'del_issue.html'
    model = Issue
    context_key = 'issue'
    success_url = reverse_lazy('index')

class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'update_issue.html'
    form_class = IssueForm
    context_key = 'issue'

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})

class TypeListView(ListView):
    model = Type
    template_name = 'type_list.html'

class TypeCreateView(CreateView):
   model = Type
   form_class = TypeForm
   template_name = 'add_type.html'
   success_url = reverse_lazy('type_list')

class StatusListView(ListView):
    model = Status
    template_name = 'status_list.html'

class StatusCreateView(CreateView):
   model = Status
   form_class = StatusForm
   template_name = 'add_status.html'
   success_url = reverse_lazy('status_list')

class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'update_status.html'
    form_class = StatusForm
    context_key = 'status'

    def get_success_url(self):
        return reverse('status_list')

class StatusDeleteView(DeleteView):
    template_name = 'del_status.html'
    model = Status
    context_key = 'status'
    success_url = reverse_lazy('status_list')

class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'update_type.html'
    form_class = TypeForm
    context_key = 'type'
    redirect_url = 'type_list'

class TypeDeleteView(DeleteView):
    template_name = 'del_type.html'
    model = Type
    context_key = 'type'
    success_url = reverse_lazy('type_list')

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'

    def get_context_data(self, **kwargs):
        kwargs['projects'] = (Project.objects.filter(status='Active'))
        return super().get_context_data(**kwargs)

class DeactiveProjectListView(ListView):
    model = Project
    template_name = 'deact_projects.html'

    def get_context_data(self, **kwargs):
        kwargs['projects'] = (Project.objects.filter(status='Deactive'))
        return super().get_context_data(**kwargs)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_view.html'

class ProjectCreateView(CreateView):
   model = Project
   form_class = ProjectForm
   template_name = 'add_project.html'
   success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = ProjectForm
    context_key = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class ProjectDeleteView(DeleteView):
    template_name = 'del_project.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('project_list')