from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Marca(Base):
    __tablename__ = 'marcas'
    id = Column(Integer, primary_key=True)
    nombre_marca = Column(String(25), nullable=False)
    id_pais = Column(Integer,nullable=False)
    habilitado = Column(Boolean, nullable=False)
