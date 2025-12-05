
import json
import os
import smtplib
from email.mime.text import MIMEText
from app.models.trabalhador import Trabalhador


class DataRecord:
    """Gerenciador de dados para Trabalhadores com CRUD completo"""

    def __init__(self):
        self.file_path = "app/controllers/db/trabalhadores.json"
        self.trabalhadores = []
        self.next_id = 1
        self.load()

    def load(self):
        """Carrega os dados do arquivo JSON"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    self.trabalhadores = [Trabalhador.from_dict(t) for t in dados]
                    if self.trabalhadores:
                        self.next_id = max([t.id for t in self.trabalhadores]) + 1
                    else:
                        self.next_id = 1
            else:
                self.trabalhadores = []
                self.next_id = 1
        except (FileNotFoundError, json.JSONDecodeError):
            self.trabalhadores = []
            self.next_id = 1

    def save(self):
        """Salva os dados no arquivo JSON"""
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            dados = [t.to_dict() for t in self.trabalhadores]
            with open(self.file_path, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

  
    def create(self, dados):
        """Cria um novo trabalhador"""
        try:
            dados['id'] = self.next_id
            trabalhador = Trabalhador.from_dict(dados)
            self.trabalhadores.append(trabalhador)
            self.next_id += 1
            self.save()
            return trabalhador
        except Exception as e:
            print(f"Erro ao criar: {e}")
            return None

   
    def read_all(self):
        """Retorna todos os trabalhadores"""
        return self.trabalhadores

   
    def read_by_id(self, id):
        """Busca um trabalhador pelo ID"""
        for trabalhador in self.trabalhadores:
            if trabalhador.id == id:
                return trabalhador
        return None

    
    def _normalize_cpf(self, cpf):
        """Remove pontos, traços e espaços do CPF para comparação"""
        return ''.join(filter(str.isdigit, str(cpf)))

    def read_by_cpf(self, cpf):
        """Busca um trabalhador pelo CPF, ignorando máscara"""
        cpf_normalizado = self._normalize_cpf(cpf)
        print(f"[DEBUG] Procurando CPF: {cpf} (normalizado: {cpf_normalizado})")
        for trabalhador in self.trabalhadores:
            print(f"[DEBUG] Comparando com: {trabalhador.cpf} (normalizado: {self._normalize_cpf(trabalhador.cpf)})")
            if self._normalize_cpf(trabalhador.cpf) == cpf_normalizado:
                print(f"[DEBUG] CPF encontrado: {trabalhador.cpf}")
                return trabalhador
        print("[DEBUG] Nenhum trabalhador encontrado com esse CPF.")
        return None

  
    def read_by_email(self, email):
        """Busca um trabalhador pelo Email"""
        for trabalhador in self.trabalhadores:
            if trabalhador.email == email:
                return trabalhador
        return None


    def enviar_email(self, destinatario, nome):
        remetente = "seuemail@gmail.com"  # Troque para o e-mail do sistema
        senha_remetente = "sua_senha_de_app"  # Troque para a senha de app do Gmail
        assunto = "Bem-vindo ao Portal do Trabalhador"
        corpo = f"""
            Olá {nome},

            Seu cadastro foi realizado com sucesso!

            Sua senha inicial é: 1234

            Por segurança, troque sua senha no primeiro acesso.

            Atenciosamente,
            Equipe RH
            """
        msg = MIMEText(corpo)
        msg['Subject'] = assunto
        msg['From'] = remetente
        msg['To'] = destinatario
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(remetente, senha_remetente)
                server.sendmail(remetente, destinatario, msg.as_string())
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")



    def create(self, dados):
        """Cria um novo trabalhador"""
        try:
            dados['id'] = self.next_id
            dados['senha'] = '1234'
            dados['primeiro_acesso'] = True
            trabalhador = Trabalhador.from_dict(dados)
            self.trabalhadores.append(trabalhador)
            self.next_id += 1
            self.save()
            if 'email' in dados and dados['email']:
                self.enviar_email(dados['email'], dados.get('nomeCompleto', ''))
            return trabalhador
        except Exception as e:
            print(f"Erro ao criar: {e}")
            return None

    def delete(self, id):
        """Deleta um trabalhador pelo ID"""
        try:
            trabalhador = self.read_by_id(id)
            if trabalhador is None:
                return False
            self.trabalhadores.remove(trabalhador)
            self.save()
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def delete_by_cpf(self, cpf):
        """Deleta um trabalhador pelo CPF"""
        trabalhador = self.read_by_cpf(cpf)
        if trabalhador:
            return self.delete(trabalhador.id)
        return False

    def count(self):
        """Retorna a quantidade de trabalhadores"""
        return len(self.trabalhadores)

    def cpf_exists(self, cpf):
        """Verifica se um CPF já está cadastrado"""
        return self.read_by_cpf(cpf) is not None

    def email_exists(self, email):
        """Verifica se um Email já está cadastrado"""
        return self.read_by_email(email) is not None

    def search(self, termo, campo='nomeCompleto'):
        """Busca trabalhadores por um termo em um campo específico"""
        resultados = []
        for trabalhador in self.trabalhadores:
            if hasattr(trabalhador, campo):
                valor = getattr(trabalhador, campo)
                if termo.lower() in str(valor).lower():
                    resultados.append(trabalhador)
        return resultados
