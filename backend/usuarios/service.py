import database as database  # importa nosso database.py para usar a get_connection()


def criar_usuario(usuario: dict):
    # abre uma conexão nova com o banco
    conexao = database.get_connection()
    cursor = conexao.cursor()

    # INSERT INTO insere uma nova linha na tabela usuarios.
    # os "?" são placeholders — evitam que o SQL quebre ou seja vulnerável
    #SQ a ataques (L Injection) quando inserimos valores vindos do usuário
    cursor.execute("""
        INSERT INTO usuarios (nome, email, idade)
        VALUES (?, ?, ?)
    """, (usuario["nome"], usuario["email"], usuario.get("idade")))

    conexao.commit()  # salva a inserção de verdade

    # cursor.lastrowid guarda o id que o SQLite gerou automaticamente
    # para essa nova linha (graças ao AUTOINCREMENT)
    novo_id = cursor.lastrowid

    conexao.close()

    # devolve o usuário criado, já com o id gerado
    return {
        "id": novo_id,
        "nome": usuario["nome"],
        "email": usuario["email"],
        "idade": usuario.get("idade")
    }


def listar_usuarios():
    conexao = database.get_connection()
    cursor = conexao.cursor()

    # SELECT * busca todas as colunas de todas as linhas da tabela
    cursor.execute("SELECT id, nome, email, idade FROM usuarios")

    # fetchall() retorna todas as linhas encontradas, como uma lista de tuplas
    # ex: [(1, "Henrique", "henrique@email.com", 18), (2, "Ana", "ana@email.com", 22)]
    linhas = cursor.fetchall()

    conexao.close()

    # transforma cada tupla numa lista de dicionários, formato mais
    # amigável para retornar como JSON na API
    usuarios = []
    for linha in linhas:
        usuarios.append({
            "id": linha[0],
            "nome": linha[1],
            "email": linha[2],
            "idade": linha[3]
        })

    return usuarios


def buscar_usuario(usuario_id: int):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    # WHERE id = ? filtra só a linha com aquele id específico
    cursor.execute("SELECT id, nome, email, idade FROM usuarios WHERE id = ?", (usuario_id,))

    # fetchone() retorna só uma linha (ou None, se não encontrar nada)
    linha = cursor.fetchone()

    conexao.close()

    # se não encontrou nenhuma linha, devolve None
    if linha is None:
        return None

    # se encontrou, devolve como dicionário
    return {
        "id": linha[0],
        "nome": linha[1],
        "email": linha[2],
        "idade": linha[3]
    }


def atualizar_usuario(usuario_id: int, dados: dict):
    # primeiro verifica se o usuário existe, reaproveitando a função acima
    usuario_existente = buscar_usuario(usuario_id)
    if usuario_existente is None:
        return None

    conexao = database.get_connection()
    cursor = conexao.cursor()

    # usa dados.get(campo, valor_atual) para manter o valor antigo
    # caso o campo não tenha sido enviado na atualização
    novo_nome = dados.get("nome", usuario_existente["nome"])
    novo_email = dados.get("email", usuario_existente["email"])
    nova_idade = dados.get("idade", usuario_existente["idade"])

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?, idade = ?
        WHERE id = ?
    """, (novo_nome, novo_email, nova_idade, usuario_id))

    conexao.commit()
    conexao.close()

    return {
        "id": usuario_id,
        "nome": novo_nome,
        "email": novo_email,
        "idade": nova_idade
    }


def excluir_usuario(usuario_id: int):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    # DELETE FROM remove a linha correspondente
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))

    conexao.commit()

    # cursor.rowcount diz quantas linhas foram afetadas pelo comando.
    # se for 0, significa que não existia nenhum usuário com esse id
    linhas_afetadas = cursor.rowcount

    conexao.close()

    return linhas_afetadas > 0