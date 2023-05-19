import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM alunos;
""")

for linha in cursor.fetchall():
    print(linha)
    
conn.close()