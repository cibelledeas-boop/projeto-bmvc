
function mascaraCPF(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2')
        .slice(0, 14);
}

function mascaraRG(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2')
        .slice(0, 12);
}


function mascaraPIS(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{5})(\d)/, '$1.$2')
        .replace(/(\d{2})(\d{1,2})$/, '$1-$2')
        .slice(0, 14);
}


function mascaraCEP(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{5})(\d)/, '$1-$2')
        .slice(0, 9);
}


function mascaraTelefone(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '($1) $2')
        .replace(/(\d{5})(\d)/, '$1-$2')
        .slice(0, 15);
}

function validarCPF(cpf) {
    cpf = cpf.replace(/\D/g, '');

    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
        return false;
    }

    let soma = 0;
    let resto;

    for (let i = 1; i <= 9; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }

    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) {
        resto = 0;
    }

    if (resto !== parseInt(cpf.substring(9, 10))) {
        return false;
    }

    soma = 0;
    for (let i = 1; i <= 10; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    }

    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) {
        resto = 0;
    }

    if (resto !== parseInt(cpf.substring(10, 11))) {
        return false;
    }

    return true;
}


function validarEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cadastroForm');
    const cpfInput = document.getElementById('cpf');
    const rgInput = document.getElementById('rg');
    const pisInput = document.getElementById('pis');
    const cepInput = document.getElementById('cep');
    const telefoneInput = document.getElementById('telefone');
    const emailInput = document.getElementById('email');

  
    if (cpfInput) {
        cpfInput.addEventListener('input', function() {
            this.value = mascaraCPF(this.value);
            // Limpar mensagem de erro quando o usuário começa a digitar
            this.style.borderColor = '';
            this.style.backgroundColor = '';
            this.classList.remove('input-error');
            const msgAnterior = this.parentElement.querySelector('.error-message');
            if (msgAnterior) msgAnterior.remove();
        });
    }

    if (rgInput) {
        rgInput.addEventListener('input', function() {
            this.value = mascaraRG(this.value);
        });
    }

    if (pisInput) {
        pisInput.addEventListener('input', function() {
            this.value = mascaraPIS(this.value);
        });
    }

    if (cepInput) {
        cepInput.addEventListener('input', function() {
            this.value = mascaraCEP(this.value);
        });
    }

    if (telefoneInput) {
        telefoneInput.addEventListener('input', function() {
            this.value = mascaraTelefone(this.value);
        });
    }

    if (cpfInput) {
        cpfInput.addEventListener('blur', function() {
            if (this.value && !validarCPF(this.value)) {
                this.style.borderColor = '#dc3545';
                this.style.backgroundColor = '#fff5f5';
                this.classList.add('input-error');
                // Remover mensagem de erro anterior se existir
                const msgAnterior = this.parentElement.querySelector('.error-message');
                if (msgAnterior) msgAnterior.remove();
                // Criar mensagem de erro
                const errorMsg = document.createElement('small');
                errorMsg.className = 'error-message';
                errorMsg.style.color = '#dc3545';
                errorMsg.style.display = 'block';
                errorMsg.style.marginTop = '4px';
                errorMsg.textContent = '❌ CPF inválido! Verifique e tente novamente.';
                this.parentElement.appendChild(errorMsg);
            } else {
                this.style.borderColor = '';
                this.style.backgroundColor = '';
                this.classList.remove('input-error');
                const msgAnterior = this.parentElement.querySelector('.error-message');
                if (msgAnterior) msgAnterior.remove();
            }
        });
    }

    
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            if (this.value && !validarEmail(this.value)) {
                this.style.borderColor = '#dc3545';
                this.style.backgroundColor = '#fff5f5';
                this.classList.add('input-error');
                // Remover mensagem de erro anterior se existir
                const msgAnterior = this.parentElement.querySelector('.error-message');
                if (msgAnterior) msgAnterior.remove();
                // Criar mensagem de erro
                const errorMsg = document.createElement('small');
                errorMsg.className = 'error-message';
                errorMsg.style.color = '#dc3545';
                errorMsg.style.display = 'block';
                errorMsg.style.marginTop = '4px';
                errorMsg.textContent = '❌ E-mail inválido! Verifique e tente novamente.';
                this.parentElement.appendChild(errorMsg);
            } else {
                this.style.borderColor = '';
                this.style.backgroundColor = '';
                this.classList.remove('input-error');
                const msgAnterior = this.parentElement.querySelector('.error-message');
                if (msgAnterior) msgAnterior.remove();
            }
        });
    }

    
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Validar CPF
        if (!validarCPF(cpfInput.value)) {
            cpfInput.style.borderColor = '#dc3545';
            cpfInput.style.backgroundColor = '#fff5f5';
            cpfInput.classList.add('input-error');
            // Remover mensagem anterior se existir
            const msgAnterior = cpfInput.parentElement.querySelector('.error-message');
            if (msgAnterior) msgAnterior.remove();
            // Criar mensagem de erro
            const errorMsg = document.createElement('small');
            errorMsg.className = 'error-message';
            errorMsg.style.color = '#dc3545';
            errorMsg.style.display = 'block';
            errorMsg.style.marginTop = '4px';
            errorMsg.textContent = '❌ CPF inválido!';
            cpfInput.parentElement.appendChild(errorMsg);
            cpfInput.focus();
            return;
        }

        // Validar Email
        if (!validarEmail(emailInput.value)) {
            emailInput.style.borderColor = '#dc3545';
            emailInput.style.backgroundColor = '#fff5f5';
            emailInput.classList.add('input-error');
            // Remover mensagem anterior se existir
            const msgAnterior = emailInput.parentElement.querySelector('.error-message');
            if (msgAnterior) msgAnterior.remove();
            // Criar mensagem de erro
            const errorMsg = document.createElement('small');
            errorMsg.className = 'error-message';
            errorMsg.style.color = '#dc3545';
            errorMsg.style.display = 'block';
            errorMsg.style.marginTop = '4px';
            errorMsg.textContent = '❌ E-mail inválido!';
            emailInput.parentElement.appendChild(errorMsg);
            emailInput.focus();
            return;
        }

        // Validar Termos
        const termos = document.getElementById('termos');
        if (!termos.checked) {
            alert('⚠️ Você deve aceitar os Termos de Uso e Política de Privacidade para continuar.');
            termos.focus();
            return;
        }

        
        const dados = {
            nomeCompleto: document.getElementById('nomeCompleto').value,
            dataNascimento: document.getElementById('dataNascimento').value,
            sexo: document.getElementById('sexo').value,
            estadoCivil: document.getElementById('estadoCivil').value,
            email: document.getElementById('email').value,
            telefone: document.getElementById('telefone').value,
            cpf: document.getElementById('cpf').value,
            rg: document.getElementById('rg').value,
            pis: document.getElementById('pis').value,
            ctps: document.getElementById('ctps').value,
            newsletter: document.getElementById('newsletter').checked
        };

    
        enviarCadastro(dados);
    });

    form.addEventListener('reset', function() {
        document.querySelectorAll('input, select').forEach(field => {
            field.style.borderColor = '';
            field.style.backgroundColor = '';
            field.classList.remove('input-error');
            // Remover mensagens de erro
            const msgErro = field.parentElement.querySelector('.error-message');
            if (msgErro) msgErro.remove();
        });
    });
});


