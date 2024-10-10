import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os valores das variáveis de ambiente
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Configuração da conexão com o banco de dados PostgreSQL
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Função de consulta dinâmica
def consultar(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        
        # Converter o resultado em um DataFrame para exibição
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

# Exemplo de uso da função com uma query dinâmica
query_exemplo = "SELECT * FROM funcionarios"
consultar(query_exemplo)
