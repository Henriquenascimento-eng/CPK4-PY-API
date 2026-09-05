# CP4-PY — API de Usuários e Produtos

Projeto acadêmico (FIAP) desenvolvido com **FastAPI** e **SQLite**, com uma interface web em **HTML, CSS e JavaScript puro** para interação com a API.

## 📋 Sobre o projeto

A aplicação gerencia duas entidades relacionadas:

- **Usuários**: `id`, `nome`, `email`, `idade`
- **Produtos**: `id`, `nome`, `preco`, `quantidade`, `usuario_id`

Cada produto pertence a um usuário (relação de chave estrangeira `usuario_id → usuarios.id`), demonstrando a integração entre modelos relacionados.

## 🏗️ Arquitetura

O backend segue uma arquitetura em camadas:

- **Controller**: recebe as requisições HTTP e define as rotas
- **Service**: contém a lógica de negócio e o acesso ao banco de dados
- **Models**: define os modelos Pydantic usados para validar os dados de entrada

CP4-PY/
├── backend/
│ ├── main.py # ponto de entrada da API
│ ├── database.py # conexão e criação das tabelas no SQLite
│ ├── usuarios/
│ │ ├── controller.py
│ │ ├── service.py
│ │ └── models.py
│ └── produtos/
│ ├── controller.py
│ ├── service.py
│ └── models.py
└── frontend/
├── index.html
├── css/
│ └── style.css
└── js/
└── script.js


## 🚀 Como rodar o projeto

### Backend

1. Entre na pasta `backend/`:
```bash
   cd backend
```

2. Crie e ative um ambiente virtual:
```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Linux/macOS
```

3. Instale as dependências:
```bash
   pip install fastapi uvicorn
```

4. Rode o servidor:
```bash
   uvicorn main:app --reload
```

5. A API estará disponível em `http://localhost:8000`, com documentação automática em `http://localhost:8000/docs`.

### Frontend

Com o backend rodando, abra o arquivo `frontend/index.html` diretamente no navegador (duplo clique, ou clique com o botão direito → "Abrir com" → navegador).

## 📡 Endpoints

### Usuários

| Método | Rota              | Descrição                  |
|--------|-------------------|-----------------------------|
| POST   | `/usuarios`       | Cria um novo usuário        |
| GET    | `/usuarios`       | Lista todos os usuários     |
| GET    | `/usuarios/{id}`  | Busca um usuário pelo id    |
| PUT    | `/usuarios/{id}`  | Atualiza um usuário         |
| DELETE | `/usuarios/{id}`  | Exclui um usuário           |

### Produtos

| Método | Rota              | Descrição                  |
|--------|-------------------|-----------------------------|
| POST   | `/produtos`       | Cria um novo produto        |
| GET    | `/produtos`       | Lista todos os produtos     |
| GET    | `/produtos/{id}`  | Busca um produto pelo id    |
| PUT    | `/produtos/{id}`  | Atualiza um produto         |
| DELETE | `/produtos/{id}`  | Exclui um produto           |

## 🛠️ Tecnologias utilizadas

- Python 3
- FastAPI
- Pydantic
- SQLite
- HTML, CSS e JavaScript

## 👤 Autor

Henrique — rm569137
Andrey Luigi - rm569575
Lucas Trevisan - rm569731