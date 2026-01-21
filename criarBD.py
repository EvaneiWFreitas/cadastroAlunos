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
        cur.execute(
            
        )     
        
         
except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos:", e)
 
    
