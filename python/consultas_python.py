import pandas as pd

data_frame_cargos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\cargos.csv', encoding='latin-1')
data_frame_departamentos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\departamentos.csv', encoding='latin-1')
data_frame_funcionarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\funcionarios.csv', encoding='latin-1')
data_frame_dependentes = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\dependentes.csv', encoding='latin-1')
data_frame_historico_salarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\historico_salarios.csv', encoding='latin-1')

# Função exemplo de consulta usando query
def consultar_salarios():
    cargos_filtrados = data_frame_cargos.query('8000 <= salario_base <= 50000')
    print("Cargos com salário base entre 8.000 e 50.000:")
    print(cargos_filtrados.to_string())

# Executar a consulta
consultar_salarios()