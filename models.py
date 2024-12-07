

from sqlalchemy.orm import declarative_base  # Importa a função do lugar certo
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# ... (resto do código)

# Configuração do banco de dados (SQLite por enquanto)
DATABASE_URL = "sqlite:///./orelha_seca.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    unidade_medida = Column(String)
    preco_unitario = Column(Float)
    tipo = Column(String)
    descricao = Column(String)

class Parede(Base):
    __tablename__ = "paredes"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    descricao = Column(String)

class Porta(Base):
    __tablename__ = "portas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    altura = Column(Float)
    largura = Column(Float)
    parede_id = Column(Integer, ForeignKey("paredes.id"))

    parede = relationship("Parede", back_populates="portas")

class Janela(Base):
    __tablename__ = "janelas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    altura = Column(Float)
    largura = Column(Float)
    parede_id = Column(Integer, ForeignKey("paredes.id"))

    parede = relationship("Parede", back_populates="janelas")

Parede.portas = relationship("Porta", back_populates="parede")
Parede.janelas = relationship("Janela", back_populates="parede")

Base.metadata.create_all(bind=engine)



# Configuração do banco de dados (SQLite por enquanto)
DATABASE_URL = "sqlite:///./orelha_seca.db"  # Banco de dados SQLite no arquivo orelha_seca.db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    unidade_medida = Column(String)  # Unidade de medida (ex: "un", "m", "kg")
    preco_unitario = Column(Float)
    tipo = Column(String)  # Tipo de material (ex: "placa", "perfil", "fixacao")
    descricao = Column(String)  # Descrição (opcional)

Base.metadata.create_all(bind=engine)


# ... (código anterior)

# Cria uma sessão com o banco de dados
db = SessionLocal()

# Cria alguns materiais e adiciona no banco de dados
#material1 = Material(nome="Placa Drywall Standard 12,5mm", unidade_medida="un", preco_unitario=50.00, tipo="placa")
#material2 = Material(nome="Perfil Montante 40mm", unidade_medida="un", preco_unitario=15.00, tipo="perfil")
#material3 = Material(nome="Parafuso Drywall 35mm", unidade_medida="un", preco_unitario=0.50, tipo="fixacao")

#db.add_all([material1, material2, material3])
#db.commit()

# Fecha a sessão com o banco de dados
db.close()

# ... (código anterior)
