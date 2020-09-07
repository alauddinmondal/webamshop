import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed
# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out. Feel free to login again!')
    return HttpResponseRedirect('%s' %(reverse('auth_login')))

def login_view(request):
    form = LoginForm(request.POST or None)
    btn = 'Login'
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        # user.emailconfirmed.activate_user_email()
        messages.success(request, 'Successfully logged in. Welcome back!')
        return HttpResponseRedirect('/')
    context = {'form':form, 'btn_submit':btn}
    return render(request, 'form.html', context)

def registration_view(request):
    btn = 'Join'
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        messages.success(request, 'Successfully registered. Please confirm your email.')
        return HttpResponseRedirect('/')
        # new_user.first_name = 'Alauddin'
        # print('This is register form')

    context = {'form':form, 'btn_submit':btn}
    return render(request, 'form.html', context)

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print('Activation key is real')
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            messages.success(request, 'There was an error with your request.')
            return HttpResponseRedirect('/')

        if instance is not None and not instance.confirmed:
            page_message = 'Confirmation successfull. Welcome back!'
            instance.confirmed = True
            instance.activation_key = 'Confirmed'
            instance.save()
            messages.success(request, 'Successfully confirmed. Please login.')
        elif instance is not None and instance.confirmed:
            page_message = 'Already confirmed'
            messages.success(request, 'Already confirmed.')
        else:
            page_message = ''

        context = {'page_message':page_message}
        template = 'accounts/activation_complete.html'
        return render(request, template, context)
    else:
        raise Http404
