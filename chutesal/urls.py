"""chutesal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from kicksal.viewsets import *
from kicksal.views import *

router = routers.DefaultRouter()

router.register(r'unidades', UnidadeViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'quadras', QuadraViewSet)
router.register(r'campeonatos', CampeonatoViewSet)
router.register(r'times', TimeViewSet)
router.register(r'jogadores', JogadorViewSet)
router.register(r'jogos', JogoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),
    path('is_admin', home, name='home'),
    path('campeonato/', campeonatos, name='campeonatos'),
    path('create_championship/', create_championship, name='create_championship'),
    path('edit_championship/', edit_championship, name='edit_championship'),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
