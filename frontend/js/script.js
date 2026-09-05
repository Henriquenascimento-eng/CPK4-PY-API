// URL base da nossa API - todos os fetch vão usar esse endereço como ponto de partida
const API_URL = "http://localhost:8000";


// ===== FUNÇÕES DE USUÁRIOS =====

// busca a lista de usuários na API e atualiza a tela
async function carregarUsuarios() {
    const resposta = await fetch(`${API_URL}/usuarios`);
    const usuarios = await resposta.json(); // converte a resposta em objeto/array JavaScript

    // pega a <ul id="lista-usuarios"> e limpa o conteúdo antigo antes de recriar
    const lista = document.getElementById("lista-usuarios");
    lista.innerHTML = "";

    // pega o <select id="produto-usuario"> (dropdown do formulário de produto) e limpa também
    const selectUsuario = document.getElementById("produto-usuario");
    selectUsuario.innerHTML = "";

    // para cada usuário retornado pela API, cria um <li> na lista e uma <option> no dropdown
    usuarios.forEach(usuario => {
        const li = document.createElement("li");
        li.textContent = `#${usuario.id} - ${usuario.nome} (${usuario.email})`;
        lista.appendChild(li);

        const option = document.createElement("option");
        option.value = usuario.id;           // o valor enviado será o id
        option.textContent = usuario.nome;   // o texto mostrado será o nome
        selectUsuario.appendChild(option);
    });
}


// captura o envio do formulário de usuário
document.getElementById("form-usuario").addEventListener("submit", async (evento) => {
    evento.preventDefault(); // impede o comportamento padrão do formulário (recarregar a página)

    // monta o objeto com os dados digitados, lendo cada campo pelo id
    const novoUsuario = {
        nome: document.getElementById("usuario-nome").value,
        email: document.getElementById("usuario-email").value,
        idade: document.getElementById("usuario-idade").value
            ? parseInt(document.getElementById("usuario-idade").value)
            : null
    };

    // envia um POST para a API, com o corpo em JSON
    await fetch(`${API_URL}/usuarios`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(novoUsuario)
    });

    // limpa o formulário e recarrega a lista, pra já aparecer o novo usuário
    document.getElementById("form-usuario").reset();
    carregarUsuarios();
});


// ===== FUNÇÕES DE PRODUTOS =====

// busca a lista de produtos na API e atualiza a tela
async function carregarProdutos() {
    const resposta = await fetch(`${API_URL}/produtos`);
    const produtos = await resposta.json();

    const lista = document.getElementById("lista-produtos");
    lista.innerHTML = "";

    produtos.forEach(produto => {
        const li = document.createElement("li");
        li.textContent = `#${produto.id} - ${produto.nome} - R$ ${produto.preco} (dono: usuário #${produto.usuario_id})`;
        lista.appendChild(li);
    });
}


// captura o envio do formulário de produto
document.getElementById("form-produto").addEventListener("submit", async (evento) => {
    evento.preventDefault();

    const novoProduto = {
        nome: document.getElementById("produto-nome").value,
        preco: parseFloat(document.getElementById("produto-preco").value),
        quantidade: document.getElementById("produto-quantidade").value
            ? parseInt(document.getElementById("produto-quantidade").value)
            : null,
        usuario_id: parseInt(document.getElementById("produto-usuario").value) // vem do dropdown
    };

    await fetch(`${API_URL}/produtos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(novoProduto)
    });

    document.getElementById("form-produto").reset();
    carregarProdutos();
});


// ===== INICIALIZAÇÃO =====

// assim que a página carrega, busca os dados já existentes na API
carregarUsuarios();
carregarProdutos();