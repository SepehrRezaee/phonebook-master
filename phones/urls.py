from django.urls import path
from . import views
from .views import ShowPhoneNumbers, AddPhoneNumber, UpdatePhoneBook, DeletePhoneBook

app_name = 'phones'
urlpatterns = [
    path('', ShowPhoneNumbers.as_view(), name='show'),
    path('create/', AddPhoneNumber.as_view(), name='create'),
    path('edit/<int:pk>', UpdatePhoneBook.as_view(), name='edit'),
    path('<pk>/delete/', DeletePhoneBook.as_view(), name='delete'),
    path('find/', views.find_entry, name='find'),
    path('search/', views.show_search_form, name='search'),
    path('print/<int:pk>/', views.PrintPhoneNumber.as_view(), name='print-phone'),
]
