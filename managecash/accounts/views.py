from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from django.urls import reverse_lazy


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = 'cash:index'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AccountsLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

