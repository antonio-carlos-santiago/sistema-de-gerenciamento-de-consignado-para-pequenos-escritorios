import json
from db_escritorio import app, database
from flask import request
from db_escritorio.Funcoes import registrarclient, registrarconvenio, registrarcontrato, vertodosandamentos, \
    novostatuscontrato, relatoriodisponivel, getdados, statuscliente


@app.route("/importar", methods=["post", "get"])
def importclient():
    response = request.get_json()
    status_cliente = registrarclient(response)
    status_convenio = registrarconvenio(response)
    status_contrato = registrarcontrato(response)
    return {"status cliente": status_cliente, "status convenio": status_convenio, "status contrato": status_contrato}


@app.route("/banco", methods=["get"])
def criarbanco():
    with app.app_context():
        database.create_all()
    return {"status": "work"}


@app.route("/andamento", methods=["get"])
def andamentos():
    contratos = vertodosandamentos()
    return contratos


@app.route("/statuscontrato", methods=["post"])
def statuscontrato():
    response = request.get_json()
    status = novostatuscontrato(response)
    return status


@app.route("/visualizarrelatorio", methods=["GET"])
def verificarrelatorio():
    status = relatoriodisponivel()
    return status


@app.route("/dadoscliente", methods=["POST"])
def dadoscliente():
    response = request.get_json()
    status = getdados(response)
    return status


@app.route("/statuscliente", methods=['post'])
def alterarstatus():
    response = request.get_json()
    status = statuscliente(response)
    return status



