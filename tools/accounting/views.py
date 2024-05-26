# coding: utf-8

from rest_framework import viewsets, filters
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import PublicHall
# from .serializer import PublicHallSerializer


# class PublicHallViewSet(viewsets.ModelViewSet):
#     queryset = PublicHall.objects.all()
#     serializer_class = PublicHallSerializer




class IndexView(TemplateView,LoginRequiredMixin):
    """ ホームビュー """
    template_name = "accounting/index.html"