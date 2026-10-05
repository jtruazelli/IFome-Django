from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .forms import LoginForm


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('admin:index')

    else:
        form = LoginForm(request=request)

    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')