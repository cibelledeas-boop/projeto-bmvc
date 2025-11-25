<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Portal do Trabalhador — Login</title>
    <link rel="stylesheet" href="login.css">
</head>
<body>
    <main class="page">
        <div class="card">
            <div class="brand">
                <div class="brand-icon">🏢</div>
                <div class="brand-title">Portal do Trabalhador</div>
            </div>

            <h1 class="title">Bem-vindo de volta</h1>
            <p class="subtitle">Entre com suas credenciais para acessar o portal</p>

            <form id="loginForm" class="login-form" autocomplete="off">
                <label class="field">
                    <span class="label">CPF</span>
                    <input id="cpf" name="cpf" type="text" inputmode="numeric" placeholder="000.000.000-00" autocomplete="username" required>
                </label>

                <label class="field">
                    <span class="label">Senha</span>
                    <div class="password-row">
                        <input id="senha" name="senha" type="password" placeholder="Digite sua senha" autocomplete="current-password" required>
                        <button type="button" id="toggleSenha" class="toggle-senha" aria-label="Mostrar senha">👁️</button>
                    </div>
                </label>

                <div class="row between">
                    <label class="checkbox-inline">
                        <input id="lembrar" type="checkbox">
                        <span>Lembrar de mim</span>
                    </label>

                    <a class="link" href="#">Esqueceu a senha?</a>
                </div>

                <button class="btn primary" type="submit">Entrar</button>

                <div class="divider">
                    <span>Não tem uma conta?</span>
                </div>

                <button type="button" class="btn secondary">Criar nova conta</button>

                <p class="note">Para sua segurança, nunca compartilhe sua senha. Em caso de dúvidas, entre em contato com o suporte.</p>
            </form>
        </div>
    </main>

    <script src="login.js"></script>
</body>
</html>
