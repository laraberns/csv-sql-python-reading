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

# 5 - Listar qual estagiário possui filho
print("Listar qual estagiário possui filho:")
consultar("""
          SELECT distinct funcionarios.nome as nome_funcionario
          FROM funcionarios
          INNER JOIN cargos ON funcionarios.id_cargo = cargos.id_cargo
          INNER JOIN dependentes ON funcionarios.id_funcionario = dependentes.id_funcionario 
          WHERE cargos.nivel = 'estagiário' and dependentes.relacao = 'filho(a)'
          """)

# 6 - Listar o funcionário que teve o salário médio mais alto
print("Listar o funcionário que teve o salário médio mais alto")
consultar("""
          SELECT round(AVG(historico_salarios.salario_recebido),2) AS media_salario, funcionarios.nome
		  FROM historico_salarios
		  INNER JOIN funcionarios ON funcionarios.id_funcionario = historico_salarios.id_funcionario 
		  group by historico_salarios.id_funcionario, funcionarios.nome
		  order by AVG(historico_salarios.salario_recebido) DESC
		  limit 1
          """)

# 7 - Listar o analista que é pai de 2 (duas) meninas.
print("Listar o analista que é pai de 2 (duas) meninas.")
consultar("""
          SELECT funcionarios.nome as nome_funcionario
          FROM funcionarios
          INNER JOIN cargos ON funcionarios.id_cargo = cargos.id_cargo
          INNER JOIN dependentes ON funcionarios.id_funcionario = dependentes.id_funcionario 
          WHERE cargos.nivel = 'analista' and dependentes.relacao = 'filho(a)' and dependentes.sexo = 'feminino'
		  group by funcionarios.nome
		  having count(funcionarios.nome) >= 2
          """)

# 8 - Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000
print("Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000.")
consultar("""
        SELECT funcionarios.nome, MAX(historico_salarios.salario_recebido) AS max_salario
        FROM historico_salarios
        INNER JOIN funcionarios ON funcionarios.id_funcionario = historico_salarios.id_funcionario 
        INNER JOIN cargos ON cargos.id_cargo = funcionarios.id_cargo 
        WHERE cargos.nivel = 'analista'
        GROUP BY funcionarios.nome
        HAVING MAX(historico_salarios.salario_recebido) BETWEEN 5000 AND 9000
        ORDER BY max_salario DESC
        LIMIT 1
          """)
