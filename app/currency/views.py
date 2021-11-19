from currency.models import ContactUs

from django.http.response import HttpResponse


def hello_world(request):
    return HttpResponse('Hello World!')


def contact_us(request):
    contact_messages = ContactUs.objects.all()
    results = []

    for contact in contact_messages:
        results.append(
            f'ID: {contact.id}, Email from: {contact.email_from},' 
            f'Subject: {contact.subject}, Message: {contact.message}<br>'
        )
    return HttpResponse(str(results))
