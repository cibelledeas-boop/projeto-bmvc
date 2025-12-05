
from bottle import template
from app.controllers.datarecord import DataRecord


class Application():
    def atualizar_senha(self, cpf, nova_senha):
        trabalhador = self.db.read_by_cpf(cpf)
        if trabalhador:
            trabalhador.senha = nova_senha
            if hasattr(trabalhador, 'primeiro_acesso'):
                trabalhador.primeiro_acesso = False
            else:
                setattr(trabalhador, 'primeiro_acesso', False)
            self.db.save()
            return True
        return False

    def __init__(self):
        self.pages = {
            'home': self.home,
            'registers': self.registers,
            'login': self.login,
            'cadastro': self.cadastro,
            'relatorios': self.relatorios,
            'pagina': self.pagina,
            'lista_trabalhadores': self.lista_trabalhadores
        }
        self.db = DataRecord()


    def render(self, page, parameter=None, **kwargs):
        content = self.pages.get(page, self.helper)
        if parameter:
            return content(parameter, **kwargs)
        return content(**kwargs)



    def helper(self, **kwargs):
        return template('helper.tpl', **kwargs)

    def home(self, nome_usuario=None, **kwargs):
        return template('home.tpl', nome_usuario=nome_usuario, **kwargs)

    def registers(self, **kwargs):
        return template('registers.tpl', **kwargs)

    def login(self, erro=None, **kwargs):
        return template('login.tpl', erro=erro, **kwargs)

    def authenticate_user(self, cpf, senha):
        print(f"[DEBUG] Autenticando CPF: {cpf} | Senha: {senha}")
        trabalhador = self.db.read_by_cpf(cpf)
        if trabalhador:
            print(f"[DEBUG] Trabalhador encontrado: {trabalhador.cpf} | Senha salva: {getattr(trabalhador, 'senha', None)}")
        else:
            print("[DEBUG] Nenhum trabalhador encontrado para este CPF.")
        if trabalhador and hasattr(trabalhador, 'senha') and trabalhador.senha == senha:
            if hasattr(trabalhador, 'primeiro_acesso') and trabalhador.primeiro_acesso:
                return 'primeiro_acesso'
            return True
        return False

    def cadastro(self, **kwargs):
        return template('cadastro.tpl', **kwargs)

    def relatorios(self, **kwargs):
        return template('relatorios.tpl', **kwargs)

    def pagina(self, **kwargs):
        return template('pagina.tpl', **kwargs)

    def lista_trabalhadores(self, **kwargs):
        return template('lista_trabalhadores.tpl', **kwargs)



    def create_trabalhador(self, dados):
        """Cria um novo trabalhador"""
        return self.db.create(dados)

    def get_all_trabalhadores(self):
        """Retorna todos os trabalhadores"""
        return self.db.read_all()

    def get_trabalhador(self, id):
        """Busca um trabalhador pelo ID"""
        return self.db.read_by_id(int(id))

    def update_trabalhador(self, id, dados):
        """Atualiza um trabalhador"""
        return self.db.update(int(id), dados)

    def delete_trabalhador(self, id):
        """Deleta um trabalhador"""
        return self.db.delete(int(id))

    def trabalhador_exists(self, cpf):
        """Verifica se um CPF já existe"""
        return self.db.cpf_exists(cpf)

    def search_trabalhadores(self, termo, campo='nomeCompleto'):
        """Busca trabalhadores"""
        return self.db.search(termo, campo)