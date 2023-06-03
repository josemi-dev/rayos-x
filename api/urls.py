"""
URL configuration for ProyectoApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from rest_framework import routers
from api.views import PacienteViewSet, Medico_ResponsableViewSet, Tecnico_ResponsableViewSet, EquipoViewSet, UserViewSet, LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
router = routers.DefaultRouter()
router.register('paciente', PacienteViewSet)
router.register('medico_responsable', Medico_ResponsableViewSet)
router.register('tecnico_responsable', Tecnico_ResponsableViewSet)
router.register('equipo', EquipoViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
] + router.urls
