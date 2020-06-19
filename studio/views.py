from django.shortcuts import render
from .models import Services, About, Slider, Gallery


def index(request):
    services = Services.objects.all()
    sliders = Slider.objects.all()

    return render(request, 'index.html', {'services': services,
                                          'sliders': sliders})


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery': gallery})


def about(request):
    about_me = About.objects.filter(id=1)

    return render(request, 'about.html', {'about_me': about_me})
