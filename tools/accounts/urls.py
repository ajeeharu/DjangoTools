from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SignupView,LoginView,LogoutView,HallListView,ModalHallCreateView,ModalHallDeleteView,ModalHallUpdateView,ModalHallApiView

app_name = "accounts"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
		path('logout/', LogoutView.as_view(), name="logout"),
		path('hall/', HallListView.as_view(), name="hall"),
		path('hall/modal/create', ModalHallCreateView.as_view(), name="modal_create_hall"),
		path('hall/modal/<int:pk>/update', ModalHallUpdateView.as_view(), name="modal_update_hall"),
		path('hall/modal/<int:pk>/delete', ModalHallDeleteView.as_view(), name="modal_delete_hall"),
]

router = DefaultRouter()
router.register(r'public-hall', ModalHallApiView,basename="public-hall")