-- ═══════════════════════════════════════════════════════════════════════════════
-- AULA 27: FUNÇÕES AGREGADAS
-- Arquivo: aula-27-exemplo-agregados.sql
-- 
-- Copie e execute os scripts abaixo no SQL Editor do Neon Tech
-- ═══════════════════════════════════════════════════════════════════════════════


-- ───────────────────────────────────────────────────────────────────────────────
-- PREPARAÇÃO INICIAL (Execute isto primeiro se não tem dados!)
-- ───────────────────────────────────────────────────────────────────────────────

-- Criar tabela de exemplo (se ainda não existe)
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2),
    departamento_id INTEGER REFERENCES departamentos(id)
);

-- Limpar dados antigos (para reutilizar)
TRUNCATE TABLE funcionarios;
TRUNCATE TABLE departamentos CASCADE;

-- Inserir departamentos de exemplo
INSERT INTO departamentos (nome) VALUES
    ('TI'),
    ('RH'),
    ('Vendas'),
    ('Financeiro');

-- Inserir funcionários de exemplo
INSERT INTO funcionarios (nome, salario, departamento_id) VALUES
    ('João Silva', 3500.00, 1),
    ('Maria Santos', 4200.00, 1),
    ('Pedro Costa', 3800.00, 1),
    ('Ana Ferreira', 4500.00, 2),
    ('Carlos Mendes', 3200.00, 2),
    ('Diana Oliveira', 5000.00, 3),
    ('Erica Sousa', 4800.00, 3),
    ('Felipe Gomes', 3600.00, 4),
    ('Gabriela Lima', 4100.00, 4),
    ('Henrique Alves', 3900.00, 1);



-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 1: COUNT() - Contagem Total
-- ═══════════════════════════════════════════════════════════════════════════════

-- 📊 Contar quantos funcionários temos no total
SELECT
    COUNT(*) AS "Total Funcionários"
FROM funcionarios;

-- Resultado esperado: 10


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 2: SUM() - Soma da Folha de Pagamento
-- ═══════════════════════════════════════════════════════════════════════════════

-- 💰 Qual é a soma de todos os salários?
SELECT
    SUM(salario) AS "Folha Total",
    -- Dica: SUM() ignora NULL automaticamente
    COUNT(*) AS "Total Funcionários"
FROM funcionarios;

-- Resultado esperado: 
-- Folha Total: 40700.00
-- Total Funcionários: 10


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 3: AVG() - Média de Salários
-- ═══════════════════════════════════════════════════════════════════════════════

-- 📈 Qual é o salário médio?
SELECT
    AVG(salario) AS "Salário Médio"
FROM funcionarios;

-- Resultado esperado: 4070.00


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 4: MIN() e MAX() - Extremos
-- ═══════════════════════════════════════════════════════════════════════════════

-- 🔍 Qual é o menor e o maior salário?
SELECT
    MIN(salario) AS "Salário Mínimo",
    MAX(salario) AS "Salário Máximo"
FROM funcionarios;

-- Resultado esperado:
-- Salário Mínimo: 3200.00
-- Salário Máximo: 5000.00


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 5: Combinação - Relatório Completo
-- ═══════════════════════════════════════════════════════════════════════════════

-- 📋 Crie um relatório executivo com todas as estatísticas
SELECT
    COUNT(*) AS "Total de Colaboradores",
    SUM(salario) AS "Folha de Pagamento",
    AVG(salario) AS "Salário Médio",
    MIN(salario) AS "Menor Salário",
    MAX(salario) AS "Maior Salário"
FROM funcionarios;

-- Resultado esperado numa única linha:
-- Total Colaboradores | Folha | Média  | Menor  | Maior
--        10           | 40700 | 4070   | 3200   | 5000


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 6: GROUP BY - Análise por Departamento
-- ═══════════════════════════════════════════════════════════════════════════════

-- 🏢 Estatísticas agrupadas por departamento
SELECT
    d.nome AS "Departamento",
    COUNT(f.id) AS "Quantidade de Funcionários",
    SUM(f.salario) AS "Folha do Departamento",
    AVG(f.salario) AS "Salário Médio",
    MIN(f.salario) AS "Menor Salário",
    MAX(f.salario) AS "Maior Salário"
FROM funcionarios f
INNER JOIN departamentos d ON f.departamento_id = d.id
GROUP BY d.id, d.nome
ORDER BY SUM(f.salario) DESC;

-- Resultado esperado: Uma linha por departamento com as estatísticas


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 7: HAVING - Filtrar Grupos
-- ═══════════════════════════════════════════════════════════════════════════════

-- 🎯 Apenas departamentos com salário médio acima de 3800
SELECT
    d.nome AS "Departamento",
    COUNT(f.id) AS "Quantidade",
    AVG(f.salario) AS "Salário Médio"
FROM funcionarios f
INNER JOIN departamentos d ON f.departamento_id = d.id
GROUP BY d.id, d.nome
HAVING AVG(f.salario) > 3800
ORDER BY AVG(f.salario) DESC;

-- Resultado esperado: Apenas departamentos com média > 3800


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 8: DISTINCT com COUNT - Contagem de Valores Únicos
-- ═══════════════════════════════════════════════════════════════════════════════

-- 🏢 Quantos departamentos diferentes temos?
SELECT
    COUNT(DISTINCT departamento_id) AS "Total de Departamentos"
FROM funcionarios;

-- Resultado esperado: 4


-- ═══════════════════════════════════════════════════════════════════════════════
-- SCRIPT 9: DESAFIO - Análise Comparativa
-- ═══════════════════════════════════════════════════════════════════════════════

-- 🌟 Compare: Qual departamento tem a folha de pagamento mais cara?
-- E qual è o departamento com o maior salário individual?
SELECT
    d.nome AS "Departamento",
    COUNT(f.id) AS "Funcionários",
    SUM(f.salario) AS "Folha Total",
    AVG(f.salario) AS "Média",
    MAX(f.salario) - MIN(f.salario) AS "Diferença Sala-Min/Max"
FROM funcionarios f
INNER JOIN departamentos d ON f.departamento_id = d.id
GROUP BY d.id, d.nome
ORDER BY SUM(f.salario) DESC;


-- ═══════════════════════════════════════════════════════════════════════════════
-- DICAS E NOTAS IMPORTANTES
-- ═══════════════════════════════════════════════════════════════════════════════

/*
✅ LEMBRE-SE:
  - COUNT(*) conta TODAS as linhas, incluindo NULLs
  - COUNT(coluna) conta apenas linhas não-NULL
  - SUM(), AVG(), MIN(), MAX() ignoram NULLs
  
⚠️ CUIDADO:
  - Quando usar GROUP BY, todas colunas não-agregadas DEVEM estar em GROUP BY
  - HAVING filtra GRUPOS (depois da agregação)
  - WHERE filtra LINHAS (antes da agregação)

🧪 PRÓXIMA AULA:
  - Aula 28: GROUP BY avançado com HAVING
  - Aula 29: INNER JOIN - Cruzar múltiplas tabelas
  - Aula 30: LEFT JOIN - Dados sem correspondência
*/
