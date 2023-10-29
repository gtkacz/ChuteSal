from django.shortcuts import render
from django.utils import timezone

from kicksal.models import Campeonato


def home(request):
    now = timezone.now().date()

    context = {
        'ongoing': Campeonato.objects.filter(periodo_jogos_comeco__lte=now, periodo_jogos_fim__gte=now),
        'upcoming': Campeonato.objects.filter(periodo_inscricao_comeco__gte=now),
        'past': Campeonato.objects.filter(periodo_jogos_fim__lte=now)
    }

    return render(request, 'home.html', context)
