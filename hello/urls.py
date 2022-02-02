from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("tepela", views.tepela, name="tepela"),
    path("<str:name>", views.greet, name="greet"),
]
