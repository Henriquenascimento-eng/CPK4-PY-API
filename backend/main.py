from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
from usuarios.controller import router as usuarios_router
from produtos.controller import router as produtos_router

app = FastAPI(
    title="API CP4",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database.criar_tabelas()

app.include_router(usuarios_router)
app.include_router(produtos_router)