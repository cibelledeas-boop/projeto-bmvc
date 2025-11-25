# 📋 BMVC II - Arquivos para Apresentação em Vídeo

## ✅ Critérios Atendidos:
- ✅ **Modelo customizado**: `Trabalhador` (diferente do exemplo em sala)
- ✅ **Página HTML/TPL customizada**: `cadastro.tpl` + `lista_trabalhadores.tpl` 
- ✅ **CRUD Completo**: Create, Read, Update, Delete
- ✅ **CSS funcional**: `cadastro.css` + `lista_trabalhadores.css`
- ✅ **JavaScript funcional**: `cadastro.js` + `lista_trabalhadores.js`
- ✅ **Backend (Python)**: Model, DataRecord, Controller, Routes
- ✅ **API REST**: Endpoints JSON para integração frontend-backend
- ✅ **Propósito claro**: Sistema de cadastro de trabalhadores/funcionários

---

## 📂 ESTRUTURA DE ARQUIVOS PARA APRESENTAR

### **🔴 ARQUIVOS PYTHON (Backend)**

#### 1. **`app/models/trabalhador.py`**
   - Modelo de dados customizado
   - Atributos: id, nomeCompleto, dataNascimento, sexo, estadoCivil, email, telefone, cpf, rg, pis, ctps, newsletter
   - Métodos: `to_dict()`, `from_dict()`
   - **Mostrar no vídeo**: Estrutura do modelo e como converte para JSON

#### 2. **`app/controllers/datarecord.py`**
   - Gerenciador CRUD completo
   - Métodos implementados:
     - `create()` - CREATE
     - `read_all()` - READ (listar todos)
     - `read_by_id()` - READ (buscar por ID)
     - `read_by_cpf()` - READ (buscar por CPF)
     - `update()` - UPDATE
     - `delete()` - DELETE
     - `search()` - SEARCH
     - `cpf_exists()`, `email_exists()` - Validações
   - Persistência em JSON: `app/controllers/db/trabalhadores.json`
   - **Mostrar no vídeo**: Salvando e carregando dados do JSON

#### 3. **`app/controllers/application.py`**
   - Controller que gerencia a lógica de negócio
   - Métodos CRUD: `create_trabalhador()`, `get_all_trabalhadores()`, `get_trabalhador()`, `update_trabalhador()`, `delete_trabalhador()`, `search_trabalhadores()`
   - Render de templates
   - **Mostrar no vídeo**: Como o controller integra modelo e view

#### 4. **`route.py`**
   - Rotas HTTP e API REST
   - **Endpoints implementados:**
     - `GET /` - Home
     - `GET /cadastro` - Página de cadastro
     - `GET /lista-trabalhadores` - Página de listagem
     - `POST /api/trabalhadores` - Criar novo
     - `GET /api/trabalhadores` - Listar todos
     - `GET /api/trabalhadores/<id>` - Buscar por ID
     - `PUT /api/trabalhadores/<id>` - Atualizar
     - `DELETE /api/trabalhadores/<id>` - Deletar
     - `GET /api/trabalhadores/search/<termo>` - Buscar
   - **Mostrar no vídeo**: Demonstrar que os endpoints respondem com JSON

---

### **🟢 ARQUIVOS FRONTEND (HTML/CSS/JS)**

#### 5. **`app/views/html/cadastro.tpl`**
   - Página HTML para cadastro de novo trabalhador
   - Formulário completo com validação
   - Campos: nomeCompleto, dataNascimento, sexo, estadoCivil, email, telefone, cpf, rg, pis, ctps, newsletter
   - Termos de uso obrigatórios
   - **Mostrar no vídeo**: Preenchimento do formulário e envio com sucesso

#### 6. **`app/views/html/lista_trabalhadores.tpl`**
   - Página HTML para visualizar todos os cadastros
   - Tabela com informações dos trabalhadores
   - Busca em tempo real
   - Modal para ver detalhes completos
   - Botões de ação: Ver detalhes e Deletar
   - **Mostrar no vídeo**: Listagem dos dados, busca funcionando, ver detalhes, deletar

