from django.urls import path
from . import views

app_name = "animals"

urlpatterns = [
    path('all/', views.AnimalsView.as_view(), name="all")
]
