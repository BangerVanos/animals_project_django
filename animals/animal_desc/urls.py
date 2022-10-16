from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('all/', views.AnimalsView.as_view(), name="all"),
    path('<str:slug>-<int:anim_id>/', views.AnimalView.as_view(), name="animal_desc"),
]
