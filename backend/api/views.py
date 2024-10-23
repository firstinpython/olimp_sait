from django.shortcuts import render
from product.models import Services, Time, HeaderThings, Review
# Create your views here.
from .serializer import ServiceSerializer, HeaderThingsSerializer, ReviewSerializer, TimeSerializer, PostsSerializer
from rest_framework import generics


class ServiceAPIList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ServiceAPIRetriveUPDATE(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ServiceAPIRetriveDelete(generics.RetrieveDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


# ---
class TimeApiList(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeAPIRetriveUpdate(generics.RetrieveAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeAPIRetriveDelete(generics.RetrieveDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


# ----
class HeaderApiList(generics.ListCreateAPIView):
    queryset = HeaderThings.objects.all()
    serializer_class = HeaderThingsSerializer


class HeaderAPIRetriveUpdate(generics.RetrieveAPIView):
    queryset = HeaderThings.objects.all()
    serializer_class = HeaderThingsSerializer


class HeaderAPIRetriveDelete(generics.RetrieveDestroyAPIView):
    queryset = HeaderThings.objects.all()
    serializer_class = HeaderThingsSerializer


# ----
class ReviewApiList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPIRetriveUpdate(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPIRetriveDelete(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
