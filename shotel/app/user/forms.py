from django import forms
from shotel.app.user.models import User



class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            "username": forms.TextInput(attrs={'placeholder': "name",}),
            "email": forms.TextInput(attrs={'placeholder': "Ex: example@gmail.com",}),
            "password": forms.PasswordInput(attrs={'placeholder': "password",}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Entrer votre nom:",
        widget=forms.TextInput(attrs={"placehoder":"username"})
    )
    password = forms.CharField(
        label="Entrer le mot de passe:",
        widget=forms.PasswordInput(
        attrs={
            "placeholder":"password",
            "id": "password"
        }
    ))