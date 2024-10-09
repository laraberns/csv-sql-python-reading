import pandas as pd

# Importando CSVs
data_frame_cargos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\cargos.csv', encoding='latin-1')
data_frame_dependentes = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\dependentes.csv', encoding='latin-1')
data_frame_departamentos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\departamentos.csv', encoding='latin-1')
data_frame_funcionarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\funcionarios.csv', encoding='latin-1')
data_frame_historico_salarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\historico_salarios.csv', encoding='latin-1')

# Lendo Data Frames
print(data_frame_cargos)
print("\n")
print(data_frame_dependentes)
print("\n")
print(data_frame_departamentos)
print("\n")
print(data_frame_funcionarios)
print("\n")
print(data_frame_historico_salarios)
