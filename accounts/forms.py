from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label='Пароль', strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label='Запомнить меня', required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError("Пароль не верный")

        return password


class EmailForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label='Почта')

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError("Не верный адрес почты")

        if not user.is_active:
            raise ValidationError("Аккаунт не активен")

        self.user_cache = user

        return email


class SignInViaEmailForm(SignIn, EmailForm):
    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email', 'password', 'remember_me']
        return ['email', 'password']


class SignInViaEmailOrUsernameForm(SignIn, EmailForm):
    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email_or_username', 'password', 'remember_me']
        return ['email_or_username', 'password']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label='Почта', help_text="Это поле обязательное")

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError("Этот адрес нельзя использовать")

        return email


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=30, required=False)
    last_name = forms.CharField(label="Фамиля", max_length=150, required=False)
