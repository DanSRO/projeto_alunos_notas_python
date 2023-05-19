import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE alunos(
    cpf VARCHAR NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nasc TEXT NOT NULL,
    sexo VARCHAR(1) NOT NULL,
    idade INTEGER,
    av1 VARCHAR(4) NOT NULL,
    av2 VARCHAR(4),
    media VARCHAR(4)
);
""")

print('Tabela criada com sucesso.')
conn.close()