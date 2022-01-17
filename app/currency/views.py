from currency.forms import ContactUsForm, RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()
    template_name = 'rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailsView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_detail.html'


class ContactUsView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contact-us')
    queryset = ContactUs.objects.all()
    template_name = 'contactus_create.html'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        recipient = settings.EMAIL_HOST_USER
        subject = 'User ContactUs'
        body = f'''
        Request From: {cleaned_data['name']}
        User email: {cleaned_data['email_from']}
        Subject: {cleaned_data['subject']}

        Body: {cleaned_data['message']}
        '''
        send_mail(
            subject,
            body,
            settings.DEGAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False
        )

        redirect = super().form_valid(form)
        return redirect


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name'
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset
