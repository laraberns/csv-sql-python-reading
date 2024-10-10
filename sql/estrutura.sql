-- Criar Tabela Departamentos
CREATE TABLE departamentos(
  id_departamento SERIAL PRIMARY KEY,
  nome VARCHAR(256) NOT NULL,
  andar INTEGER NOT NULL,
  sigla VARCHAR(5) NOT NULL
);

-- Criar Tabela Cargos com id_departamento
CREATE TABLE cargos(
  id_cargo SERIAL PRIMARY KEY,
  descricao VARCHAR(256) NOT NULL,
  salario_base FLOAT NOT NULL,
  nivel VARCHAR(10) CHECK (nivel IN ('estagiário', 'técnico', 'analista', 'gerente', 'diretor')) NOT NULL,
  carga_horaria_semanal INT NOT NULL,
  id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL
);

-- Criar Tabela Funcionários
CREATE TABLE funcionarios(
  id_funcionario SERIAL PRIMARY KEY,
  nome VARCHAR(256) NOT NULL,
  id_cargo INTEGER REFERENCES cargos(id_cargo) NOT NULL,
  id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL,
  salario_real FLOAT NOT NULL,
  data_admissao DATE NOT NULL
);	

-- Criar Tabela Histórico de Salários
CREATE TABLE historico_salarios(
  id_salario SERIAL PRIMARY KEY,
  id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
  mes_ano DATE NOT NULL, -- Mês e ano do salário recebido
  salario_recebido FLOAT NOT NULL
);

-- Criar Tabela Dependentes
CREATE TABLE dependentes(
  id_dependente SERIAL PRIMARY KEY,
  id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
  relacao VARCHAR(20) CHECK (relacao IN ('cônjuge', 'companheiro(a)', 'filho(a)', 'enteado(a)', 'outro')) NOT NULL, -- Correção no CHECK
  sexo VARCHAR(10) CHECK (sexo IN ('feminino', 'masculino')) NOT NULL, -- Correção no CHECK
  nome VARCHAR(256) NOT NULL,
  data_nascimento DATE NOT NULL
);
