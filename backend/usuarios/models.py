from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    idade: int | None = None