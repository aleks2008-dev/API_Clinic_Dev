import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)

from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

#SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
doctors = Table(
    "doctors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("category", Integer(3)),
    Column("speciality", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("email", String(50)),
    Column("age", Integer(3)),
    Column("phone", Integer(12)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

rooms = Table(
    "rooms",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("number", Integer(4)),
)

appointments = Table(
    "appointments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

     #databases query builder
database = Database(DATABASE_URL)