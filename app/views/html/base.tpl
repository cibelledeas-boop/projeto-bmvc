<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/home.css">
    <title>{{!title or 'Portal do Funcionário'}}</title>
</head>
<body>
    <header>
        <div class="cabecalho">
            <div class="logo"><img id="img-logo" src="/static/img/logocj.jpg" alt=""></div>
            <h2 id="h2-cab">Portal do Funcionário</h2>
            <a href="/logout" class="btn-logout">Logout</a>
        </div>
    </header>
    <nav class="menu">
        <h2 id="h2-menu">Ponto</h2>
        <a href="/home"><button type="button"><i data-lucide="clock"></i> Registrar Ponto</button></a>
        <a href="/registers" class="menu-link"><button type="button"><i data-lucide="list"></i> Meus Registros</button></a>
        <a href="/relatorios" class="menu-link"><button type="button"><i data-lucide="bar-chart-2"></i> Relatórios</button></a>
    </nav>
    <main class="ponto">
        {{!base_content}}
    </main>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="/static/js/home.js"></script>
</body>
</html>
