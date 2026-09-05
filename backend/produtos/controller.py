from fastapi import APIRouter, HTTPException
from produtos import service
from produtos.models import ProdutoCreate

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("", status_code=201)
def criar_produto(produto: ProdutoCreate):
    return service.criar_produto(produto.dict())


@router.get("")
def listar_produtos():
    return service.listar_produtos()


@router.get("/{produto_id}")
def buscar_produto(produto_id: int):
    produto = service.buscar_produto(produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.put("/{produto_id}")
def atualizar_produto(produto_id: int, produto: ProdutoCreate):
    resultado = service.atualizar_produto(produto_id, produto.dict())
    if resultado is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return resultado


@router.delete("/{produto_id}")
def excluir_produto(produto_id: int):
    sucesso = service.excluir_produto(produto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"mensagem": "Produto excluído com sucesso"}