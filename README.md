# StrideStore — API de Usuários e Produtos (CP4-PY)

Projeto acadêmico (FIAP) com **FastAPI** + **SQLite** no backend e **HTML/CSS/JS** no frontend, simulando uma loja virtual de tênis.

## Estrutura
CP4-PY/

├── backend/

      │ ├── main.py # ponto de entrada da API

      │ ├── database.py # conexão e criação das tabelas

      │ ├── usuarios/ # models, service, controller de clientes

      │ └── produtos/ # models, service, controller de tênis

└── frontend/
  
      ├── index.html
   
      ├── css/style.css
   
      └── js/script.js


      
## Como rodar

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

API em `http://localhost:8000` — docs em `http://localhost:8000/docs`.
Frontend: abrir `frontend/index.html` no navegador.

## Endpoints

- `POST /usuarios`, `GET /usuarios`, `GET /usuarios/{id}`, `PUT /usuarios/{id}`, `DELETE /usuarios/{id}`
- `POST /produtos`, `GET /produtos`, `GET /produtos/{id}`, `PUT /produtos/{id}`, `DELETE /produtos/{id}`

Cada produto pode opcionalmente pertencer a um usuário (`usuario_id`), representando a relação entre os dois modelos.

## Tecnologias

Python · FastAPI · Pydantic · SQLite · HTML · CSS · JavaScript

## Autor

Henrique — FIAP, disciplina de APIs.
