from db_escritorio.Models import Clientes, Convenios, Contratos, Relatorio
from db_escritorio import database, app
import json
from datetime import datetime


def registrarclient(response):
    print("chegou em registrar cliente")
    buscaclciente = Clientes.query.filter_by(cpf_cliente=int(response["cpf"])).first()
    print(type(buscaclciente))
    if not buscaclciente:
        novocliente = Clientes(cpf_cliente=response["cpf"], nome_cliente=response["nome"],
                               dt_nascimento_cliente=response["dt_nascimento"], sexo_cliente=response["sexo"],
                               telefone_cliente=response["telefone"])

        database.session.add(novocliente)
        database.session.commit()
        return {"status": "cliente registrado"}
    else:
        return {"status": "cliente ja possui cadastro ativo!"}


def registrarconvenio(response):
    buscarmatricula = Convenios.query.filter_by(matricula_convenio=response["matricula"]).first()
    if not buscarmatricula:
        dadoscliente = Clientes.query.filter_by(cpf_cliente=response["cpf"]).first()
        referencia = Clientes.query.get(dadoscliente.id_cliente)

        novamatricula = Convenios(matricula_convenio=response["matricula"], cpf_convenio=response["cpf"],
                                  nome_convenio=response["convenio"], tipo_convenio=response["tiposerv"],
                                  clientes=referencia)
        database.session.add(novamatricula)
        database.session.commit()
        return {"status": "matricula registrada"}
    else:
        return {"status": "cliente ja possui matricula ativa!"}


def registrarcontrato(response):
    buscarcontrato = Contratos.query.filter_by(numero_contrato=response["contrato"]).first()
    if not buscarcontrato:
        dadoscliente = Clientes.query.filter_by(cpf_cliente=response["cpf"]).first()
        referencia = Clientes.query.get(dadoscliente.id_cliente)

        novocontrato = Contratos(numero_contrato=response["contrato"], banco_contrato=response["banco"],
                                 parcela_contrato=response["parcela"], prazo_contrato=response["prazo"],
                                 liquido_contrato=response["liquido"], bruto_contrato=response["bruto"],
                                 modalidade_contrato=response["modalidade"], tabela_contrato=response["tabela"],
                                 convenio_contrato=response["convenio"], matricula_contrato=response["matricula"],
                                 tipo_contrato=response["tiposerv"], senha_contrato=response["senha"],
                                 origem_contrato=response["origem"], promotora_contrato=response["promotora"],
                                 digitador_contrato=response["digitador"], clientes=referencia)
        database.session.add(novocontrato)
        database.session.commit()
        return {"status": "contrato registrada"}
    else:
        return {"status": "cliente ja possui contrato cadastrado!"}


def vertodosandamentos():
    listacontrato = []
    contratos = Contratos.query.all()
    for contrato in contratos:
        if not contrato.status_contrato in ["REPROVADO", "PAGO"]:
            listacontrato.append({"id_contrato": contrato.id_contrato,
                                  "numero_contrato": contrato.numero_contrato,
                                  "banco_contrato": contrato.banco_contrato,
                                  "parcela_contrato": contrato.parcela_contrato,
                                  "prazo_contrato": contrato.prazo_contrato,
                                  "liquido_contrato": contrato.liquido_contrato,
                                  "bruto_contrato": contrato.bruto_contrato,
                                  "modalidade_contrato": contrato.modalidade_contrato,
                                  "tabela_contrato": contrato.tabela_contrato,
                                  "convenio_contrato": contrato.convenio_contrato,
                                  "matricula_contrato": contrato.matricula_contrato,
                                  "tipo_contrato": contrato.tipo_contrato,
                                  "origem_contrato": contrato.origem_contrato,
                                  "status_contrato": contrato.status_contrato,
                                  "data_origem_contrato": contrato.data_origem_contrato,
                                  "data_pagamento_contrato": contrato.data_pagamento_contrato,
                                  "promotora_contrato": contrato.promotora_contrato,
                                  "relatorio_status": contrato.relatorio_status,
                                  "digitador_contrato": contrato.digitador_contrato,
                                  "id_cliente": contrato.clientes.id_cliente,
                                  "cpf_cliente": contrato.clientes.cpf_cliente,
                                  "nome_cliente": contrato.clientes.nome_cliente,
                                  "dt_nascimento_cliente": contrato.clientes.dt_nascimento_cliente,
                                  "sexo_cliente": contrato.clientes.sexo_cliente,
                                  "telefone_cliente": contrato.clientes.telefone_cliente,
                                  "status_cliente": contrato.clientes.status_cliente,
                                  "data_registro_cliente": contrato.clientes.data_registro_cliente})
    return listacontrato


