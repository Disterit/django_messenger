from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from .models import CustomUser


class AccountDetailView(DetailView):
    model = CustomUser
    context_object_name = 'account'
    template_name = 'account/personal_page.html'


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user in None:
            login(request, user)
            return redirect('account/personal_page')

        else:
            error_massage = 'Неправильный email или пароль'
            return render(request, 'home.html', {'error_message': error_massage})

    else:
        return render(request, 'home.html')
