from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import JobApplication


class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = 'applications/application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        
        queryset = JobApplication.objects.filter(user=self.request.user)

        
        query = self.request.GET.get('q', '').strip()
        status_filter = self.request.GET.get('status', '').strip()

        
        if query:
            queryset = queryset.filter(
                Q(company_name__icontains=query) | Q(job_title__icontains=query)
            )

        
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['status_choices'] = JobApplication.Status.choices
        context['selected_status'] = self.request.GET.get('status', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context


class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    template_name = 'applications/application_form.html'
    fields = ['company_name', 'job_title', 'job_url', 'status', 'applied_date', 'notes']
    success_url = reverse_lazy('applications:application_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    template_name = 'applications/application_form.html'
    fields = ['company_name', 'job_title', 'job_url', 'status', 'applied_date', 'notes']
    success_url = reverse_lazy('applications:application_list')

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)


class JobApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    template_name = 'applications/application_confirm_delete.html'
    success_url = reverse_lazy('applications:application_list')

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)