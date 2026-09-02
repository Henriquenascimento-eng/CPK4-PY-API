from fastapi import FastAPI
import database  # importa o arquivo database.py

app = FastAPI(
    title="API CP4",
    version="1.0.0"
)

database.criar_tabelas()  # roda a criação das tabelas assim que a API sobe