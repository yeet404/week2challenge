from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("balance/", views.bal, name="bal")
]