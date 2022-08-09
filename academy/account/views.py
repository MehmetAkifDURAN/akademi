from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm, NewUserForm
from academyapp.models import CategoryLevelOne
from academyapp.views import getCategories, convertToJson
# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    context = {
        'categories_level_one': convertToJson(getCategories(CategoryLevelOne.objects.all().order_by('order_number')))
    }

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                nextUrl = request.GET.get('next', None)
                if nextUrl is None:
                    return redirect('home_page')
                else:
                    return redirect(nextUrl)
            else:
                return render(request, 'account/login.html', context)
        else:
            return render(request, 'account/login.html', context)
    else:
        form = LoginUserForm()
        context['form'] = form
        return render(request, 'account/login.html', context)


def register_request(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    context = {
        'categories_level_one': convertToJson(getCategories(CategoryLevelOne.objects.all().order_by('order_number')))
    }

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'account/register.html', context)
    else:
        form = NewUserForm()
        context['form'] = form
        return render(request, 'account/register.html', context)


def logout_request(request):
    logout(request)
    return redirect('home_page')
