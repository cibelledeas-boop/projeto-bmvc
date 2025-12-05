print('=== [DEBUG] Iniciando route.py ===')
import os
import json
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response, TEMPLATE_PATH


base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'app', 'views', 'html')
TEMPLATE_PATH.insert(0, template_dir)


app = Bottle()
ctl = Application()

# ROTA DE LOGOUT
@app.route('/logout', method='GET')
def logout():
    response.delete_cookie('user_cpf')
    return redirect('/login')

@app.route('/trocar_senha', method=['GET', 'POST'])
def trocar_senha():
    cpf = request.get_cookie('user_cpf')
    if not cpf:
        return redirect('/login')
    if request.method == 'GET':
        return template('trocar_senha.tpl', erro=None)
    nova = request.forms.get('nova_senha')
    confirmar = request.forms.get('confirmar_senha')
    if not nova or not confirmar:
        return template('trocar_senha.tpl', erro='Preencha todos os campos.')
    if nova != confirmar:
        return template('trocar_senha.tpl', erro='Senhas não conferem.')
    if ctl.atualizar_senha(cpf, nova):
        response.delete_cookie('user_cpf')
        return template('login.tpl', erro='Senha alterada com sucesso! Faça login novamente.')
    else:
        return template('trocar_senha.tpl', erro='Erro ao atualizar senha.')


@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/')
@app.route('/helper')
def action_helper(info=None):
    return ctl.render('helper')


@app.route('/pagina', methods=['GET'])
def action_pagina():
    return ctl.render('pagina')

@app.route('/home', method='GET')
def home():
    cpf = request.get_cookie('user_cpf')
    nome = None
    trabalhador = None
    if cpf:
        trabalhador = ctl.db.read_by_cpf(cpf)
        if trabalhador:
            print(f"[DEBUG] Verificando primeiro_acesso: {trabalhador.primeiro_acesso} (type: {type(trabalhador.primeiro_acesso)})")
            # Bloqueia se primeiro_acesso for True, 'true', 1, etc.
            valor = trabalhador.primeiro_acesso
            # Converte para booleano, considerando string 'true', 1, etc.
            bloqueio = bool(valor) and str(valor).lower() not in ['false', '0', 'none', '']
            print(f"[DEBUG] Verificando primeiro_acesso: {valor} (type: {type(valor)}) | bloqueio={bloqueio}")
            if bloqueio:
                print(f"[DEBUG] BLOQUEIO ATIVADO: primeiro_acesso={valor} (type: {type(valor)})")
                return redirect('/trocar_senha')
        if trabalhador and getattr(trabalhador, 'nomeCompleto', None):
            nome = trabalhador.nomeCompleto
    if not nome:
        nome = 'usuário'
    print(f"[DEBUG] home.tpl - CPF: {cpf} | Nome: {nome}")
    return template('home.tpl', nome_usuario=nome, cpf=cpf)

@app.route('/registers', method='GET')
def registers():
    return ctl.render('registers')


@app.route('/login', method='GET')
def login():
    return ctl.render('login', None, erro=None)

@app.route('/login', method='POST')
def login_post():
    print('=== [DEBUG] Entrou na rota POST /login ===')
    cpf = request.forms.get('cpf')
    senha = request.forms.get('senha')
    print(f'[DEBUG] Dados recebidos: cpf={cpf}, senha={senha}')
    resultado = ctl.authenticate_user(cpf, senha)
    if resultado == 'primeiro_acesso':
        response.set_cookie('user_cpf', cpf, path='/')
        return redirect('/trocar_senha')
    elif resultado is True:
        response.set_cookie('user_cpf', cpf, path='/')
        redirect('/home')
    else:
        return ctl.render('login', None, erro='CPF ou senha inválidos')

