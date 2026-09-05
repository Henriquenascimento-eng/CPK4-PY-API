import sqlite3  # importa o módulo do Python que sabe conversar com bancos SQLite


def get_connection():
    # abre (ou cria, se não existir) o arquivo dados.db
    conexao = sqlite3.connect("dados.db")
    # ativa a validação de chaves estrangeiras (FOREIGN KEY) nesta conexão.
    # o SQLite vem com essa validação DESLIGADA por padrão, então sem essa
    # linha ele aceitaria produtos com usuario_id de usuários que não existem
    conexao.execute("PRAGMA foreign_keys = ON")
    # devolve essa conexão pra quem chamou a função poder usá-la
    return conexao


def criar_tabelas():
    # reutiliza a função acima em vez de repetir sqlite3.connect(...)
    conexao = get_connection()
    # cursor é a "ferramenta" usada para executar comandos SQL através da conexão
    cursor = conexao.cursor()

    # cria a tabela usuarios, só se ela ainda não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            idade INTEGER
        )
    """)

    # cria a tabela produtos, só se ela ainda não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER,
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    """)

    # salva de verdade as mudanças no arquivo dados.db
    conexao.commit()
    # fecha a conexão, liberando o recurso
    conexao.close()