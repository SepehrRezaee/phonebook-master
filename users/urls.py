from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import Login, Logout

router = DefaultRouter()
router.register('users', views.UserViewSet)

app_name = 'users'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('api/v1/', include(router.urls)),
]
