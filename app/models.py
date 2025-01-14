from typing import Any
from django.db import models

# Classe 'UF' para representar as Unidades Federativas
class UF(models.Model):
    sigla = models.CharField(
        max_length=2,
        verbose_name="Sigla",
        unique=True,
        help_text="Informe a sigla da Unidade Federativa",
    )

    class Meta:
        verbose_name = "Unidade Federal" 
        verbose_name_plural = "Unidades Federais"

    def __str__(self):
        return self.sigla

# Classe 'Cidade' para representar as cidades
class Cidades(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name="Nome da Cidade",
        help_text="Informe o nome da cidade",
    )
    uf = models.ForeignKey(
        UF,
        on_delete=models.CASCADE,
        verbose_name="Unidade Federal",
        help_text="Selecione a Unidade Federal",
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ('nome', 'uf')
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome

# Classe 'Ocupacao' para representar as ocupacoes
class Ocupacoes(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name="Nome da Ocupação",
        unique=True,
        help_text="Informe o nome da ocupação",
    )

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

    def __str__(self):
        return self.nome
    
# Classe 'Pessoas'
class Pessoas(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome",
        help_text="Informe o nome"
    )
    nome_pai = models.CharField(
        max_length=255, 
        verbose_name="Nome do Pai",
        help_text="Informe o nome do pai"
    )
    nome_mae = models.CharField(
        max_length=255, 
        verbose_name="Nome da Mãe",
        help_text="Informe o nome da mãe"
    )
    cpf = models.CharField(
        max_length=11, 
        verbose_name="CPF",
        unique=True,
        help_text="Informe o CPF",
    )
    data_nasc = models.DateField(
        default="2000-01-01",
        verbose_name="Data de Nascimento",
        help_text="Informe a data de Nascimento"
    )
    email = models.EmailField(
        verbose_name="E-mail",
        help_text="Informe o e-mail",
    )
    cidades = models.ForeignKey(
        Cidades, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Cidade",
        help_text="Selecione a cidade"
    )
    ocupacao = models.ForeignKey(
        Ocupacoes, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Ocupação",
        help_text="Selecione a ocupação"
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome

# Classe 'Instituição'
class Instituicao(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome",
        help_text="Informe o nome"
    )
    site = models.CharField(
        max_length=255, 
        verbose_name="Site",
        help_text="Informe o site"
    )
    telefone = models.CharField(
        max_length=255, 
        verbose_name="Telefone",
        help_text="Informe o telefone"
    )
    cidades = models.ForeignKey(
        Cidades, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Cidade",
        help_text="Selecione a cidade"
    )
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

    def __str__(self):
        return self.nome
    
# Classe 'Áreas do Saber'
class Area_Saber(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Áreas do Saber",
        help_text="Informe a área do saber:"
    )
    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"

    def __str__(self):
        return self.nome

# Classe 'curso'
class Curso(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="curso",
        help_text="Informe o curso:"
    )
    carga_horaria_total = models.CharField(
        max_length=255, 
        verbose_name="Carga Horária Total",
        help_text="Informe a carga horária total"
    )
    duracao_meses = models.CharField(
        max_length=255, 
        verbose_name="Duração em meses",
        help_text="Informe a duração em meses"
    )
    area_saber = models.ForeignKey(
        Area_Saber, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Áreas do Saber",
        help_text="Selecione a área do saber"
    )

    def __str__(self):
        return self.nome


# Classe 'Turnos'
class Turnos(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Turnos",
        help_text="Informe o turno:"
    )

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return self.nome
    
# Classe 'Disciplinas'
class Disciplinas(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Displinas",
        help_text="Informe as disciplinas:"
    )
    instituicao = models.ForeignKey(
        Instituicao, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Instituição",
        help_text="Selecione a instituição"
    )
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.nome

# Classe 'Matrículas'
class Matriculas(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Matrícula",
        help_text="Informe a matrícula:"
    )
    data_inicio = models.DateField(
        default="2000-01-01",
        verbose_name="Data de início",
        help_text="Informe a data de início"
    )
    data_previsao_termino = models.DateField(
        default="2000-01-01",
        verbose_name="Data de previsão do término",
        help_text="Informe a data de previsão do término"
    )
    instituicao = models.ForeignKey(
        Instituicao, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Instituição",
        help_text="Selecione a instituição"
    )
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="curso",
        help_text="Selecione o curso"
    )
    pessoas = models.ForeignKey(
        Pessoas, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Usuário",
        help_text="Selecione o usuário"
    )

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return self.nome

# Classe 'avaliações'
class Avaliacao(models.Model):
    descricao = models.CharField(
        max_length=255, 
        verbose_name="Descricao",
        help_text="Informe a descricao:"
    )
    nota = models.CharField(
        max_length=255, 
        verbose_name="Nota",
        help_text="Informe a nota:"
    )
    disciplina = models.ForeignKey(
        Disciplinas, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Disciplinas",
        help_text="Selecione a disciplina"
    )
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="curso",
        help_text="Selecione o curso"
    )
    tipoavaliacao = models.ForeignKey(
        Pessoas, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Tipo de avaliação",
        help_text="Selecione o tipo da avaliação"
    )

    def __str__(self):
        return self.nome


# Classe 'Frequência'
class Frequencia(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Faltas",
        help_text="Informe as faltas:"
    )
    disciplina = models.ForeignKey(
        Disciplinas, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Disciplinas",
        help_text="Selecione a disciplina"
    )
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="curso",
        help_text="Selecione o curso"
    )
    pessoas = models.ForeignKey(
        Pessoas, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Usuário",
        help_text="Selecione o usuário"
    )

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

    def __str__(self):
        return self.nome

# Classe 'Turmas'
class Turmas(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome",
        help_text="Informe o nome da turma:"
    )
    turnos = models.ForeignKey(
        Turnos, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        verbose_name="Turno",
        help_text="Selecione o turno"
    )

    def __str__(self):
        return self.nome

# Classe 'tipoavaliacao'
class tipoavaliacao(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome",
        help_text="Informe o nome da turma:"
    )

    def __str__(self):
        return self.nome

# Classe 'Ocorrência'
class Ocorrencia(models.Model):
    nome = models.TextField(
        verbose_name="Descrição",
        help_text="Descreva a ocorrência",
    )
    data = models.DateField(
        verbose_name="Data da Ocorrência",
        help_text="Informe a data da ocorrência",
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name="Curso",
        help_text="Selecione o curso relacionado à ocorrência",
    )
    disciplina = models.ForeignKey(
        Disciplinas,
        on_delete=models.CASCADE,
        verbose_name="Disciplina",
        help_text="Selecione a disciplina relacionada à ocorrência",
    )
    pessoa = models.ForeignKey(
        Pessoas,
        on_delete=models.CASCADE,
        verbose_name="Pessoa",
        help_text="Selecione a pessoa relacionada à ocorrência",
    )
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
    def __str__(self):
        return self.nome


class DisciplinaPorCurso(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name="Curso",
        help_text="Selecione o curso",
    )
    disciplina = models.ForeignKey(
        Disciplinas,
        on_delete=models.CASCADE,
        verbose_name="Disciplina",
        help_text="Selecione a disciplina",
    )
    turno = models.ForeignKey(
        Turnos,
        on_delete=models.CASCADE,
        verbose_name="Turno",
        help_text="Selecione o turno",
    )
    carga_horaria = models.PositiveIntegerField(
        verbose_name="Carga Horária",
        help_text="Informe a carga horária em horas",
    )

    def __str__(self):
        return self.nome