from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import Login, Logout

app_name = 'users'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
