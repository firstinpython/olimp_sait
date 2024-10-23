from django.urls import path
from .views import ServiceAPIList,ServiceAPIRetriveUPDATE

urlpatterns = [
    path('',ServiceAPIList.as_view()),
    path('<int:pk>/',ServiceAPIRetriveUPDATE.as_view())
]