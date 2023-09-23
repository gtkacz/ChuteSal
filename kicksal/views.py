from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from kicksal.models import *
from kicksal.serializers import *


class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = (AllowAny,)


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = (AllowAny,)


class QuadraViewSet(ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer
    permission_classes = (AllowAny,)


class CampeonatoViewSet(ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
    permission_classes = (AllowAny,)


class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (AllowAny,)


class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    permission_classes = (AllowAny,)


class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = (AllowAny,)
