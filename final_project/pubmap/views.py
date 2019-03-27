from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from django.views import View
from django.views.generic import CreateView

from pubmap.forms import AddPubForm, AddReviewForm, AddUserModelForm, LogInForm
from pubmap.models import Pub, Review


class MainPage(View):
    def get(self, request):
        places = Pub.objects.all()
        reviews = Review.objects.order_by('-posted')
        return render(request, 'pubmap/homepage.html', {"places": places, "reviews": reviews})


class AddPub(CreateView):
    form_class = AddPubForm
    model = Pub
    success_url = '/'


class AddReview(CreateView):
    form_class = AddReviewForm
    model = Review
    success_url = '/'


class ShowAllPubs(View):
    def get(self, request):
        pubs = Pub.objects.order_by('name')
        reviews = Review.objects.order_by('-posted')
        return render(request, 'pubmap/showallpubs.html', {"pubs": pubs, "reviews": reviews})


class AddUserView(View):
    def get(self, request):
        form = AddUserModelForm()
        return render(request, 'pubmap/signin.html', {'form': form})

    def post(self, request):
        form = AddUserModelForm(request.POST)
        if form.is_valid():
            user_exists = User.objects.filter(username=form.cleaned_data['username']).exists()
            if user_exists:
                return render(request, 'pubmap/error.html', {'msg': "Już istnieje taki użytkownik"})
            if form.cleaned_data['password'] != form.cleaned_data['password_again']:
                return render(request, 'pubmap/error.html', {'msg': "Hasła są różne"})
            form.cleaned_data.pop('password_again')
            User.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect('/')


class LoginView(View):

    def get(self, request):
        form = LogInForm()
        return render(request, 'pubmap/login.html', {"form": form})

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return render(request, 'pubmap/error.html', {'msg': "Błędne dane logowania"})
        else:
            return render(request, 'pubmap/login.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
