from django.contrib import admin
from django.urls import path
from.views import HomeView
from.views import HabilidadesView
from.views import ProyectosView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('habilidades/',HabilidadesView.as_view(),name='habilidades'),
    path('proyectos/',ProyectosView.as_view(),name='proyectos')
]

