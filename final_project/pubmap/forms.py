from django import forms
from django.contrib.auth.models import User

from pubmap.models import Pub, Review


class AddPubForm(forms.ModelForm):
    class Meta:
        model = Pub
        fields = '__all__'
        labels = {
            'name': 'Nazwa knajpy',
            'formatted_address': 'Adres',
            'formatted_phone_number': 'Numer telefonu',
            'website': 'Adres strony'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'formatted_address': forms.TextInput(attrs={'class': 'form-control'}),
            'formatted_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'place_id': forms.HiddenInput(),
            'open_now': forms.HiddenInput(),
            'opening_hours': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'rating': 'Ocena',
            'pub': 'Wybierz knajpę',
            'comment': 'Komentarz'
        }
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={"class": "form-control"}),
            'pub': forms.Select(attrs={"class": "form-control"}),
            'author': forms.HiddenInput()
        }


class LogInForm(forms.Form):
    username = forms.CharField(label="Login", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)


class AddUserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Hasło')
    password_again = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Hasło ponownie')

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {
            'username': 'Nazwa użytkownika',
            'email': 'Adres email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }

