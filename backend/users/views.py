from django.shortcuts import render,reverse,HttpResponseRedirect
from .forms import RegistrationForm,AuthtorizationForm,ProfileForm
from django.contrib import auth
from .models import User
from product.models import HeaderThings
# Create your views here.

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product:main'))

    else:
        form = RegistrationForm()
    things = HeaderThings
    context = {
        'form':form,
        'things':things
    }
    return render(request,"users/registration.html", context=context)

def authtorization(request):
    if request.method == "POST":
        form = AuthtorizationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('product:main'))

    form = AuthtorizationForm()
    things = HeaderThings
    context = {
        'form': form,
        'things':things
    }
    return render(request, 'users/sign-up.html', context=context)

def profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProfileForm(data=request.POST)
            if form.is_valid():
                my_model = User.objects.get(username=request.user.username)
                my_model.first_name = form.data['first_name']
                my_model.last_name = form.data['last_name']
                my_model.save()
            form = User.objects.get(username=request.user.username)
            things = HeaderThings
            context = {
                    "user": form,
                    "things":things
                }
            return render(request, 'users/profile.html', context=context)
        else:
            return HttpResponseRedirect(reverse('users:auth'))

    form = User.objects.get(username = request.user.username)
    things = HeaderThings
    context = {
            "user":form,
            'things':things
        }
    return render(request,'users/profile.html',context=context)