from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı', 'autofocus': True})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Parola'})


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Parola'})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Parola (Tekrar)'})
        self.fields['username'].widget = widgets.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'})
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['email'].required = True
        self.fields['first_name'].widget = widgets.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ad'})
        self.fields['first_name'].required = True
        self.fields['last_name'].widget = widgets.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Soyad'})
        self.fields['last_name'].required = True
