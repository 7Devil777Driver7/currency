import uuid

from accounts.models import User

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


class SignUpForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()

        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords should match!')
        return cleaned_data

    def save(self, commit=True):
        # create python object without saving to database
        instance = super().save(commit=False)

        instance.set_password(self.cleaned_data['password1'])
        instance.is_active = False
        instance.username = str(uuid.uuid4())
        instance.save()
        self._send_email()

        return instance

    def _send_email(self):
        path = reverse('accounts:activate', args=(self.instance.username, ))
        subject = 'Activate your account!'
        body = f'''
        Hi!

        Here is you activation link: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{path}
        '''

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [self.instance.email],
            fail_silently=False
            )
