from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "accounts"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
	path('logout/', views.LogoutView.as_view(), name="logout"),
	path('hall/', views.HallListView.as_view(), name="hall"),
	path('hall/modal/create', views.ModalHallCreateView.as_view(), name="modal_create_hall"),
	path('hall/modal/<int:pk>/update', views.ModalHallUpdateView.as_view(), name="modal_update_hall"),
	path('hall/modal/<int:pk>/delete', views.ModalHallDeleteView.as_view(), name="modal_delete_hall"),
]

router = DefaultRouter()
router.register(r'public-hall', views.ModalHallApiView,basename="public-hall")