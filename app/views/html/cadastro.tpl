<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Trabalhador</title>
    <link rel="stylesheet" href="/static/css/cadastro.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Cadastro de Trabalhador</h1>
            <p>Preencha o formulário abaixo com seus dados pessoais e profissionais para se cadastrar no Portal do Trabalhador. Todos os campos marcados com <span class="required">*</span> são obrigatórios.</p>
        </header>

        <form class="form" id="cadastroForm">
            <!-- Dados Pessoais -->
            <section class="form-section">
                <div class="section-header">
                    <span class="section-icon">👤</span>
                    <div>
                        <h2>Dados Pessoais</h2>
                        <p>Informações básicas de identificação</p>
                    </div>
                </div>

                <div class="form-group-row">
                    <div class="form-group">
                        <label for="nomeCompleto">Nome Completo <span class="required">*</span></label>
                        <input type="text" id="nomeCompleto" name="nomeCompleto" placeholder="Digite seu nome completo" required>
                    </div>
                    <div class="form-group">
                        <label for="dataNascimento">Data de Nascimento <span class="required">*</span></label>
                        <input type="date" id="dataNascimento" name="dataNascimento" placeholder="dd/mm/aaaa" required>
                    </div>
                </div>

                <div class="form-group-row">
                    <div class="form-group">
                        <label for="sexo">Sexo <span class="required">*</span></label>
                        <select id="sexo" name="sexo" required>
                            <option value="">Selecione</option>
                            <option value="masculino">Masculino</option>
                            <option value="feminino">Feminino</option>
                            <option value="outro">Outro</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="estadoCivil">Estado Civil <span class="required">*</span></label>
                        <select id="estadoCivil" name="estadoCivil" required>
                            <option value="">Selecione</option>
                            <option value="solteiro">Solteiro(a)</option>
                            <option value="casado">Casado(a)</option>
                            <option value="divorciado">Divorciado(a)</option>
                            <option value="viuvo">Viúvo(a)</option>
                        </select>
                    </div>
                </div>

                <div class="form-group-row">
                    <div class="form-group">
                        <label for="email">E-mail <span class="required">*</span></label>
                        <input type="email" id="email" name="email" placeholder="seu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label for="telefone">Telefone/Celular <span class="required">*</span></label>
                        <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" required>
                    </div>
                </div>
            </section>

            <section class="form-section">
                <div class="section-header">
                    <span class="section-icon">📄</span>
                    <div>
                        <h2>Documentação</h2>
                        <p>Documentos de identificação e registro</p>
                    </div>
                </div>

                <div class="form-group-row">
                    <div class="form-group">
                        <label for="cpf">CPF <span class="required">*</span></label>
                        <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>
                    </div>
                    <div class="form-group">
                        <label for="rg">RG <span class="required">*</span></label>
                        <input type="text" id="rg" name="rg" placeholder="00.000.000-0" required>
                    </div>
                </div>

                <div class="form-group-row">
                    <div class="form-group">
                        <label for="pis">PIS/PASEP</label>
                        <input type="text" id="pis" name="pis" placeholder="000.00000.00-0">
                    </div>
                    <div class="form-group">
                        <label for="ctps">Carteira de Trabalho (CTPS)</label>
                        <input type="text" id="ctps" name="ctps" placeholder="Número da CTPS">
                    </div>
                </div>
            </section>
            
            <section class="form-section">
                <div class="checkbox-group">
                    <label class="checkbox-label">
                        <input type="checkbox" id="termos" name="termos" required>
                        <span>Li e aceito os <a href="#" target="_blank">Termos de Uso</a> e a <a href="#" target="_blank">Política de Privacidade</a> do Portal do Trabalhador. <span class="required">*</span></span>
                    </label>
                </div>

                <div class="checkbox-group">
                    <label class="checkbox-label">
                        <input type="checkbox" id="newsletter" name="newsletter">
                        <span>Desejo receber informações sobre oportunidades de emprego, cursos e benefícios por e-mail.</span>
                    </label>
                </div>
            </section>

            <section class="form-actions">
                <button type="reset" class="btn btn-secondary">Limpar Formulário</button>
                <button type="submit" class="btn btn-primary">Concluir Cadastro</button>
            </section>
        </form>
    </div>

    <script src="/static/js/cadastro.js"></script>
</body>
</html>
