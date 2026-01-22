#Importando SQLite
import sqlite3 as lite

#Criando conexao
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizada com sucesso...')
except sqlite3.Error as e:
    print("Erro ao tentar conectar com o banco de dados:", e)


# Tabela de Cursos---------------------------------------------------

# Criando a Função criar cursos(CREATE - INSERIR)
def criar_cursos(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO cursos(nome, duracao, preco) VALUES (?,?,?)"
		cur.execute(query,i)

#criar_cursos(['Python','Duas Semanas',50])


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

print(ver_cursos())





