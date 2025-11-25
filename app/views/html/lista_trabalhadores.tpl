<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Trabalhadores</title>
    <link rel="stylesheet" href="/static/css/lista_trabalhadores.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>📋 Lista de Trabalhadores Cadastrados</h1>
            <p>Total de registros: <span id="totalRegistros">0</span></p>
        </header>

        <div class="actions">
            <input type="text" id="searchInput" placeholder="Buscar por nome ou CPF..." class="search-input">
            <button onclick="carregarTrabalhadores()" class="btn btn-refresh"> Atualizar</button>
            <a href="/cadastro" class="btn btn-novo"> Novo Cadastro</a>
        </div>

        <div id="loadingMsg" class="loading" style="display:none;">Carregando...</div>
        <div id="emptyMsg" class="empty-message">Nenhum trabalhador cadastrado ainda.</div>

        <table id="trabalhadorTable" class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome Completo</th>
                    <th>CPF</th>
                    <th>Email</th>
                    <th>Telefone</th>
                    <th>Sexo</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>
    </div>

    <!-- Modal para detalhes -->
    <div id="detailsModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="fecharModal()">&times;</span>
            <h2>Detalhes do Trabalhador</h2>
            <div id="detailsContent"></div>
            <div class="modal-actions">
                <button onclick="fecharModal()" class="btn btn-secondary">Fechar</button>
                <button onclick="deletarSelecionado()" class="btn btn-danger">🗑️ Deletar</button>
            </div>
        </div>
    </div>

    <script src="/static/js/lista_trabalhadores.js"></script>
    <script>
        // Carregar dados ao abrir a página
        document.addEventListener('DOMContentLoaded', carregarTrabalhadores);
    </script>
</body>
</html>
