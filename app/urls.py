from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicoes'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacoes'),
    path('pessoa/', PessoaView.as_view(), name='pessoas'),
    path('uf/', UFView.as_view(), name='ufs'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplinas'),
    path('curso/', CursosView.as_view(), name='cursos'),
    path('areas-do-saber/', AreasDoSaberView.as_view(), name='area_saber'),
    path('matricula/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencias'),
    path('turma/', TurmasView.as_view(), name='turmas'),
    path('tipo-avaliacao/', TiposAvaliacaoView.as_view(), name='tipos_avaliacao'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('disciplina-por-curso/', DisciplinaPorCursoView.as_view(), name='disciplinas_por_curso'),
    
]
