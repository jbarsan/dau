from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# from perfis.models import User


# Create your models here.
class Equipamento(models.Model):
    tombamento = models.CharField(primary_key=True, max_length=15, verbose_name='Tombamento')
    descricao = models.CharField(_('Descrição'), max_length=50)
    marca = models.CharField(_('Marca'), max_length=50)
    modelo = models.CharField(_('Modelo'), max_length=50)
    num_serie = models.CharField(_('Número de Série'), max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Equipamento'
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return '{} - ({}, {}, {})'.format(self.tombamento, self.descricao, self.marca, self.modelo)


class Departamento(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, verbose_name='Código')
    descricao = models.CharField(_('Descrição'), max_length=100)

    class Meta:
        db_table = 'Departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{} {}'.format(self.codigo, self.descricao)


class Entrada(models.Model):
    STATUS_CHOICE = (
        ('0', 'Manutenção'),
        ('1', 'Pronto'),
        ('-1', 'Inservível'),
    )

    equipamento = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name='Equipamento')
    recebido_por = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, verbose_name='Recebido por')
    encaminhado_por = models.ForeignKey('Departamento', models.DO_NOTHING, verbose_name='Encaminhado por')
    responsavel = models.CharField(_('Responsável'), max_length=250)
    contatos = models.TextField(_('Contatos'))
    problemas = models.TextField(_('Problemas'), blank=True, null=True)
    servicos = models.TextField(_('Serviços'), blank=True, null=True)
    observacoes = models.TextField(_('Observações'), blank=True, null=True)
    data = models.DateTimeField(_('Data'))
    status = models.CharField(_('Status'), max_length=2, choices=STATUS_CHOICE)

    class Meta:
        db_table = 'Entrada'
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entrada'

    def __str__(self):
        return '{}'.format(self.id)


class Atendimento(models.Model):
    entrada = models.ForeignKey('Entrada', models.DO_NOTHING, verbose_name='Entrada')
    tecnico = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, verbose_name='Técnico')
    data_inicio = models.DateTimeField(_('Data de inicio'))
    data_fim = models.DateTimeField(_('Data de encerramento'), blank=True, null=True)
    resumo = models.TextField(_('Resumo'), blank=True, null=True)

    class Meta:
        db_table = 'Atendimento'
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return '{} ({})'.format(self.entrada.id, self.resumo)


class Saida(models.Model):
    entrada = models.ForeignKey('Entrada', models.DO_NOTHING, verbose_name='Entrada')
    tecnico = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, verbose_name='Técnico')
    data = models.DateTimeField(_('Data de Saída'))

    class Meta:
        db_table = 'Saida'
        verbose_name = 'Saída'
        verbose_name_plural = 'Saídas'

    def __str__(self):
        return '{}, ({}), ({})'.format(self.entrada.id, self.entrada.status, self.data)
