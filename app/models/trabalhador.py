class Trabalhador:
    """Modelo para representar um Trabalhador/Funcionário"""
    
    def __init__(self, id=None, nomeCompleto='', dataNascimento='', sexo='', 
                 estadoCivil='', email='', telefone='', cpf='', rg='', pis='', 
                 ctps='', newsletter=False):
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
            'newsletter': self.newsletter
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Trabalhador a partir de um dicionário"""
        return Trabalhador(**data)
