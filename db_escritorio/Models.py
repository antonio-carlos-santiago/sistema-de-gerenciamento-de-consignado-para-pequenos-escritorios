from datetime import datetime

from sqlalchemy import Integer, String, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db_escritorio import database


class Clientes(database.Model):
    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    cpf_cliente: Mapped[int] = mapped_column(Numeric, unique=True, nullable=False)
    nome_cliente: Mapped[str] = mapped_column(String, nullable=False)
    dt_nascimento_cliente: Mapped[str] = mapped_column(String, nullable=False)
    sexo_cliente: Mapped[str] = mapped_column(String, nullable=False)
    telefone_cliente: Mapped[str] = mapped_column(String, nullable=False)
    status_cliente: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    data_registro_cliente: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)


class Convenios(database.Model):
    id_convenio: Mapped[int] = mapped_column(Integer, primary_key=True)
    matricula_convenio: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    cpf_convenio: Mapped[int] = mapped_column(Numeric, nullable=False)
    nome_convenio: Mapped[str] = mapped_column(String, nullable=False)
    tipo_convenio: Mapped[str] = mapped_column(String, nullable=False)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('clientes.id_cliente'))
    clientes = database.relationship("Clientes", backref='convenios')


class Contratos(database.Model):
    id_contrato = database.Column(database.Integer, primary_key=True)
    numero_contrato = database.Column(database.Integer, nullable=False, unique=True)
    banco_contrato = database.Column(database.String, nullable=False)
    parcela_contrato = database.Column(database.Float, nullable=False)
    prazo_contrato = database.Column(database.Integer, nullable=False)
    liquido_contrato = database.Column(database.Float, nullable=False)
    bruto_contrato = database.Column(database.Float, nullable=False)
    modalidade_contrato = database.Column(database.String, nullable=False)  # Se é novo/refin
    tabela_contrato = database.Column(database.String, nullable=False)
    convenio_contrato = database.Column(database.String, nullable=False)
    matricula_contrato = database.Column(database.String, nullable=False)
    tipo_contrato = database.Column(database.String, nullable=False)
    senha_contrato = database.Column(database.String, nullable=False)
    origem_contrato = database.Column(database.String, nullable=False)
    status_contrato = database.Column(database.String, nullable=False, default="ANDAMENTO")
    data_origem_contrato = database.Column(database.DateTime, default=datetime.utcnow)
    pagamento_contrato = database.Column(database.Boolean, nullable=False, default=False)
    data_pagamento_contrato = database.Column(database.DateTime)
    promotora_contrato = database.Column(database.String, nullable=False)
    digitador_contrato = database.Column(database.String, nullable=False)
    relatorio_status = database.Column(database.Boolean, nullable=False, default=False)
    id_cliente = database.Column(database.Integer, database.ForeignKey('clientes.id_cliente'))
    clientes = database.relationship("Clientes", backref='contratos')


class Relatorio(database.Model):
    id_relatorio = database.Column(database.Integer, primary_key=True)
    numero_relatorio = database.Column(database.Integer, nullable=False, unique=True)
    banco_relatorio = database.Column(database.String, nullable=False)
    parcela_relatorio = database.Column(database.Float, nullable=False)
    prazo_relatorio = database.Column(database.Integer, nullable=False)
    liquido_relatorio = database.Column(database.Float, nullable=False)
    modalidade_relatorio = database.Column(database.String, nullable=False)  # Se é novo/refin
    tabela_relatorio = database.Column(database.String, nullable=False)
    convenio_relatorio = database.Column(database.String, nullable=False)
    origem_relatorio = database.Column(database.String, nullable=False)
    status_relatorio = database.Column(database.String, nullable=False, default="EM ABERTO")
    pagamento_relatorio = database.Column(database.Boolean, nullable=False, default=False)
    data_gerada_relatorio = database.Column(database.DateTime, default=datetime.utcnow)
    data_finalizado_relatorio = database.Column(database.DateTime)
    id_cliente = database.Column(database.Integer, database.ForeignKey("clientes.id_cliente"))
    clientes = database.relationship("Clientes", backref="relatorio")
