from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
    def get(self, request,*args,**kwargs):
        return render(request, "index.html")

class HabilidadesView(View):
    def get(self, request,*args,**kwargs):
        return render(request, "habilidades.html")

class ProyectosView(View):
    def get(self, request, *args, **kwargs):

        proyectos = [
            {
                "nombre": "Estacionamiento Inteligente",
                "descripcion": "Sistema de estacionamiento desarrollado con ESP32.",
                "imagen": "img/estacionamiento.jpg",
            },
            {
                "nombre": "Mi CV con Django",
                "descripcion": "Portafolio personal desarrollado con Django y Bootstrap 5.",
                "imagen": "img/cv.jpg",
            },
            {
                "nombre": "Página de Música",
                "descripcion": "Sitio web responsivo desarrollado con Bootstrap 5.",
                "imagen": "img/musica.jpg",
            },
        ]

        contexto = {
            "proyectos": proyectos
        }

        return render(request, "proyectos.html", contexto)

