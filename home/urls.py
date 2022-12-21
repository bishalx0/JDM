from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home"),
    path("mission", views.mission, name="mission"),
    path("gallery", views.gallery, name="gallery"),
    path("chairman-message", views.chairman_message, name="chairman_message"),
    path("about-us", views.about_us, name="about_us"),
    path("contact-us", views.contact_us, name="contact_us"),
]
