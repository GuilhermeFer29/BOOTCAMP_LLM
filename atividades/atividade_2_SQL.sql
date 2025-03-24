-- 1. Quantos aluguéis cada cliente fez?
SELECT cliente_id, COUNT(*) AS total_alugueis
FROM alugueis
GROUP BY cliente_id;

-- 2. Quais carros foram alugados mais de 2 vezes?
SELECT carro_id, COUNT(*) AS total_alugueis
FROM alugueis
GROUP BY carro_id
HAVING COUNT(*) > 2;

-- 3. Quem são os clientes que alugaram o carro mais caro?
SELECT c.nome
FROM clientes c
JOIN alugueis a ON c.cliente_id = a.cliente_id
WHERE a.carro_id = (
    SELECT carro_id
    FROM carros
    ORDER BY valor DESC
    LIMIT 1
);

-- 4. Quais modelos de carros nunca foram alugados?
SELECT modelo
FROM carros
WHERE carro_id NOT IN (SELECT DISTINCT carro_id FROM alugueis);

-- 5. Classifique os carros como 'Econômico', 'Padrão' ou 'Premium' com base no valor.
SELECT modelo, valor,
    CASE 
        WHEN valor < 100 THEN 'Econômico'
        WHEN valor BETWEEN 100 AND 200 THEN 'Padrão'
        ELSE 'Premium'
    END AS categoria
FROM carros;

-- 6. Crie uma CTE que retorne os clientes com mais de 2 aluguéis.
WITH clientes_frequentes AS (
    SELECT cliente_id, COUNT(*) AS total_alugueis
    FROM alugueis
    GROUP BY cliente_id
    HAVING COUNT(*) > 2
)
SELECT * FROM clientes_frequentes;

-- 7. Crie uma VIEW chamada vw_resumo_alugueis com nome do cliente, modelo do carro e data do aluguel.
CREATE VIEW vw_resumo_alugueis AS
SELECT c.nome AS cliente, car.modelo AS carro, a.data_aluguel
FROM alugueis a
JOIN clientes c ON a.cliente_id = c.cliente_id
JOIN carros car ON a.carro_id = car.carro_id;

-- 8. Use a vw_resumo_alugueis para consultar todos os aluguéis feitos por 'Ana Silva'.
SELECT * FROM vw_resumo_alugueis
WHERE cliente = 'Ana Silva';

-- 9. Mostre a média de valor dos carros alugados por cliente.
SELECT c.nome AS cliente, AVG(car.valor) AS media_valor
FROM alugueis a
JOIN clientes c ON a.cliente_id = c.cliente_id
JOIN carros car ON a.carro_id = car.carro_id
GROUP BY c.nome;

-- 10. Encontre a cidade com o maior número de clientes.
SELECT cidade, COUNT(*) AS total_clientes
FROM clientes
GROUP BY cidade
ORDER BY total_clientes DESC
LIMIT 1;
