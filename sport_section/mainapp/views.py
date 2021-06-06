from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from mainapp.models import SectionView, Sportsman
from mainapp.forms import SectionViewForm


def index(request):
    context = {
        'page_title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def section_list(request):
    sections = SectionView.objects.all()
    context = {
        'sections': sections,
        'page_title': 'Спортивные секции'
    }
    return render(request, 'mainapp/sections.html', context)


def sportsman_page(request, sections_pk):
    sportsmans = Sportsman.objects.filter(sections_id=sections_pk)
    context = {
        'sportsmans': sportsmans,
        'page_title': 'Спортсмены'
    }
    return render(request, 'mainapp/sportsman_page.html', context)


def create_group(request):
    if request.method == 'POST':
        form = SectionViewForm(request.POST)
        if form.is_valid():
            # form.save()
            return HttpResponseRedirect(reverse('mainapp:sections'))
    else:
        form = SectionViewForm()
    context = {
        'title': 'Добавить секции',
        'form': form,
    }
    return render(request, 'mainapp/section_add.html', context)
