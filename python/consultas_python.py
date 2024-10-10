import pandas as pd

data_frame_cargos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\cargos.csv', encoding='latin-1')
data_frame_departamentos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\departamentos.csv', encoding='latin-1')
data_frame_funcionarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\funcionarios.csv', encoding='latin-1')
data_frame_dependentes = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\dependentes.csv', encoding='latin-1')
data_frame_historico_salarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\historico_salarios.csv', encoding='latin-1')

def listar_crescente(data_frame, coluna):
    data_frame_ordenado = data_frame.sort_values(by=coluna)
    print(data_frame_ordenado.to_string())

# 1 - Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.
print("Tabela Funcionários em ordem crescente - Nome:")
listar_crescente(data_frame_funcionarios, "nome")
print("Tabela Cargos em ordem crescente - Descricao:")
listar_crescente(data_frame_cargos, "descricao")
print("Tabela Departamentos em ordem crescente - Nome:")
listar_crescente(data_frame_departamentos, "nome")
print("Tabela Histórico de Salários em ordem crescente - salario_recebido:")
listar_crescente(data_frame_historico_salarios, "salario_recebido")
print("Tabela Dependentes em ordem crescente - nome:")
listar_crescente(data_frame_dependentes, "nome")