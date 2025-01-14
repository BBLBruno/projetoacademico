from django.shortcuts import render
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidades.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
    
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacoes.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoas.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class UFView(View):
    def get(self, request, *args, **kwargs):
        ufs = UF.objects.all()
        return render(request, 'uf.html', {'ufs': ufs})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turnos.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplinas.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class AreasDoSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = Area_Saber.objects.all()
        return render(request, 'area_saber.html', {'areas': areas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matriculas.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turmas.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class TiposAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos_avaliacao = tipoavaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos_avaliacao': tipos_avaliacao})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

class DisciplinaPorCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_por_curso = DisciplinaPorCurso.objects.all()
        return render(request, 'disciplina_por_curso.html', {'disciplinas_por_curso': disciplinas_por_curso})

