from django.shortcuts import render
from django.http import HttpResponse
from classView import models
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


# class Index(View):
#     def get(self, request):
#         return HttpResponse('GO')


# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'Django Class Base View'
#         return context


class List(ListView):
    context_object_name = 'data_list'
    model = models.Data
    template_name = 'index.html'


class Detail(DetailView):
    context_object_name = 'data_info'
    model = models.Data
    template_name = 'detail.html'


class Add(CreateView):
    model = models.Data
    template_name = 'add.html'
    fields = ['name', 'email', 'address']


class Payment(CreateView):
    model = models.Payment
    template_name = 'payment.html'
    fields = ['employee', 'amount', 'status']


class Update(UpdateView):
    model = models.Data
    template_name = 'add.html'
    fields = ['name', 'address']


class Delete(DeleteView):
    model = models.Data
    success_url = reverse_lazy('index')
    template_name = 'delete.html'

