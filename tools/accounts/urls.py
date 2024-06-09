from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
		path('logout/', views.LogoutView.as_view(), name="logout"),
		path('hall/', views.HallListView.as_view(), name="hall"),
		path('hall/modal/create', views.ModalHallCreateView.as_view(), name="modal_create_hall"),
]
