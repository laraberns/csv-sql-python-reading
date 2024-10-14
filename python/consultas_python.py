import pandas as pd
from datetime import datetime

data_frame_cargos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\cargos.csv', encoding='latin-1')
data_frame_departamentos = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\departamentos.csv', encoding='latin-1')
data_frame_funcionarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\funcionarios.csv', encoding='latin-1')
data_frame_dependentes = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\dependentes.csv', encoding='latin-1')
data_frame_historico_salarios = pd.read_csv(r'C:\Users\Lara\Documents\TP-3-Bloco\csv\historico_salarios.csv', encoding='latin-1')

# 1 - Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.
def listar_crescente(data_frame, coluna):
    data_frame_ordenado = data_frame.sort_values(by=coluna)
    print(data_frame_ordenado.to_string())

# Exibindo o resultado
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

# 3 - Listar os funcionários que tiveram aumento salarial nos últimos 3 meses
funcionarios_salarios = pd.merge(
    data_frame_funcionarios, 
    data_frame_historico_salarios, 
    on='id_funcionario',  
    suffixes=('_funcionario', '_salarios') 
)

funcionarios_salarios = funcionarios_salarios.sort_values(by=['id_funcionario', 'mes_ano'])
ultimos_quatro_salarios = funcionarios_salarios.groupby('id_funcionario').tail(4)
salarios_comparacao = ultimos_quatro_salarios.groupby('id_funcionario').agg(
    primeiro_salario=('salario_recebido', 'first'),
    ultimo_salario=('salario_recebido', 'last')
).reset_index()
aumentos_salariais_df = salarios_comparacao[salarios_comparacao['ultimo_salario'] > salarios_comparacao['primeiro_salario']]
resultado_final = pd.merge(aumentos_salariais_df, data_frame_funcionarios[['id_funcionario', 'nome']], on='id_funcionario', how='left')

# Exibindo o resultado
print("Funcionários que tiveram aumento salarial nos últimos 3 meses:")
print(resultado_final[['nome']])

# 4 - Listar a média de idade dos filhos dos funcionários por departamento.
dependentes_e_funcionarios = pd.merge(
    data_frame_dependentes, 
    data_frame_funcionarios, 
    on='id_funcionario',  
    suffixes=('_dependente', '_funcionario') 
)

dependentes_funcionarios_departamentos = pd.merge(
    dependentes_e_funcionarios,
    data_frame_departamentos,
    on='id_departamento' 
)

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

dependentes_filhos = dependentes_funcionarios_departamentos.query("relacao == 'filho(a)'").copy()
dependentes_filhos.loc[:, 'data_nascimento'] = pd.to_datetime(dependentes_filhos['data_nascimento'], format='%Y-%m-%d')
dependentes_filhos.loc[:, 'idade'] = dependentes_filhos['data_nascimento'].apply(calcular_idade)
media_idade_filhos = dependentes_filhos.groupby('nome')['idade'].mean().reset_index()
media_idade_filhos.columns = ['Nome Departamento', 'Média de Idade dos Filhos']

# Exibindo o resultado
print("Média de idade dos filhos dos funcionários por departamento:")
print(media_idade_filhos.to_string())

# 9 - Listar qual departamento possui o maior número de dependentes.
dependentes_funcionarios = pd.merge(
    data_frame_dependentes, 
    data_frame_funcionarios, 
    on='id_funcionario',  
    suffixes=('_dependente', '_funcionario') 
)

resultado_final =pd.merge(
    dependentes_e_funcionarios,
    data_frame_departamentos,
    on='id_departamento' 
)

contagem_dependentes = resultado_final.groupby('nome')['nome_dependente'].count().reset_index()
contagem_dependentes.columns = ['Nome Departamento', 'Número de Dependentes']
departamento_com_mais_dependentes = contagem_dependentes.sort_values(by='Número de Dependentes', ascending=False).head(1)

# Exibindo o resultado
print("Departamento que possui o maior número de dependentes:")
print(departamento_com_mais_dependentes.to_string())

# 10 - Listar a média de salário por departamento em ordem decrescente.
funcionarios_departamento = pd.merge(
    data_frame_funcionarios, 
    data_frame_departamentos, 
    on='id_departamento',  
    suffixes=('_funcionario', '_departamento') 
)
media_departamento = funcionarios_departamento.groupby('nome_departamento')['salario_real'].mean().reset_index()
media_departamento.columns = ['Nome Departamento', 'Média de Salário']
media_departamento_ordenado = media_departamento.sort_values(by='Média de Salário', ascending=False)

# Exibindo o resultado
print("Média de salário por departamento em ordem decrescente:")
print(media_departamento_ordenado.to_string())