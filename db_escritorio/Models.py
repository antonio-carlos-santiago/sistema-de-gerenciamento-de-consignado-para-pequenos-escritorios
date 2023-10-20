from datetime import datetime

from sqlalchemy import Integer, String, Boolean, Numeric, DateTime, ForeignKey, Float
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
    id_contrato: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_contrato: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    banco_contrato: Mapped[str] = mapped_column(String, nullable=False)
    parcela_contrato: Mapped[float] = mapped_column(Float, nullable=False)
    prazo_contrato: Mapped[int] = mapped_column(Integer, nullable=False)
    liquido_contrato: Mapped[float] = mapped_column(Float, nullable=False)
    bruto_contrato: Mapped[float] = mapped_column(Float, nullable=False)
    modalidade_contrato: Mapped[str] = mapped_column(String, nullable=False)  # Se é novo/refin
    tabela_contrato: Mapped[str] = mapped_column(String, nullable=False)
    convenio_contrato: Mapped[str] = mapped_column(String, nullable=False)
    matricula_contrato: Mapped[str] = mapped_column(String, nullable=False)
    tipo_contrato: Mapped[str] = mapped_column(String, nullable=False)
    senha_contrato: Mapped[str] = mapped_column(String, nullable=False)
    origem_contrato: Mapped[str] = mapped_column(String, nullable=False)
    status_contrato: Mapped[str] = mapped_column(String, nullable=False, default="ANDAMENTO")
    data_origem_contrato: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    pagamento_contrato: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    data_pagamento_contrato: Mapped[int] = mapped_column(DateTime, nullable=True)
    promotora_contrato: Mapped[str] = mapped_column(String, nullable=False)
    digitador_contrato: Mapped[str] = mapped_column(String, nullable=False)
    relatorio_status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('clientes.id_cliente'))
    clientes = database.relationship("Clientes", backref='contratos')


class Relatorio(database.Model):
    id_relatorio: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_relatorio: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    banco_relatorio: Mapped[str] = mapped_column(String, nullable=False)
    parcela_relatorio: Mapped[float] = mapped_column(Float, nullable=False)
    prazo_relatorio: Mapped[int] = mapped_column(Integer, nullable=False)
    liquido_relatorio: Mapped[float] = mapped_column(Float, nullable=False)
    modalidade_relatorio: Mapped[str] = mapped_column(String, nullable=False)  # Se é novo/refin
    tabela_relatorio: Mapped[str] = mapped_column(String, nullable=False)
    convenio_relatorio: Mapped[str] = mapped_column(String, nullable=False)
    origem_relatorio: Mapped[str] = mapped_column(String, nullable=False)
    status_relatorio: Mapped[str] = mapped_column(String, nullable=False, default="EM ABERTO")
    pagamento_relatorio: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    data_gerada_relatorio: Mapped[str] = mapped_column(database.DateTime, default=datetime.utcnow)
    data_finalizado_relatorio: Mapped[str] = mapped_column(database.DateTime, nullable=True)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey("clientes.id_cliente"))
    clientes = database.relationship("Clientes", backref="relatorio")
