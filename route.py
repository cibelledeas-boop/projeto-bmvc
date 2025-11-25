import os
import json
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response, TEMPLATE_PATH


# Configurar o diretório de templates com caminho absoluto
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'app', 'views', 'html')
TEMPLATE_PATH.insert(0, template_dir)

app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas de arquivos estáticos:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


#-----------------------------------------------------------------------------
# Rotas de páginas (GET):

@app.route('/')
@app.route('/helper')
def action_helper(info=None):
    return ctl.render('helper')


@app.route('/pagina', methods=['GET'])
def action_pagina():
    return ctl.render('pagina')

@app.route('/home', method='GET')
def home():
    return ctl.render('home')

@app.route('/registers', method='GET')
def registers():
    return ctl.render('registers')

@app.route('/login', method='GET')
def login():
    return ctl.render('login')

@app.route('/relatorios', method='GET')
def relatorios():
    return ctl.render('relatorios')

@app.route('/cadastro', method='GET')
def cadastro():
    return ctl.render('cadastro')

@app.route('/lista-trabalhadores', method='GET')
def lista_trabalhadores():
    return ctl.render('lista_trabalhadores')


#-----------------------------------------------------------------------------
# CRUD - Trabalhador (API REST):

# CREATE - Criar novo trabalhador
@app.route('/api/trabalhadores', method='POST')
def api_create_trabalhador():
    try:
        dados = request.json
        
        # Validar dados obrigatórios
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


# READ - Listar todos os trabalhadores
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


# READ - Buscar trabalhador por ID
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


# UPDATE - Atualizar trabalhador
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


# DELETE - Deletar trabalhador
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


# SEARCH - Buscar trabalhadores
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


#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='127.0.0.1', port=8080, debug=True)
