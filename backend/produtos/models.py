from pydantic import BaseModel


class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    quantidade: int | None = None
    usuario_id: int