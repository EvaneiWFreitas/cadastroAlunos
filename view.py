#Importando SQLite
import sqlite3 as lite

#Criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizada com sucesso...')
except sqlite3.Error as e:
    print("Erro ao tentar conectar com o banco de dados:", e)


# Tabela de Cursos---------------------------------------------------

# Criando a Função criar cursos(CREATE - INSERIR)
def criar_cursos(i)




