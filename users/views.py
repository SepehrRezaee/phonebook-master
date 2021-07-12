from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('phones:show')


class Logout(LogoutView):
    template_name = 'phones/show_phone_book.html'
    success_url = reverse_lazy('phones:show')
