from django.urls import path
from . import views

urlpatterns = [
    path("", views.TestView.as_view()),
    path("keyword/", views.KeywordSearch.as_view()),
]