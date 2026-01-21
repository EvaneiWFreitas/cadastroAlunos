# Importando SQLite3
import sqlite3

#Criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizada com sucesso...')
except sqlite3.Error as e:
    print("Erro ao tentar conectar com o banco de dados:", e)
    
    
#Criando Tabela de Cursos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT,
          duracao TEXT,
          preco REAL      
        )""") 

        print("Tabela Cursos criada com sucesso!")    
                
except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos:", e)


#Criando Tabela de Turmas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT,
          curso_nome TEXT,
          data_inicio DATE,
          FOREIGN KEY(curso_nome) REFERENCES cursos(nome) ON UPDATE CASCADE ON DELETE CASCADE     
        )""") 

        print("Tabela Turmas criada com sucesso!")    
                
except sqlite3.Error as e:
    print("Erro ao criar a tabela turmas:", e)
 
    