def novostatuscontrato(response):
    contrato = Contratos.query.filter_by(id_contrato=response["id_contrato"]).first()
    if contrato:
        contrato.status_contrato = response["status_contrato"]
        contrato.data_pagamento_contrato = datetime.utcnow()
        database.session.commit()
        if response["status_contrato"] == "PAGO":
            referencia = Clientes.query.get(contrato.clientes.id_cliente)
            novorelatorio = Relatorio(numero_relatorio=contrato.numero_contrato,
                                      banco_relatorio=contrato.banco_contrato,
                                      parcela_relatorio=contrato.parcela_contrato,
                                      prazo_relatorio=contrato.prazo_contrato,
                                      liquido_relatorio=contrato.liquido_contrato,
                                      modalidade_relatorio=contrato.modalidade_contrato,
                                      tabela_relatorio=contrato.tabela_contrato,
                                      convenio_relatorio=contrato.convenio_contrato,
                                      origem_relatorio=contrato.origem_contrato,
                                      clientes=referencia)
            database.session.add(novorelatorio)
            database.session.commit()


        return {"status": "status atualizado com sucesso"}
    else:
        return {"status": "contrato não encontrado"}


def relatoriodisponivel():
    relatorioaberto = Relatorio.query.all()
    relatorios = [{"id_relatorio": relatorio.id_relatorio, "numero_contrato": relatorio.numero_relatorio,
                   "banco_contrato": relatorio.banco_relatorio, "parcela_contrato": relatorio.parcela_relatorio,
                   "prazo_contrato": relatorio.prazo_relatorio, "liquido_contrato": relatorio.liquido_relatorio,
                   "modalidade_contrato": relatorio.modalidade_relatorio, "tabela_contrato": relatorio.tabela_relatorio,
                   "convenio_contrato": relatorio.convenio_relatorio, "origem_contrato": relatorio.origem_relatorio,
                   "status_contrato": relatorio.status_relatorio, "pagamento_relatorio": relatorio.pagamento_relatorio,
                   "data_relatorio": relatorio.data_gerada_relatorio, "cpf_cliente": relatorio.clientes.cpf_cliente,
                   "nome_cliente": relatorio.clientes.nome_cliente}
                  for relatorio in relatorioaberto
                  if relatorio.status_relatorio == "EM ABERTO"]
    return relatorios


def finalizarrelatoriogeral():
    clientes = relatoriodisponivel()


def getdados(response):
    cliente = Clientes.query.filter_by(cpf_cliente=response).first()
    if cliente:
        conv = Convenios.query.filter_by(cpf_convenio=cliente.cpf_cliente).all()
        return {"nome_cliente": cliente.nome_cliente, "cpf_cliente": cliente.cpf_cliente,
                "dt_nascimento_cliente": cliente.dt_nascimento_cliente, "sexo_cliente": cliente.sexo_cliente,
                "convenios": [{"convenio": convenio.nome_convenio, "matricula": convenio.matricula_convenio,
                               "tipo": convenio.tipo_convenio} for convenio in conv],
                "status": cliente.status_cliente}
    else:
        return {"nome_cliente": "INDEFINIDO", "cpf_cliente": "INDEFINIDO",
                "dt_nascimento_cliente": "INDEFINIDO", "sexo_cliente": "INDEFINIDO",
                "convenios": [{"convenio": "INDEFINIDO", "matricula": "INDEFINIDO", "tipo": "INDEFINIDO"}],
                "status": "INDEFINIDO"}


def statuscliente(response):
    findclient = Clientes.query.filter_by(cpf_cliente=response["cpf_cliente"]).first()
    if findclient:
        findclient.status_cliente = response["status"]
        database.session.commit()
        return {"status": "sucesso"}
    return {"status": "cliente inexistente"}
