from . import views
from django.urls import path

urlpatterns = [
    path("", views.Tuner, name="Home"),
    path("contribute", views.Contribute, name="contribute"),
    path("saveform", views.dataSubmission, name="saveform")
]
