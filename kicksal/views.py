from django.shortcuts import render
from django.utils import timezone

from kicksal.models import (Campeonato, Funcionario, Jogador, Jogo, Time,
                            Unidade)


def home(request):
    now = timezone.now().date()

    context = {
        'ongoing': Campeonato.objects.filter(data_inicio_divulgacao__lte=now, periodo_jogos_comeco__lte=now, periodo_jogos_fim__gt=now),
        'upcoming': Campeonato.objects.filter(data_inicio_divulgacao__lte=now, periodo_jogos_comeco__gt=now),
        'past': Campeonato.objects.filter(data_inicio_divulgacao__lte=now, periodo_jogos_fim__lt=now)
    }

    return render(request, 'home.html', context)

def campeonatos(request):
    obj = Campeonato.objects.get(pk=request.GET.get('pk'))

    def __get_status(obj: Campeonato) -> str:
        now = timezone.now().date()

        return 'ongoing' if obj.periodo_jogos_comeco <= now and obj.periodo_jogos_fim >= now else 'upcoming' if obj.periodo_jogos_comeco >= now else 'past'
    
    def __get_posicao(obj: Campeonato) -> list[dict[Time, int]]:
        response = []

        times = Time.objects.filter(campeonato=obj)

        for time in times:
            response.append({
                'time': time,
                'pontos': __get_pontos(time),
                'saldo_de_gols': __get_saldo_de_gols(time),
            })

        response.sort(key=lambda x: (x['pontos'], x['saldo_de_gols']), reverse=True)
        return response
    
    def __get_pontos(obj: Time) -> int:
        game_scores = __get_game_scores(obj)
        victories = len([score for score in game_scores if score > 0])
        ties = len([score for score in game_scores if score == 0])

        return victories*3 + ties

    def __get_saldo_de_gols(obj: Time) -> int:
        return sum(__get_game_scores(obj))

    def __get_game_scores(obj: Time) -> list[int]:
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
    
    context = {
        'campeonato': obj,
        'status': __get_status(obj),
        'jogos': Jogo.objects.filter(campeonato=obj).order_by('rodada', 'data', 'horario'),
        'times': Time.objects.filter(campeonato=obj),
        'posicao': __get_posicao(obj)
    }

    return render(request, 'campeonatos.html', context=context)

def create_championship(request):
    context = {
        'unidades': Unidade.objects.all(),
        'cup_managers': Funcionario.objects.all()
    }

    return render(request, 'create_championship.html', context=context)

def edit_championship(request):
    obj = Campeonato.objects.get(pk=request.GET.get('pk'))

    context = {
        'campeonato': obj,
        'jogos': Jogo.objects.filter(campeonato=obj).order_by('rodada', 'data', 'horario'),
        'times': Time.objects.filter(campeonato=obj),
        'jogadores': Jogador.objects.filter(time__in=Time.objects.filter(campeonato=obj)),
        'unidades': Unidade.objects.all(),
        'cup_managers': Funcionario.objects.all()
    }

    return render(request, 'edit_championship.html', context=context)
