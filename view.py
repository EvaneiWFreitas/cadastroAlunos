"""
CRUD é um acrônimo para Create (Criar), Read (Ler), Update (Atualizar) e Delete (Deletar),
representando as quatro operações fundamentais para manipular dados em qualquer 
sistema de software ou banco de dados

"""

#Importando SQLite
import sqlite3 as lite

#Criando conexao
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizada com sucesso...')
except sqlite3.Error as e:
    print("Erro ao tentar conectar com o banco de dados:", e)


#************************************************************************
#                               CURSOS
#************************************************************************

# FUNÇÕES -------------CURSOS------------------------------------------
# Criando a Função criar cursos(CREATE - INSERIR)

def criar_cursos(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO cursos(nome, duracao, preco) VALUES (?,?,?)"
		cur.execute(query,i)

#criar_cursos(['Python','Duas Semanas',50])

#------------------------------------------------------------------------

#Ver Todos os Cursos(READ - LER OU SELECIONAR TODOS OS CURSOS)
#Criando uma Função para ver os cursos

def ver_cursos():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM cursos')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)

	return lista

#print(ver_cursos())

#------------------------------------------------------------------------

#Atualizar  Curso(UPDATE - ATUALIZAR CURSO)
# Criando a Função atualizar curso(UPDATE - ATUALIZAR)

def atualizar_cursos(i):
	with con:
		cur = con.cursor()
		query = "UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=?"
		cur.execute(query,i)


l = ['Básico de Python', 'Quatro Semanas', 120.0, 1]
#atualizar_cursos(l)

#------------------------------------------------------------------------

#Deletar - Excluir  Curso(EXCLUIR CURSO)
# Criando a Função Excluir(DELETE) 

def deletar_curso(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM cursos WHERE id=?"
		cur.execute(query,i)


#deletar_curso([1])

#------------------------------------------------------------------------


#************************************************************************
#                               TURMAS
#************************************************************************

# FUNÇÕES ---------------TURMAS------------------------------------------
# Criando a Função criar turmas(CREATE - INSERIR)

def criar_turmas(i):
	with con:
		cur = con.cursor()
			query = "INSERT INTO turmas(nome, curso_nome, data_inicio) VALUES (?,?,?)"
		cur.execute(query,i)


#------------------------------------------------------------------------

#Ver Todos as Turmas(READ - LER OU SELECIONAR TODAS AS TURMAS)
# Criando a Função ver turmas(READ - LER OU SELECIONAR TODAS AS TURMAS)

def ver_turmas():
	lista = []
	with con:
		cur = con.cursor()
		cur.execute('SELECT * FROM turmas')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)

	return lista


#------------------------------------------------------------------------

#Atualizar Todos as Turmas(UPDATE - ATUALIZAR TODAS AS TURMAS)
# Criando a Função atualizar turmas(UPDATE - ATUALIZAR)

def atualizar_turmas(i):
	with con:
		cur = con.cursor()
		query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
		cur.execute(query,i)


#------------------------------------------------------------------------

#Deletar - Excluir  Turma(EXCLUIR TURMA)
# Criando a Função Excluir(DELETE) 

def deletar_turma(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM turmas WHERE id=?"
		cur.execute(query,i)


#------------------------------------------------------------------------


#************************************************************************
#                               ALUNOS
#************************************************************************





