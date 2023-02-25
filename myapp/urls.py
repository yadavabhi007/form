from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormData.as_view(), name='formdata'),
    path('data/', views.AllData.as_view(), name='alldata'),
]