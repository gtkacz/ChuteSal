from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.query_utils import Q


class Unidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    unidade = models.OneToOneField(
        Unidade, on_delete=models.CASCADE, related_name='unidade')
    is_cup_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Quadra(models.Model):
    nome = models.CharField(max_length=50)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = ('nome', 'unidade')


class Campeonato(models.Model):
    nome = models.CharField(max_length=50)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    periodo_inscricao_comeco = models.DateField()
    periodo_inscricao_fim = models.DateField()
    periodo_jogos_comeco = models.DateField()
    periodo_jogos_fim = models.DateField()
    data_inicio_divulgacao = models.DateField()
    cup_manager = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.periodo_inscricao_comeco > self.periodo_inscricao_fim:
            raise ValueError(
                'Data de início de inscrição não pode ser maior que a data de fim de inscrição.')

        if self.periodo_jogos_comeco > self.periodo_jogos_fim:
            raise ValueError(
                'Data de início de jogos não pode ser maior que a data de fim de jogos.')

        if self.periodo_inscricao_fim > self.periodo_jogos_comeco:
            raise ValueError(
                'Data de fim de inscrição não pode ser maior que a data de início de jogos.')

        if self.data_inicio_divulgacao > self.periodo_inscricao_comeco:
            raise ValueError(
                'Data de início de divulgação não pode ser maior que a data de início de inscrição.')

        if self.cup_manager.unidade != self.unidade:
            raise ValueError(
                'O cup manager deve pertencer a unidade do campeonato.')

        if self.cup_manager.is_cup_manager is False:
            raise ValueError('O cup manager deve ser um cup manager.')

        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ('nome', 'unidade')


class Time(models.Model):
    nome = models.CharField(max_length=50)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    # posicao = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     if self.posicao < 0:
    #         raise ValueError('Posição não pode ser menor que negativa.')

    #     elif self.posicao > 0:
    #         if any(self.posicao == time.posicao for time in Time.objects.filter(campeonato=self.campeonato)):
    #             raise ValueError('Posição já está ocupada.')

    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = (('nome', 'campeonato'),)
        # constraints = [
        #     UniqueConstraint(
        #         fields=['campeonato', 'posicao'], condition=Q(posicao__gt=0), name='unique_position'
        #     )
        # ]

class Jogo(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    time1 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time1')
    time2 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time2')
    data = models.DateField()
    horario = models.TimeField()
    rodada = models.IntegerField(default=0)
    quadra = models.ForeignKey(Quadra, on_delete=models.CASCADE, null=True, blank=True)
    resultado_time1 = models.IntegerField(default=0)
    resultado_time2 = models.IntegerField(default=0)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.time1} x {self.time2}'

    def save(self, *args, **kwargs):
        if self.time1.campeonato != self.campeonato or self.time2.campeonato != self.campeonato:
            raise ValueError('Os times devem pertencer ao campeonato do jogo.')

        if self.time1 == self.time2:
            raise ValueError('Os times não podem ser iguais.')

        if self.data < self.campeonato.periodo_jogos_comeco or self.data > self.campeonato.periodo_jogos_fim:
            raise ValueError(
                'A data do jogo deve estar dentro do período de jogos do campeonato.')

        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ('time1', 'time2', 'data', 'campeonato')


class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50, null=True, blank=True)
    data_nascimento = models.DateField()
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, blank=True, related_name='time')

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = ('nome', 'time')
