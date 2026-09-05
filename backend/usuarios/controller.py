from fastapi import APIRouter, HTTPException  # APIRouter organiza as rotas; HTTPException gera erros HTTP (404, etc.)
from usuarios import service  # importa as funções do service.py que está dentro da pasta usuarios/

# cria um "roteador" com prefixo /usuarios — todas as rotas aqui dentro
# vão começar com /usuarios automaticamente (ex: /usuarios, /usuarios/1)
router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("")
def criar_usuario(usuario: dict):
    # recebe o corpo da requisição como dict e repassa pro service cuidar da lógica/banco
    return service.criar_usuario(usuario)


@router.get("")
def listar_usuarios():
    # retorna a lista de todos os usuários cadastrados
    return service.listar_usuarios()


@router.get("/{usuario_id}")
def buscar_usuario(usuario_id: int):
    # busca um usuário específico pelo id (vindo da URL, ex: /usuarios/3)
    usuario = service.buscar_usuario(usuario_id)

    # se o service retornou None, quer dizer que não achou — devolve erro 404
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario


@router.put("/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: dict):
    resultado = service.atualizar_usuario(usuario_id, usuario)

    if resultado is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado") #raise dispara o erro de proposito

    return resultado


@router.delete("/{usuario_id}")
def excluir_usuario(usuario_id: int):
    sucesso = service.excluir_usuario(usuario_id)

    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {"mensagem": "Usuário excluído com sucesso"}