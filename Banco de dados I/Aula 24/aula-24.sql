SELECT * FROM departamento
SELECT nome, cargo FROM funcionario
SELECT DISTINCT cargo FROM funcionario
SELECT nome, salario * 12 AS salario_anual FROM funcionario
SELECT nome COALESCE
(cargo, 'Sem Cargo') AS cargo_seguro, 
CASE 
   WHEN salario > 4000 then
     'Alto'
   ELSE 
     'Normal'
END AS classificacao FROM funcionario