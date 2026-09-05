import database as database  # reutiliza a mesma conexão que usuarios/service.py usa


def criar_produto(produto: dict):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, usuario_id)
        VALUES (?, ?, ?, ?)
    """, (produto["nome"], produto["preco"], produto.get("quantidade"), produto["usuario_id"]))

    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return {
        "id": novo_id,
        "nome": produto["nome"],
        "preco": produto["preco"],
        "quantidade": produto.get("quantidade"),
        "usuario_id": produto["usuario_id"]
    }


def listar_produtos():
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, quantidade, usuario_id FROM produtos")
    linhas = cursor.fetchall()

    conexao.close()

    produtos = []
    for linha in linhas:
        produtos.append({
            "id": linha[0],
            "nome": linha[1],
            "preco": linha[2],
            "quantidade": linha[3],
            "usuario_id": linha[4]
        })

    return produtos


def buscar_produto(produto_id: int):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, preco, quantidade, usuario_id FROM produtos WHERE id = ?", (produto_id,))
    linha = cursor.fetchone()

    conexao.close()

    if linha is None:
        return None

    return {
        "id": linha[0],
        "nome": linha[1],
        "preco": linha[2],
        "quantidade": linha[3],
        "usuario_id": linha[4]
    }


def atualizar_produto(produto_id: int, dados: dict):
    produto_existente = buscar_produto(produto_id)
    if produto_existente is None:
        return None

    conexao = database.get_connection()
    cursor = conexao.cursor()

    novo_nome = dados.get("nome", produto_existente["nome"])
    novo_preco = dados.get("preco", produto_existente["preco"])
    nova_quantidade = dados.get("quantidade", produto_existente["quantidade"])
    novo_usuario_id = dados.get("usuario_id", produto_existente["usuario_id"])

    cursor.execute("""
        UPDATE produtos
        SET nome = ?, preco = ?, quantidade = ?, usuario_id = ?
        WHERE id = ?
    """, (novo_nome, novo_preco, nova_quantidade, novo_usuario_id, produto_id))

    conexao.commit()
    conexao.close()

    return {
        "id": produto_id,
        "nome": novo_nome,
        "preco": novo_preco,
        "quantidade": nova_quantidade,
        "usuario_id": novo_usuario_id
    }


def excluir_produto(produto_id: int):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conexao.commit()

    linhas_afetadas = cursor.rowcount
    conexao.close()

    return linhas_afetadas > 0