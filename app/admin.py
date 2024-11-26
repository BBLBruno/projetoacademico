from django.contrib import admin
from .models import *

# Definir as classes de inline
class CidadeInline(admin.TabularInline):
    model = Cidades  # Modelo relacionado
    extra = 1  # Quantidade de formulários em branco

class OcupacaoInline(admin.TabularInline):  # Formulário em tabela
    model = Ocupacoes
    extra = 1


class InstituicaoInline(admin.StackedInline):  # Formulário em pilha
    model = Instituicao
    extra = 1


class UFAdmin(admin.ModelAdmin):
    list_display = ("sigla",)
    search_fields = ("sigla",)
    ordering = ("sigla",)
    inlines = [CidadeInline]  # Você pode descomentar se quiser incluir as cidades aqui

# Definir as classes de administração
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "uf")
    list_filter = ("uf",)
    search_fields = ("nome",)
    ordering = ("nome",)


class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    list_filter = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


class PessoasAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "cidades", "ocupacao")
    list_filter = ("nome", "email", "cidades", "ocupacao")
    search_fields = ("nome", "email")
    ordering = ("nome", "email")


class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "site", "cidades")
    list_filter = ("nome", "cidades")
    search_fields = ("nome", "site")
    ordering = ("nome", "site")


class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "carga_horaria_total", "duracao_meses", "area_saber")
    list_filter = ("nome", "area_saber")
    search_fields = ("nome",)
    ordering = ("nome",)


class TurnoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao")
    list_filter = ("instituicao",)
    search_fields = ("nome",)
    ordering = ("nome",)


class MatriculasAdmin(admin.ModelAdmin):
    list_display = ("matricula", "data_inicio", "data_previsao_termino", "instituicao", "curso", "pessoas")
    list_filter = ("instituicao", "curso", "pessoas")
    search_fields = ("matricula", "instituicao", "curso", "pessoas")
    ordering = ("matricula",)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("descricao", "nota", "disciplina", "curso", "tipoavaliacao")
    list_filter = ("disciplina", "curso")
    search_fields = ("descricao", "nota")
    ordering = ("descricao",)

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ("numero_faltas", "disciplina", "curso", "pessoas")
    list_filter = ("disciplina", "curso", "pessoas")
    search_fields = ("disciplina",)
    ordering = ("disciplina",)


class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("descricao", "data", "curso", "disciplina", "pessoa")
    list_filter = ("curso", "disciplina", "pessoa")
    search_fields = ("descricao",)
    ordering = ("data",)


class DisciplinaPorCursoAdmin(admin.ModelAdmin):
    list_display = ("curso", "disciplina", "turno", "carga_horaria")
    list_filter = ("curso", "disciplina", "turno")
    search_fields = ("curso", "disciplina")
    ordering = ("curso", "disciplina")


# Registrar as classes no ambiente administrativo
admin.site.register(UF, UFAdmin)
admin.site.register(Cidades, CidadeAdmin)
admin.site.register(Ocupacoes, OcupacaoAdmin)
admin.site.register(Pessoas, PessoasAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turnos, TurnoAdmin)
admin.site.register(Disciplinas, DisciplinaAdmin)
admin.site.register(Matriculas, MatriculasAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)
admin.site.register(DisciplinaPorCurso, DisciplinaPorCursoAdmin)