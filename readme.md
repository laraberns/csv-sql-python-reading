
# Projeto: Teste de Performance (TP3) - Modelagem de Banco de Dados e Manipulação de Dados em Python

## Introdução

Neste projeto você terá a oportunidade de aplicar seus conhecimentos sobre modelagem de banco de dados SQL e manipulação de dados em Python. O foco deste projeto é desenvolver habilidades em:

- Modelagem eficiente de bancos de dados em SQL.
- Utilização de diretivas para agregação, filtragem e garantia da integridade dos dados.
- Manipulação avançada de conjuntos em Python, criando estruturas de dados como listas e dicionários.

## Descrição do Problema

Você deverá criar as seguintes tabelas, tendo como referência as tabelas criadas no TP2:

1. **Funcionários:** Informações dos funcionários, com pelo menos 10 registros.
2. **Cargos:** Informações dos cargos, com pelo menos 5 registros.
3. **Departamentos:** Informações dos departamentos, com pelo menos 5 registros.
4. **Histórico de Salários:** Guarda mês a mês os valores recebidos pelos funcionários, com pelo menos os últimos 6 meses de salários de cada funcionário.
5. **Dependentes:** Armazena dados dos dependentes do funcionário, com pelo menos 2 dependentes por funcionário.

### Estrutura das Tabelas

A estrutura das tabelas poderá ser ajustada conforme a necessidade das consultas solicitadas neste TP. Certifique-se de criar todos os campos necessários, bem como as chaves primárias e estrangeiras.

## Importação de Dados

Os dados deverão ser lidos a partir de arquivos .CSV de sua autoria (criados dentro ou fora do Python), e uma estrutura SQL equivalente deverá ser criada, utilizando Python, para inserir os dados nas tabelas do Banco de Dados SQL.

## Consultas

Dentre as 10 (dez) consultas solicitadas a seguir, você deverá escolher 5 (cinco) consultas para serem feitas utilizando comandos SQL dentro do Python, e outras 5 (cinco) somente utilizando estrutura de comandos Python (sem SQL):

1. Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.
2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.
3. Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.
4. Listar a média de idade dos filhos dos funcionários por departamento.
5. Listar qual estagiário possui filho.
6. Listar o funcionário que teve o salário médio mais alto.
7. Listar o analista que é pai de 2 (duas) meninas.
8. Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000.
9. Listar qual departamento possui o maior número de dependentes.
10. Listar a média de salário por departamento em ordem decrescente.

## Resolução

Para a resolução deste projeto, foram realizadas as seguintes etapas:

1. **Geração dos Arquivos CSV**: Criei um script SQL para gerar os arquivos CSV necessários para a importação de dados. O script pode ser encontrado na pasta `sql/gerar_csv.sql`.

2. **Importação de Dados para o PostgreSQL**: Utilizando as bibliotecas Pandas e SQLAlchemy, criei um arquivo Python responsável por importar os arquivos CSV para dentro do banco de dados PostgreSQL. Este arquivo cria as tabelas correspondentes e insere os dados lidos dos arquivos CSV.

3. **Consultas**: Desenvolvi arquivos de consultas que utilizam tanto comandos SQL quanto manipulações em Python, permitindo uma análise mais abrangente dos dados importados.

Essas etapas garantem que o banco de dados esteja bem estruturado e que os dados possam ser manipulados e analisados de forma eficiente.
