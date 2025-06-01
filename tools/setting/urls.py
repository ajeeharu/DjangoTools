"""
URL configuration for tools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import router as accounts_router
from accounting.urls import router as accounting_router


urlpatterns = [
	# apli
	path('',include("common.urls")),
	path('accounts/', include("accounts.urls")),
	path('accounting/',include("accounting.urls")),	
 	path('event_manager/',include("event_manager.urls")),
    # api
    path('api/account/', include(accounts_router.urls)),
    path('api/accounting/', include(accounting_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # admin
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)