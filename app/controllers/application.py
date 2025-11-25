from bottle import template
from app.controllers.datarecord import DataRecord


class Application():

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


    def render(self, page, parameter=None):
       content = self.pages.get(page, self.helper)
       if parameter:
           return content(parameter)
       return content()


    def helper(self):
        return template('helper.tpl')

    def home(self):
        return template('home.tpl')
    
    def registers(self):
        return template('registers.tpl')
    
    def login(self):
        return template('login.tpl')
    
    def cadastro(self):
        return template('cadastro.tpl')
    
    def relatorios(self):
        return template('relatorios.tpl')

    def pagina(self):
        return template('pagina.tpl')

    def lista_trabalhadores(self):
        return template('lista_trabalhadores.tpl')

    # Métodos para CRUD de Trabalhador

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