#### 7. **`app/static/css/cadastro.css`**
   - Estilo do formulário de cadastro
   - Design responsivo
   - Variáveis CSS com paleta de cores
   - Efeitos de hover e focus
   - Validação visual (campos com erro)
   - **Mostrar no vídeo**: Carregamento correto do CSS, formulário estilizado

#### 8. **`app/static/css/lista_trabalhadores.css`**
   - Estilo da tabela de listagem
   - Design responsivo
   - Modal para detalhes
   - Tabela com paginação visual
   - **Mostrar no vídeo**: Carregamento correto do CSS, tabela estilizada

#### 9. **`app/static/js/cadastro.js`**
   - Validações em JavaScript:
     - Máscaras: CPF, RG, PIS, CEP, Telefone
     - Validação de CPF (algoritmo correto)
     - Validação de Email (regex)
   - Envio via AJAX (Fetch API):
     - `enviarCadastro()` - POST para `/api/trabalhadores`
     - `atualizarTrabalhador()` - PUT
     - `deletarTrabalhador()` - DELETE
     - `preencherFormulario()` - Popular campos
   - Mensagens de erro inline (sem alert())
   - **Mostrar no vídeo**: Preencher formulário, ver máscara funcionando, enviar e confirmação de sucesso

#### 10. **`app/static/js/lista_trabalhadores.js`**
   - Carregamento de dados via AJAX:
     - `carregarTrabalhadores()` - GET `/api/trabalhadores`
     - `verDetalhes()` - Abrir modal com dados
     - `deletarTrabalhador()` - DELETE com confirmação
     - `buscar()` - Busca em tempo real
   - Formatação de dados: CPF, CEP
   - **Mostrar no vídeo**: Carregar lista, buscar, ver detalhes, deletar registro

#### 11. **`app/controllers/db/trabalhadores.json`**
   - Banco de dados em JSON
   - Armazena todos os trabalhadores cadastrados
   - Estrutura: `[{id, nomeCompleto, dataNascimento, ...}, ...]`
   - **Mostrar no vídeo**: Abrir arquivo no editor e mostrar dados persistentes

---

## 🎬 ROTEIRO DO VÍDEO (Máximo 6 minutos)

### **Minuto 0-0:30** - Apresentação
- "Este é meu CRUD completo BMVC II de Cadastro de Trabalhadores"
- Mostrar a estrutura do projeto

### **Minuto 0:30-1:30** - Backend (Código Python)
1. Abrir `app/models/trabalhador.py`
   - Mostrar os atributos do modelo
   - Explicar métodos `to_dict()` e `from_dict()`
2. Abrir `app/controllers/datarecord.py`
   - Mostrar método `create()` - CREATE
   - Mostrar método `read_all()` - READ
   - Mostrar método `update()` - UPDATE
   - Mostrar método `delete()` - DELETE
   - Mencionar que persiste em JSON

### **Minuto 1:30-2:30** - Routes (API REST)
- Abrir `route.py`
- Mostrar os endpoints:
  - POST `/api/trabalhadores` - para criar
  - GET `/api/trabalhadores` - para listar
  - GET `/api/trabalhadores/<id>` - para buscar
  - PUT `/api/trabalhadores/<id>` - para atualizar
  - DELETE `/api/trabalhadores/<id>` - para deletar

### **Minuto 2:30-4:30** - Frontend Funcionando (Ação!)
1. Abrir `http://127.0.0.1:8080/cadastro`
   - Mostrar formulário (CSS carregado)
   - Preencher um cadastro:
     - Nome, data nascimento, sexo, estado civil
     - Email, telefone
     - CPF (mostrar a máscara funcionando: 123.456.789-09)
     - RG, PIS, CTPS
     - Aceitar termos
   - Clicar em "Concluir Cadastro"
   - Mostrar confirmação de sucesso (sem alert, apenas mensagem)

2. Abrir `http://127.0.0.1:8080/lista-trabalhadores`
   - Mostrar tabela com dados (CSS carregado)
   - **Funcionalidades:**
     - Listar trabalhadores cadastrados
     - Mostrar coluna: ID, Nome, CPF, Email, Telefone, Sexo
     - Clicar em "👁️ Ver" para abrir modal com detalhes completos
     - Fechar modal
     - Usar busca para filtrar (ex: digitar o nome)
     - Clicar em "🗑️ Del" para deletar um registro
     - Confirmação de delete

