from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ShowPhoneNumbers, AddPhoneNumber, UpdatePhoneBook, DeletePhoneBook

router = DefaultRouter()
router.register('phones', views.PhoneBookViewSets)

app_name = 'phones'
urlpatterns = [
    path('', ShowPhoneNumbers.as_view(), name='show'),
    path('create/', AddPhoneNumber.as_view(), name='create'),
    path('edit/<int:pk>', UpdatePhoneBook.as_view(), name='edit'),
    path('<pk>/delete/', DeletePhoneBook.as_view(), name='delete'),
    path('find/', views.find_entry, name='find'),
    path('search/', views.show_search_form, name='search'),
    path('api/v1/', include(router.urls)),
]
