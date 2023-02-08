from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllKeywordsView.as_view(),name="home")
]