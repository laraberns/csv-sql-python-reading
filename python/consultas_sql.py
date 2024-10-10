import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Função de consulta dinâmica
def consultar(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

# 2 - Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes
print("Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes:")
consultar("""
          SELECT funcionarios.nome as nome_funcionario, cargos.descricao as nome_cargo, departamentos.nome as nome_departamento, dependentes.nome as nome_dependente
          FROM funcionarios
          INNER JOIN cargos ON funcionarios.id_cargo = cargos.id_cargo
          INNER JOIN departamentos ON cargos.id_departamento = departamentos.id_departamento 
          INNER JOIN dependentes ON funcionarios.id_funcionario = dependentes.id_funcionario 
          """)