function enviarCadastro(dados) {
    fetch('/api/trabalhadores', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            alert('Cadastro realizado com sucesso!\nID: ' + resultado.data.id);
            document.getElementById('cadastroForm').reset();
            
            localStorage.setItem('cadastroTrabalhador_' + resultado.data.id, JSON.stringify(resultado.data));
        } else {
            alert('Erro: ' + resultado.message);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao enviar o formulário: ' + error);
    });
}


function buscarTodosTrabalhadores() {
    fetch('/api/trabalhadores', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            console.log('Trabalhadores:', resultado.data);
            return resultado.data;
        } else {
            console.error('Erro:', resultado.message);
            return [];
        }
    })
    .catch(error => console.error('Erro:', error));
}

function buscarTrabalhador(id) {
    fetch('/api/trabalhadores/' + id, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            console.log('Trabalhador:', resultado.data);
            preencherFormulario(resultado.data);
        } else {
            alert('Trabalhador não encontrado: ' + resultado.message);
        }
    })
    .catch(error => console.error('Erro:', error));
}


function atualizarTrabalhador(id, dados) {
    fetch('/api/trabalhadores/' + id, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            alert('Trabalhador atualizado com sucesso!');
            console.log('Dados atualizados:', resultado.data);
        } else {
            alert('Erro: ' + resultado.message);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao atualizar: ' + error);
    });
}


function deletarTrabalhador(id) {
    if (confirm('Tem certeza que deseja deletar este trabalhador?')) {
        fetch('/api/trabalhadores/' + id, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(resultado => {
            if (resultado.success) {
                alert('Trabalhador deletado com sucesso!');
                document.getElementById('cadastroForm').reset();
            } else {
                alert('Erro: ' + resultado.message);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao deletar: ' + error);
        });
    }
}

// Buscar trabalhadores por termo
function buscarTrabalhadores(termo, campo = 'nomeCompleto') {
    fetch('/api/trabalhadores/search/' + encodeURIComponent(termo) + '?campo=' + campo, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            console.log('Resultados da busca:', resultado.data);
            return resultado.data;
        } else {
            console.error('Erro:', resultado.message);
            return [];
        }
    })
    .catch(error => console.error('Erro:', error));
}

// Preencher formulário com dados de um trabalhador
function preencherFormulario(dados) {
    document.getElementById('nomeCompleto').value = dados.nomeCompleto || '';
    document.getElementById('dataNascimento').value = dados.dataNascimento || '';
    document.getElementById('sexo').value = dados.sexo || '';
    document.getElementById('estadoCivil').value = dados.estadoCivil || '';
    document.getElementById('email').value = dados.email || '';
    document.getElementById('telefone').value = dados.telefone || '';
    document.getElementById('cpf').value = dados.cpf || '';
    document.getElementById('rg').value = dados.rg || '';
    document.getElementById('pis').value = dados.pis || '';
    document.getElementById('ctps').value = dados.ctps || '';
    document.getElementById('newsletter').checked = dados.newsletter || false;
}
