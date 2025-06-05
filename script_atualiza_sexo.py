import sqlite3
import gender_guesser.detector as gender

# Conectar ao banco SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Inicializa o detector de gênero
detector = gender.Detector()

# Obtém todos os clientes que ainda não têm sexo definido
cursor.execute("SELECT id, nome FROM app_medidas_clientes_pessoa WHERE sexo IS NULL OR sexo = '';")
clientes = cursor.fetchall()

for cliente in clientes:
    cliente_id, nome_completo = cliente
    primeiro_nome = nome_completo.strip().split()[0]  # Pega só o primeiro nome

    # Detecta o gênero baseado no nome
    sexo_detectado = detector.get_gender(primeiro_nome)

    # Ajusta para "Masculino" ou "Feminino"
    if sexo_detectado in ['male', 'mostly_male']:
        sexo_final = 'Masculino'
    elif sexo_detectado in ['female', 'mostly_female']:
        sexo_final = 'Feminino'
    else:
        sexo_final = 'Indefinido'  # Para casos desconhecidos

    # Atualiza no banco de dados
    cursor.execute("""
        UPDATE app_medidas_clientes_pessoa
        SET sexo = ?
        WHERE id = ?
    """, (sexo_final, cliente_id))

# Salva as alterações
conn.commit()
conn.close()

print("Atualização de sexo concluída com sucesso!")
