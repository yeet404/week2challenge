from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("", views.index, name="index"),
    # path("balance/", views.bal, name="bal"),
    path("transaction/", views.transaction, name="transaction")
]