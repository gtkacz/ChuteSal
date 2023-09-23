from rest_framework.serializers import ModelSerializer, SerializerMethodField

from kicksal.models import *


class UnidadeSerializer(ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

    unidade = UnidadeSerializer()


class QuadraSerializer(ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'

    unidade = UnidadeSerializer()


class CampeonatoSerializer(ModelSerializer):
    class Meta:
        model = Campeonato
        fields = '__all__'

    unidade = UnidadeSerializer()
    cup_manager = FuncionarioSerializer()
    times = SerializerMethodField()

    def get_times(self, obj: Campeonato):
        times = Time.objects.filter(campeonato=obj)
        return TimeSerializer(times, many=True).data


class TimeSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

    campeonato = SerializerMethodField()
    pontos = SerializerMethodField()
    saldo_de_gols = SerializerMethodField()

    def get_campeonato(self, obj: Time) -> dict[int, str]:
        return {obj.campeonato.pk: obj.campeonato.nome}

    def get_pontos(self, obj: Time) -> int:
        game_scores = self.__get_game_scores(obj)
        victories = len([score for score in game_scores if score > 0])
        ties = len([score for score in game_scores if score == 0])

        return victories*3 + ties

    def get_saldo_de_gols(self, obj: Time) -> int:
        return sum(self.__get_game_scores(obj))

    def __get_game_scores(self, obj: Time) -> list[int]:
        games_as_home = obj.time1.all()
        games_as_away = obj.time2.all()
        result = []
        result += [
            (game.resultado_time1 - game.resultado_time2) for game in games_as_home
        ]
        result += [
            (game.resultado_time2 - game.resultado_time1) for game in games_as_away
        ]
        return result


class JogadorSerializer(ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

    time = TimeSerializer()


class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

    time1 = TimeSerializer()
    time2 = TimeSerializer()
    quadra = QuadraSerializer()
    campeonato = CampeonatoSerializer()