@app.route('/relatorios', method='GET')
def relatorios():
    cpf = request.get_cookie('user_cpf')
    trabalhador = ctl.db.read_by_cpf(cpf) if cpf else None
    # Permite apenas Julia ou Cibelle acessar
    nomes_gerentes = ['julia', 'cibelle']
    nome_usuario = trabalhador.nomeCompleto.strip().lower() if trabalhador and trabalhador.nomeCompleto else ''
    print(f"[DEBUG] relatorios - trabalhador: {trabalhador.nomeCompleto if trabalhador else None} | nome_usuario normalizado: {nome_usuario}")
    if not trabalhador:
        return template('home.tpl', nome_usuario='usuário', cpf=cpf, erro='Acesso restrito aos gerentes.')
    if nome_usuario not in nomes_gerentes:
        return template('home.tpl', nome_usuario=trabalhador.nomeCompleto, cpf=cpf, erro='Acesso restrito aos gerentes.')
    print("[DEBUG] Permissão concedida para relatórios!")
    return ctl.render('relatorios', nome_usuario=trabalhador.nomeCompleto, cpf=cpf)

@app.route('/cadastro', method='GET')
def cadastro():
    return ctl.render('cadastro')

@app.route('/lista-trabalhadores', method='GET')
@app.route('/lista_trabalhadores', method='GET')
def lista_trabalhadores():
    return ctl.render('lista_trabalhadores')



@app.route('/api/trabalhadores', method='POST')
def api_create_trabalhador():
    try:
        dados = request.json
        
    
        if not dados.get('nomeCompleto') or not dados.get('cpf') or not dados.get('email'):
            return json.dumps({'success': False, 'message': 'Dados obrigatórios faltando'})
        
        # Verificar se CPF já existe
        if ctl.trabalhador_exists(dados['cpf']):
            return json.dumps({'success': False, 'message': 'CPF já cadastrado'})
        
        trabalhador = ctl.create_trabalhador(dados)
        if trabalhador:
            return json.dumps({
                'success': True,
                'message': 'Trabalhador criado com sucesso',
                'data': trabalhador.to_dict()
            })
        else:
            return json.dumps({'success': False, 'message': 'Erro ao criar trabalhador'})
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/trabalhadores', method='GET')
def api_get_all_trabalhadores():
    try:
        trabalhadores = ctl.get_all_trabalhadores()
        return json.dumps({
            'success': True,
            'data': [t.to_dict() for t in trabalhadores]
        })
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/trabalhadores/<id:int>', method='GET')
def api_get_trabalhador(id):
    try:
        trabalhador = ctl.get_trabalhador(id)
        if trabalhador:
            return json.dumps({
                'success': True,
                'data': trabalhador.to_dict()
            })
        else:
            return json.dumps({'success': False, 'message': 'Trabalhador não encontrado'})
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})



@app.route('/api/trabalhadores/<id:int>', method='PUT')
def api_update_trabalhador(id):
    try:
        dados = request.json
        trabalhador = ctl.update_trabalhador(id, dados)
        if trabalhador:
            return json.dumps({
                'success': True,
                'message': 'Trabalhador atualizado com sucesso',
                'data': trabalhador.to_dict()
            })
        else:
            return json.dumps({'success': False, 'message': 'Trabalhador não encontrado'})
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/trabalhadores/<id:int>', method='DELETE')
def api_delete_trabalhador(id):
    try:
        sucesso = ctl.delete_trabalhador(id)
        if sucesso:
            return json.dumps({
                'success': True,
                'message': 'Trabalhador deletado com sucesso'
            })
        else:
            return json.dumps({'success': False, 'message': 'Trabalhador não encontrado'})
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/trabalhadores/search/<termo>', method='GET')
def api_search_trabalhadores(termo):
    try:
        campo = request.query.get('campo', 'nomeCompleto')
        trabalhadores = ctl.search_trabalhadores(termo, campo)
        return json.dumps({
            'success': True,
            'data': [t.to_dict() for t in trabalhadores]
        })
    except Exception as e:
        return json.dumps({'success': False, 'message': f'Erro: {str(e)}'})




if __name__ == '__main__':
    print('=== [DEBUG] Antes do run(app) ===')
    print("Rotas registradas:")
    for r in app.routes:
        print(r.rule)
    run(app, host='127.0.0.1', port=8080, debug=True)
