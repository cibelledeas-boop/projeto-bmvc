let todosOsDados = [];
let usuarioSelecionado = null;


function carregarTrabalhadores() {
    const loadingMsg = document.getElementById('loadingMsg');
    const emptyMsg = document.getElementById('emptyMsg');
    const table = document.getElementById('trabalhadorTable');
    
    loadingMsg.style.display = 'block';
    table.style.display = 'none';
    emptyMsg.style.display = 'none';

    fetch('/api/trabalhadores', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(resultado => {
        loadingMsg.style.display = 'none';

        if (resultado.success && resultado.data.length > 0) {
            todosOsDados = resultado.data;
            preencherTabela(resultado.data);
            document.getElementById('totalRegistros').textContent = resultado.data.length;
            table.style.display = 'table';
            emptyMsg.style.display = 'none';
        } else {
            emptyMsg.style.display = 'block';
            table.style.display = 'none';
            document.getElementById('totalRegistros').textContent = '0';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        loadingMsg.style.display = 'none';
        emptyMsg.style.display = 'block';
        alert('Erro ao carregar dados: ' + error);
    });
}

function preencherTabela(dados) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    dados.forEach(trabalhador => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>#${trabalhador.id}</td>
            <td>${trabalhador.nomeCompleto}</td>
            <td>${formatarCPF(trabalhador.cpf)}</td>
            <td>${trabalhador.email}</td>
            <td>${trabalhador.telefone}</td>
            <td>${trabalhador.sexo}</td>
            <td>
                <div class="action-buttons">
                    <button onclick="verDetalhes(${trabalhador.id})" class="btn btn-small btn-view">👁️ Ver</button>
                    <button onclick="deletarTrabalhador(${trabalhador.id})" class="btn btn-small btn-delete">🗑️ Del</button>
                </div>
            </td>
        `;
        tableBody.appendChild(row);
    });
}


function verDetalhes(id) {
    const trabalhador = todosOsDados.find(t => t.id === id);
    if (!trabalhador) {
        alert('Trabalhador não encontrado');
        return;
    }

    usuarioSelecionado = id;
    const detailsContent = document.getElementById('detailsContent');
    
    detailsContent.innerHTML = `
        <div class="detail-grid">
            <div class="detail-item">
                <div class="detail-label">ID</div>
                <div class="detail-value">#${trabalhador.id}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Nome Completo</div>
                <div class="detail-value">${trabalhador.nomeCompleto}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">CPF</div>
                <div class="detail-value">${formatarCPF(trabalhador.cpf)}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Email</div>
                <div class="detail-value">${trabalhador.email}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Telefone</div>
                <div class="detail-value">${trabalhador.telefone}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Data de Nascimento</div>
                <div class="detail-value">${trabalhador.dataNascimento}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Sexo</div>
                <div class="detail-value">${trabalhador.sexo}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Estado Civil</div>
                <div class="detail-value">${trabalhador.estadoCivil}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">RG</div>
                <div class="detail-value">${trabalhador.rg}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">PIS/PASEP</div>
                <div class="detail-value">${trabalhador.pis || 'N/A'}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">CTPS</div>
                <div class="detail-value">${trabalhador.ctps || 'N/A'}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Newsletter</div>
                <div class="detail-value">${trabalhador.newsletter ? '✅ Sim' : '❌ Não'}</div>
            </div>
        </div>
    `;

    document.getElementById('detailsModal').classList.add('active');
}


function fecharModal() {
    document.getElementById('detailsModal').classList.remove('active');
    usuarioSelecionado = null;
}


function deletarSelecionado() {
    if (usuarioSelecionado) {
        deletarTrabalhador(usuarioSelecionado);
        fecharModal();
    }
}

function deletarTrabalhador(id) {
    if (!confirm('Tem certeza que deseja deletar este trabalhador?')) {
        return;
    }

    fetch('/api/trabalhadores/' + id, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            alert('Trabalhador deletado com sucesso!');
            carregarTrabalhadores();
        } else {
            alert('Erro: ' + resultado.message);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao deletar: ' + error);
    });
}

function buscar() {
    const termo = document.getElementById('searchInput').value;
    
    if (termo.trim() === '') {
        preencherTabela(todosOsDados);
        return;
    }

    fetch('/api/trabalhadores/search/' + encodeURIComponent(termo) + '?campo=nomeCompleto', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(resultado => {
        if (resultado.success) {
            preencherTabela(resultado.data);
        } else {
            alert('Erro: ' + resultado.message);
        }
    })
    .catch(error => console.error('Erro:', error));
}

function formatarCPF(cpf) {
    if (!cpf) return '';
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

function formatarCEP(cep) {
    if (!cep) return '';
    return cep.replace(/(\d{5})(\d{3})/, '$1-$2');
}


document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keyup', buscar);
    }
});
