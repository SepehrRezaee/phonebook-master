from rest_framework import generics, viewsets, permissions, mixins
from rest_framework.permissions import IsAuthenticated

# from .serializers import EntrySerializers
import logging

import weasyprint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .forms import EntryForm
from .models import Entry
from .serializers import EntrySerializers

logger = logging.getLogger(__name__)


class ShowPhoneNumbers(ListView):
    model = Entry
    template_name = 'phones/show_phone_book.html'
    logger.info("your list contacts is totally true")

    def get_queryset(self):
        if self.request.user.is_authenticated:
            logger.info(f'{self.request.user} is authenticated')
            return Entry.objects.filter(username=self.request.user)
        if not self.request.user.is_authenticated:
            logger.warning("Didn't login")


class AddPhoneNumber(CreateView):
    model = Entry
    template_name = 'phones/add_entry.html'
    success_url = reverse_lazy('phones:show')

    fields = [
        'username',
        'first_name',
        'last_name',
        'phone_number',
    ]

    def get_queryset(self):
        qs = self.request.user
        logger.info(
            f'a contact in the name {self.request.first_name} {self.request.last_name} is added to phone book by {self.request.user};')
        return require_GET.usename.filter(username=qs)


class UpdatePhoneBook(UpdateView):
    form_class = EntryForm
    template_name = "phones/edit_entry.html"
    success_url = reverse_lazy('phones:show')

    def get_queryset(self):
        queryset = Entry.objects.all()
        logger.warning(
            f'a contact is edited by {self.request.user};')
        return queryset


class DeletePhoneBook(DeleteView):
    model = Entry
    template_name = 'phones/entry_confirm_delete.html'
    success_url = reverse_lazy('phones:show')


def find_entry(request):
    """
    Finds a phonebook entry
    """
    phone_number = request.GET.get('num', None)
    type_search = request.GET.get('type_search')
    print("type_search", type_search)
    qs = None

    if not phone_number:
        return JsonResponse({'success': False, 'error': 'No number specified.'}, status=400)

    if type_search == 'contains':
        qs = Entry.objects.filter(phone_number__contains=phone_number, username=request.user)
        print(type_search)
    if type_search == 'startswith':
        qs = Entry.objects.filter(phone_number__startswith=phone_number, username=request.user)
        print(type_search)
    if type_search == 'endswith':
        qs = Entry.objects.filter(phone_number__endswith=phone_number, username=request.user)
        print(type_search)
    if type_search == 'exact':
        qs = Entry.objects.filter(phone_number__exact=phone_number, username=request.user)
        print(type_search)

    request.session['action'] = [f'search type: {type_search}\nnumber search: {phone_number}']
    print(qs)

    return JsonResponse(
        {
            'results': list(
                qs.values()
            ),
            'count': qs.count()
        }
        , status=200
    )


@require_GET
def show_search_form(request):
    """
    Show the search form page
    """
    return render(request, 'phones/search.html')


"""
DRF Views
"""


class PhoneBookViewSets(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    filter_fields = (
        'phone_number',
        'first_name',
        'last_name',
    )

    def get_queryset(self):
        qs = Entry.objects.filter(username=self.request.user)
        return qs


class PrintPhoneNumber(DetailView):
    model = models.Entry

    def get(self, request, *args, **kwargs):
        # Call parents as normal
        g = super(PrintPhoneNumber, self).get(request, *args, **kwargs)

        # Get the rendered content and pass it to w-easy-print
        rendered_content = g.rendered_content
        pdf = weasyprint.HTML(string=rendered_content).write_pdf()

        # Create a new http response with pdf mime type
        response = HttpResponse(pdf, content_type='application/pdf')
        logger.info("Your print PDF mode is working")
        return response

# class PhoneNumberShow(generics.ListAPIView):
#     queryset = models.Entry.objects.all()
#     serializer_class = EntrySerializers
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(username=self.request.user)
#         return qs
#
#
# class PhoneNumberCreate(generics.CreateAPIView):
#     queryset = models.Entry.objects.all()
#     serializer_class = EntrySerializers
#     permission_classes = [IsAuthenticated]
#
#
# class PhoneNumberUpdate(generics.UpdateAPIView):
#     queryset = models.Entry.objects.all()
#     serializer_class = EntrySerializers


# class PhoneNumberUpdate(generics.ListCreateAPIView):
#     queryset = models.Entry.objects.all()
#     serializer_class = EntrySerializers
#     permission_classes = [IsAuthenticated]
#
#     def partial_update(self, request):
#         queryset = self.get_queryset()
#         serializer = EntrySerializers(queryset, many=True)
#         return Response(serializer.data)
