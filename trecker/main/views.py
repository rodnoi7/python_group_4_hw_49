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

class IssueDeleteView(View):
    delete_settings = False
    form_class = IssueForm
    template_name = 'del_issue.html'
    model = Issue

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        if self.delete_settings:
            context = {
                'issue': issue
            }
            return render(request, self.template_name, context)
        else:
            issue.delete()
            return redirect('index')

    def post(self, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        issue.delete()
        return redirect('index')

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

class StatusUpdateView(View):
    form_class = StatusForm
    template_name = 'update_status.html'
    model = Status

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(instance=status)
        context = {
            'form': form,
            'status': status
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(instance=status, data=request.POST)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        form.save()
        return redirect('status_list')

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

class StatusDeleteView(View):
    delete_settings = False
    form_class = StatusForm
    template_name = 'del_status.html'
    model = Status

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        if self.delete_settings:
            context = {
                'status': status
            }
            return render(request, self.template_name, context)
        else:
            status.delete()
            return redirect('status_list_list.html')

    def post(self, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()

class TypeUpdateView(View):
    form_class = TypeForm
    template_name = 'update_type.html'
    model = Type

    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(instance=type)
        context = {
            'form': form,
            'type': type
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(instance=type, data=request.POST)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        form.save()
        return redirect('type_list')

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

class TypeDeleteView(View):
    delete_settings = False
    form_class = TypeForm
    template_name = 'del_type.html'
    model = Type

    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        if self.delete_settings:
            context = {
                'type': type
            }
            return render(request, self.template_name, context)
        else:
            type.delete()
            return redirect('type_list.html')

    def post(self, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
