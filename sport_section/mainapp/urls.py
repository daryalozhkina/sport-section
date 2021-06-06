import mainapp.views as mainapp

from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('sections/', mainapp.section_list, name='section_list'),
    path('sections/sportsmans/<int:sections_pk>/', mainapp.sportsman_page, name='sportsman_page'),
    ]