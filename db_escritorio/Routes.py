from flask import request
from db_escritorio import database

from db_escritorio import app
from db_escritorio.Funcoes import registrarclient, registrarconvenio, registrarcontrato, vertodosandamentos, \
    novostatuscontrato, relatoriodisponivel, getdados, statuscliente


@app.route("/teste", methods=["GET"])
def teste():
    return {"status": "work"}


@app.route("/importar", methods=["POST"])
def importclient():
    response = request.get_json()
    status_cliente = registrarclient(response)
    status_convenio = registrarconvenio(response)
    status_contrato = registrarcontrato(response)
    return {"status cliente": status_cliente, "status convenio": status_convenio, "status contrato": status_contrato}


@app.route("/andamento", methods=["GET"])
def andamentos():
    contratos = vertodosandamentos()
    return contratos


@app.route("/statuscontrato", methods=["PATCH"])
def statuscontrato():
    response = request.get_json()
    status = novostatuscontrato(response)
    return status


@app.route("/visualizarrelatorio", methods=["GET"])
def verificarrelatorio():
    status = relatoriodisponivel()
    return status


@app.route("/dadoscliente/<cpf>", methods=["GET"])
def dadoscliente(cpf):
    status = getdados(int(cpf))
    return status


@app.route("/statuscliente", methods=['PATCH'])
def alterarstatus():
    response = request.get_json()
    status = statuscliente(response)
    return status
