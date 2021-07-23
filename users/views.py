from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions

from users.serializers import UserSerializer


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('phones:show')


class Logout(LogoutView):
    template_name = 'phones/show_phone_book.html'
    success_url = reverse_lazy('phones:show')


"""
DRF View
"""


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
