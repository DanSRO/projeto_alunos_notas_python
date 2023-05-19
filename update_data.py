import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

p_cpf = 123
p_nome = input('Nome: ')
p_data_nasc = input('DATA DE NASCIMENTO: ')
p_sexo = input('SEXO: ')
p_idade = input('IDADE: ')
p_av1 = input('AV1: ')
p_av2 = input('AV2: ')
p_media = input('MÉDIA: ')

cursor.execute("""
UPDATE alunos 
SET nome = ? , data_nasc = ? , sexo = ?, idade= ?, av1 = ?, av2 = ?, media = ? 
WHERE cpf = ?
""", (p_cpf, p_nome, p_data_nasc, p_sexo, p_idade, p_av1, p_av2, p_media))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()