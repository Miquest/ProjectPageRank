from django.urls import path
from . import views

urlpatterns = [
    path("", views.TestView.as_view()),
    path("crawl/", views.Crawl.as_view()),
]