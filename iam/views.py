# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import IAMRoleRequestForm
from .models import IAMRoleRequest


class IAMRoleRequestCreateView(LoginRequiredMixin, CreateView):
    model = IAMRoleRequest
    form_class = IAMRoleRequestForm
    template_name = 'iam/request_form.html'
    success_url = reverse_lazy('iam:request-list')

    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form)

class IAMRoleRequestListView(LoginRequiredMixin, ListView):
    model = IAMRoleRequest
    template_name = 'iam/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return IAMRoleRequest.objects.filter(requested_by=self.request.user).order_by('-created_at')
