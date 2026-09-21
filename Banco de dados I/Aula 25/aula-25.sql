CREATE TABLE IF NOT EXISTS departamento ( 
    id_depto SERIAL PRIMARY KEY, 
    nome VARCHAR(50) NOT NULL UNIQUE 
    ); 

CREATE TABLE IF NOT EXISTS funcionario ( 
    id_func SERIAL PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL, 
    cargo VARCHAR(60), 
    salario NUMERIC(10,2), 
    email VARCHAR(100) UNIQUE, 
    ativo BOOLEAN DEFAULT TRUE, 
    id_depto INT REFERENCES departamento(id_depto) ON DELETE RESTRICT 
    ); 
    
    -- Tabela para arquivar funcionários demitidos (Auditoria) 
    
CREATE TABLE IF NOT EXISTS funcionario_arquivo (  
    id_func INT, 
    nome VARCHAR(100), 
    cargo VARCHAR(60), 
    salario NUMERIC(10,2), 
    data_saida TIMESTAMP DEFAULT now() 
    );

-- departamentos à sua escolha (ex: 'TI', 'RH', 'Financeiro', 'Marketing', 'Projetos').

INSERT INTO departamento(nome) VALUES
('TI'), 
('RH'),
('Financeiro'),
('Marketing'),
('Projetos');


-- Insira 12 funcionários, distribuindo-os pelos departamentos (ids de 1 a 5). A funcionária 'Sol' (ID 12) ainda não tem e-mail configurado, portanto o valor dela deve ser explicitamente NULL. nome,  cargo , salario,  email , ativo, 

INSERT INTO funcionario(nome, cargo, salario, email, ativo, id_depto)
VALUES
('Ana Souza', 'Analista de Sistemas', 5500.00, 'ana.souza@empresa.com', TRUE, 1),
('Carlos Lima', 'Suporte Técnico', 3200.00, 'carlos.lima@empresa.com', TRUE, 1),
('Mariana Costa', 'Gerente de RH', 7500.00, 'mariana.costa@empresa.com', TRUE, 2),
('João Silva', 'Assistente de Departamento Pessoal', 2800.00, 'joao.silva@empresa.com', TRUE, 2),
('Roberto Alves', 'Analista Financeiro', 4800.00, 'roberto.alves@empresa.com', TRUE, 3),
('Amanda Rocha', 'Contadora', 6200.00, 'amanda.rocha@empresa.com', TRUE, 3),
('Bruno Mendes', 'Analista de Marketing', 4500.00, 'bruno.mendes@empresa.com', TRUE, 4),
('Camila Oliveira', 'Designer Gráfico', 3800.00, 'camila.oliveira@empresa.com', TRUE, 4),
('Diego Santos', 'Gerente de Projetos', 9000.00, 'diego.santos@empresa.com', TRUE, 5),
('Fernanda Dias', 'Coordenadora de Projetos', 6800.00, 'fernanda.dias@empresa.com', TRUE, 5),
('Lucas Martins', 'Desenvolvedor Full Stack', 6000.00, 'lucas.martins@empresa.com', TRUE, 1),
('Sol', 'Estagiária de RH', 1500.00, NULL, TRUE, 2);


SELECT nome FROM funcionario WHERE id_func = 1
--- Ana Souza

UPDATE  funcionario SET nome = 'Ana Sofia Silva' WHERE id_func = 1;




--- Etapa 2


SELECT cargo, salario FROM funcionario WHERE id_func = 2;

UPDATE funcionario SET cargo = 'Dev Sênior', salario = salario * 1.15 WHERE id_func = 2;

SELECT salario FROM funcionario WHERE id_depto = 1;

UPDATE funcionario SET salario = salario * 1.08 WHERE id_depto = 1;

--- etapa 3

-- O funcionário id_func = 11 estava em período de experiência e foi desligado.
-- Apaga definitivamente de "funcionario" e insere o registro em "funcionario_arquivo"
-- numa única query, usando CTE (WITH ... AS) + RETURNING.

WITH funcionario_demitido AS(
    DELETE FROM funcionario
    WHERE id_func = 11
    RETURNING id_func, nome, cargo, salario
)
INSERT INTO funcionario_arquivo (id_func,nome, cargo, salario)
SELECT id_func,nome, cargo ,salario 
FROM funcionario_demitido;

--- apagar da tabela funcionario e salvar automatomaticamente em
--- funcionario_arquivo

--- Etapa 4

-- O departamento 5 precisa ser removido, mas a FK funcionario.id_depto
-- está com ON DELETE RESTRICT: não dá pra apagar um departamento que
-- ainda tem funcionário vinculado.

-- Passo 1: transferir todos os funcionários do departamento 5 para o TI (id_depto = 1)
UPDATE funcionario
SET id_depto = 1
WHERE id_depto = 5;

-- Passo 2: com o departamento 5 vazio, agora o DELETE não esbarra mais no RESTRICT
DELETE FROM departamento
WHERE id_depto = 5;

