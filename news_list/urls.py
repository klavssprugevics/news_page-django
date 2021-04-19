from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "news_list"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('post/<slug:slug>', views.post, name="single"),
    path('add', views.new_post, name="new_post"),
]