from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home/index.html")


def mission(request):
    return render(request, "home/mission.html")


def chairman_message(request):
    return render(request, "home/chairman_message.html")


def gallery(request):
    return render(request, "home/gallery.html")


def about_us(request):
    return render(request, "home/about_us.html")


def contact_us(request):
    return render(request, "home/contact_us.html")
