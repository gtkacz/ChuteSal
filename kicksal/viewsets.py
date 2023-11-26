from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from kicksal.models import *
from kicksal.serializers import *


@method_decorator(csrf_exempt, name='dispatch')
class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class QuadraViewSet(ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class CampeonatoViewSet(ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    permission_classes = (AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = (AllowAny,)
