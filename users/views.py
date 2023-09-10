
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from users.models import User



class RegisterUser(CreateView):
    model = User

    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация'
    }



class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('users:login')


class ListUsersView(ListView):
    model = User
    template_name = 'users/list_users.html'
    extra_context = {
        'title': 'Список пользователей сервиса'
    }




class ProfileUser(UpdateView):
    model = User
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'title': 'Профиль'
    }


class BlockUser(UpdateView):

    model = User
    template_name = 'users/block_user.html'
    extra_context = {
        'title': 'Блокировка пользователя'
    }
