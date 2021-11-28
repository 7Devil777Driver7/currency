from currency.forms import SourceForm
from currency.models import ContactUs, Rate, Source

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def contact_us(request):
    contacts = ContactUs.objects.all()

    context = {
        'contacts': contacts,
    }
    return render(request, 'contact_us.html', context)


def source_list(request):
    sources = Source.objects.all()

    context = {
        'sources': sources,
    }
    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')

    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form,
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):

    instance = get_object_or_404(Source, id=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')

    elif request.method == 'GET':
        form = SourceForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    instance = get_object_or_404(Source, id=pk)

    if request.method == 'GET':
        context = {
            'instance': instance,
        }
        return render(request, 'source_delete.html', context)

    elif request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/source-list/')
