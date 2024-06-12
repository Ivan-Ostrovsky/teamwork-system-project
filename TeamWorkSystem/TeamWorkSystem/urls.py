"""
URL configuration for TeamWorkSystem project.

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
from django.urls import path, include
from knox import views as knox_views
from staff.views import LoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')), # вход в систему в просматриваемый API - Browsable API
    path('api/v1/', include('staff.urls')),
    path('api/v1/', include('news.urls')),

    path(r'api/v1/login/', LoginView.as_view(), name='knox_login'), # конечная точка входа
    path(r'api/v1/logout/', knox_views.LogoutView.as_view(), name='knox_logout'), # конечная точка выхода
    path(r'api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'), # конечная точка токина

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
