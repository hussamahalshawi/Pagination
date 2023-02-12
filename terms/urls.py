from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllKeywordsView.as_view(),name="home"),
    path(
        "terms",
        views.KeywordListView.as_view(),
        name="terms"
    ),
    path(
        "terms/<int:page>",
        views.listing,
        name="terms-by-page"
    ),
    path(
        "terms.json",
        views.listing_api,
        name="terms-api"
    ),
]