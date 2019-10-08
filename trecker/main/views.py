from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from main.forms import IssueForm, TypeForm, StatusForm
from django.urls import reverse_lazy, reverse
from main.models import Issue, Type, Status
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
    model = Issue
    template_name = 'del_issue.html'
    success_url = reverse_lazy('index')

class IssueUpdateView(View):
    form_class = IssueForm
    template_name = 'update_issue.html'
    model = Issue

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(instance=issue)
        context = {
            'form': form,
            'issue': issue
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(instance=issue, data=request.POST)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        form.save()
        return redirect('view', pk=kwargs.get('pk'))

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

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
    form_class = StatusForm
    template_name = 'update_status.html'
    success_url = reverse_lazy('status_list')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'del_status.html'
    success_url = reverse_lazy('status_list')

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'update_type.html'
    success_url = reverse_lazy('type_list')

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'del_type.html'
    success_url = reverse_lazy('type_list')