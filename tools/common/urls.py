from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('settings', views.SettingsView.as_view(), name="settings"),
]

