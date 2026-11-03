from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
    def get(self, request,*args,**kwargs):
        return render(request, "index.html")

class HabilidadesView(View):
    def get(self, request,*args,**kwargs):
        return render(request, "habilidades.html")

class ProyectosView(View):
    def get(self, request,*args,**kwargs):
        return render(request, "proyectos.html")
