from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ans/', views.AnserView.as_view(), name='ans'),
]