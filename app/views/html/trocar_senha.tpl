<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trocar Senha</title>
    <link rel="stylesheet" href="/static/css/login.css">
</head>
<body>
    <main class="page">
        <div class="card">
            <h1 class="title">Troca de Senha</h1>
            <p class="subtitle">Por segurança, defina uma nova senha para continuar.</p>
            % if erro:
                <div class="erro">{{erro}}</div>
            % end
            <form class="login-form" method="post" action="/trocar_senha">
                <label class="field">
                    <span class="label">Nova senha</span>
                    <input name="nova_senha" type="password" placeholder="Digite a nova senha" required>
                </label>
                <label class="field">
                    <span class="label">Confirmar nova senha</span>
                    <input name="confirmar_senha" type="password" placeholder="Confirme a nova senha" required>
                </label>
                <button class="btn primary" type="submit">Salvar nova senha</button>
            </form>
        </div>
    </main>
</body>
</html>
