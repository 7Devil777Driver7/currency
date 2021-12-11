from currency.models import ContactUs, Rate, Source

from django import forms


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name'
            )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'created',
            'cur_type',
            'source'
            )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message'
            )
