import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

p_cpf = 123

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM alunos
WHERE cpf = ?
""", (p_cpf,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()