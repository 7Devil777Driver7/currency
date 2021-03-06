from accounts.forms import SignUpForm
from accounts.models import User

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class UserActivateView(RedirectView):
    # TODO add django messages
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = User.objects.filter(username=username).first()
        if user:
            user.is_active = True
            user.save(update_fields=('is_active', ))
        url = super().get_redirect_url(*args, **kwargs)
        return url