3. Abrir DevTools (F12) > Network
   - Fazer uma requisição POST ao cadastro
   - Mostrar que recebe JSON com status 200
   - Abrir a lista
   - Mostrar requisição GET retornando os dados em JSON

### **Minuto 4:30-5:30** - Arquivos Estáticos
1. Mostrar carregamento de CSS:
   - Abrir DevTools > Network > XHR
   - Filtrar por "css"
   - Mostrar `/static/css/cadastro.css` com status 200
   - Mostrar `/static/css/lista_trabalhadores.css` com status 200

2. Mostrar carregamento de JS:
   - Filtrar por ".js"
   - Mostrar `/static/js/cadastro.js` com status 200
   - Mostrar `/static/js/lista_trabalhadores.js` com status 200

### **Minuto 5:30-6:00** - Arquivo JSON e Conclusão
- Abrir VS Code
- Mostrar `app/controllers/db/trabalhadores.json`
- Mostrar que contém os dados cadastrados em formato JSON
- **Conclusão**: "Assim, demonstrei um CRUD completo com:
  - ✅ Modelo Trabalhador customizado
  - ✅ CRUD Create, Read, Update, Delete
  - ✅ Páginas HTML/TPL customizadas
  - ✅ CSS funcional e responsivo
  - ✅ JavaScript com validações e AJAX
  - ✅ API REST com 6 endpoints
  - ✅ Persistência em JSON"

---

## 📋 CHECKLIST PARA O VÍDEO

- [ ] Servidor rodando (`python route.py`)
- [ ] Navegador aberto em `http://127.0.0.1:8080`
- [ ] VS Code aberto com os arquivos
- [ ] DevTools (F12) pronto para mostrar network
- [ ] Terminal/Cmd para mostrar servidor respondendo
- [ ] Banco de dados JSON aberto
- [ ] Áudio claro
- [ ] Câmera focada na tela
- [ ] Duração máxima: 6 minutos
- [ ] Mostrar fluente e com segurança

---

## 📁 RESUMO DOS ARQUIVOS PRINCIPAIS

```
Projeto-BMVC/
├── app/
│   ├── models/
│   │   └── trabalhador.py ...................... ✅ Modelo customizado
│   ├── controllers/
│   │   ├── application.py ...................... ✅ Controller
│   │   ├── datarecord.py ....................... ✅ CRUD completo
│   │   └── db/
│   │       └── trabalhadores.json ............. ✅ Banco de dados
│   ├── views/html/
│   │   ├── cadastro.tpl ........................ ✅ Formulário
│   │   └── lista_trabalhadores.tpl ............ ✅ Listagem
│   └── static/
│       ├── css/
│       │   ├── cadastro.css ................... ✅ Estilo form
│       │   └── lista_trabalhadores.css ........ ✅ Estilo lista
│       └── js/
│           ├── cadastro.js ................... ✅ Lógica form
│           └── lista_trabalhadores.js ........ ✅ Lógica lista
└── route.py ................................. ✅ Rotas e API REST
```

---

## 🎯 DIFERENCIAIS PARA DESTAQUE

1. **Validações robustas**:
   - CPF com algoritmo correto
   - Email com regex
   - Mensagens de erro inline

2. **UX melhorada**:
   - Máscaras de entrada
   - Sem alert() desagradável
   - Modal elegante para detalhes
   - Busca em tempo real

3. **Código profissional**:
   - Separação de responsabilidades (Model-View-Controller)
   - API REST bem estruturada
   - Persistência em JSON
   - Comentários no código

4. **Design responsivo**:
   - CSS com Flexbox/Grid
   - Mobile-friendly
   - Cores e tipografia profissionais

---

## ✨ CONCLUSÃO

Ao apresentar estes arquivos no vídeo, você estará demonstrando:
- ✅ Conhecimento completo de BMVC
- ✅ Capacidade de criar sistemas CRUD
- ✅ Integração frontend-backend
- ✅ Boas práticas de desenvolvimento
- ✅ Atenção aos detalhes (UX/UI)

**Boa sorte com a apresentação! 🚀**
