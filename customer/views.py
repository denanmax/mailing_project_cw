from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from customer.models import Customer


# Create your views here.
class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customer/create_customer.html'

    success_url = reverse_lazy('customer:list_customers')
    extra_context = {
        'title': 'Создание клиента'
    }


class ListCustomers(ListView):
    model = Customer
    template_name = 'customer/list_customers.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class DetailCustomer(DetailView):
    model = Customer
    template_name = 'customer/detail.html'
    extra_context = {
        'title': 'Информация о клиенте'
    }


class UpdateCustomer(UpdateView):
    model = Customer
    template_name = 'customer/update_customer.html'
    extra_context = {
        'title': 'Обновление информации о клиенте'
    }


class DeleteCustomerView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:list_customers')
