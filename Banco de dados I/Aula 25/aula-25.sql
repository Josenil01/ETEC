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
    salario NUMERIC(10,2), data_saida TIMESTAMP DEFAULT now() 
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
('Ana Souza', 'Analista de Sistemas', 5500.00, 'ana.souza@empresa.com', 1, 1),
('Carlos Lima', 'Suporte Técnico', 3200.00, 'carlos.lima@empresa.com', 1, 1),
('Mariana Costa', 'Gerente de RH', 7500.00, 'mariana.costa@empresa.com', 1, 2),
('João Silva', 'Assistente de Departamento Pessoal', 2800.00, 'joao.silva@empresa.com', 1, 2),
('Roberto Alves', 'Analista Financeiro', 4800.00, 'roberto.alves@empresa.com', 1, 3),
('Amanda Rocha', 'Contadora', 6200.00, 'amanda.rocha@empresa.com', 1, 3),
('Bruno Mendes', 'Analista de Marketing', 4500.00, 'bruno.mendes@empresa.com', 1, 4),
('Camila Oliveira', 'Designer Gráfico', 3800.00, 'camila.oliveira@empresa.com', 1, 4),
('Diego Santos', 'Gerente de Projetos', 9000.00, 'diego.santos@empresa.com', 1, 5),
('Fernanda Dias', 'Coordenadora de Projetos', 6800.00, 'fernanda.dias@empresa.com', 1, 5),
('Lucas Martins', 'Desenvolvedor Full Stack', 6000.00, 'lucas.martins@empresa.com', 1, 1),
('Sol', 'Estagiária de RH', 1500.00, NULL, 1, 2);
