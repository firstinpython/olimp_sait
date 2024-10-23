from django.urls import path
from .views import main_page,services

app_name = "product"

urlpatterns = [
    path("",main_page,name = "main"),
    path("services/",services,name='service')
]