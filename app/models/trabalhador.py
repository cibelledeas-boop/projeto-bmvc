
class Trabalhador:
    """Modelo para representar um Trabalhador/Funcionário"""
    def __init__(self, id=None, nomeCompleto='', dataNascimento='', sexo='', 
                 estadoCivil='', email='', telefone='', cpf='', rg='', pis='', 
                 ctps='', newsletter=False, senha=None, primeiro_acesso=None):
        self.id = id
        self.nomeCompleto = nomeCompleto
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.rg = rg
        self.pis = pis
        self.ctps = ctps
        self.newsletter = newsletter
        self.senha = senha
        self.primeiro_acesso = primeiro_acesso

    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nomeCompleto': self.nomeCompleto,
            'dataNascimento': self.dataNascimento,
            'sexo': self.sexo,
            'estadoCivil': self.estadoCivil,
            'email': self.email,
            'telefone': self.telefone,
            'cpf': self.cpf,
            'rg': self.rg,
            'pis': self.pis,
            'ctps': self.ctps,
            'newsletter': self.newsletter,
            'senha': self.senha,
            'primeiro_acesso': self.primeiro_acesso
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Trabalhador a partir de um dicionário"""
        # Agora inclui senha e primeiro_acesso
        return Trabalhador(
            id=data.get('id'),
            nomeCompleto=data.get('nomeCompleto', ''),
            dataNascimento=data.get('dataNascimento', ''),
            sexo=data.get('sexo', ''),
            estadoCivil=data.get('estadoCivil', ''),
            email=data.get('email', ''),
            telefone=data.get('telefone', ''),
            cpf=data.get('cpf', ''),
            rg=data.get('rg', ''),
            pis=data.get('pis', ''),
            ctps=data.get('ctps', ''),
            newsletter=data.get('newsletter', False),
            senha=data.get('senha'),
            primeiro_acesso=data.get('primeiro_acesso')
        )
