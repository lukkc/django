from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from cash.models import Cash
from cash.forms import (
    CashForm,
    CashChangeForm
)


class CashListView(ListView):
    template_name = 'cash/index.html'
    context_object_name = 'cashs'
    extra_context = {'form': CashForm()}

    def get_queryset(self):
        user = self.request.user
        cash_list = Cash.objects.all()
        if user.is_authenticated:
            cash_list = Cash.objects.filter(user=user)
        self.extra_context.update({
            'total_price': cash_list.aggregate(total=Sum('price'))['total']
        })
        return cash_list


class CashCreateView(LoginRequiredMixin, CreateView):
    model = Cash
    template_name = 'cash/index.html'
    form_class = CashForm
    success_url = reverse_lazy('cash:index')
    queryset = Cash.objects.all()
    extra_context = {
        'cashs': queryset
    }

    def get_form_kwargs(self):
        kwargs = {}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'user': self.request.user
            })
        return kwargs


class CashEditView(LoginRequiredMixin, UpdateView):
    model = Cash
    template_name = 'cash/edit.html'
    form_class = CashChangeForm
    success_url = reverse_lazy('cash:index')


class CashDeleteView(LoginRequiredMixin, DeleteView):
    model = Cash
    template_name = 'cash/delete.html'
    success_url = reverse_lazy('cash:index')
    context_object_name = 'cash'


