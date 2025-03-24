# locadora_queries.py
from google.cloud import bigquery
import pandas as pd

# Configuração do cliente BigQuery
client = bigquery.Client(project='guilherme-454214')  # Altere para seu projeto

# Dicionário com todas as queries corrigidas
queries = {
    # Questão 1
    "Q1": """
    SELECT * FROM `guilherme-454214.locadora.cliente`
    """,
    
    # Questão 2
    "Q2": """
    SELECT * FROM `guilherme-454214.locadora.cliente`
    WHERE cidade = 'São Paulo'
    """,
    
    # Questão 8
    "Q8": """
    SELECT ca.*, ma.marca 
    FROM `guilherme-454214.locadora.carro` ca
    JOIN `guilherme-454214.locadora.marca` ma 
      ON ca.codmarca = ma.codmarca
    WHERE ma.marca IN ('Ford', 'Fiat')
    """,
    
    # Questão 19
    "Q19": """
    SELECT cli.nome, ca.modelo  
    FROM `guilherme-454214.locadora.cliente` cli 
    LEFT JOIN `guilherme-454214.locadora.aluguel` a 
      ON cli.codcliente = a.codcliente 
    LEFT JOIN `guilherme-454214.locadora.carro` ca 
      ON a.codcarro = ca.codcarro 
    UNION ALL
    SELECT cli.nome, ca.modelo  
    FROM `guilherme-454214.locadora.carro` ca 
    LEFT JOIN `guilherme-454214.locadora.aluguel` a 
      ON ca.codcarro = a.codcarro 
    LEFT JOIN `guilherme-454214.locadora.cliente` cli 
      ON a.codcliente = cli.codcliente
    """,
    
    # Questão 23
    "Q23": """
    SELECT cli.nome, COUNT(a.codaluguel) AS total_alugueis  
    FROM `guilherme-454214.locadora.cliente` cli 
    LEFT JOIN `guilherme-454214.locadora.aluguel` a 
      ON cli.codcliente = a.codcliente 
    GROUP BY cli.codcliente, cli.nome
    """,
    
    # Questão 41
    "Q41": """
    SELECT cli.nome, SUM(ca.valor) AS total_gasto  
    FROM `guilherme-454214.locadora.cliente` cli 
    JOIN `guilherme-454214.locadora.aluguel` a 
      ON cli.codcliente = a.codcliente 
    JOIN `guilherme-454214.locadora.carro` ca 
      ON a.codcarro = ca.codcarro 
    GROUP BY cli.codcliente, cli.nome
    """,
    
    # Questão 43
    "Q43": """
    SELECT cli.nome, ca.modelo, a.data_aluguel 
    FROM `guilherme-454214.locadora.cliente` cli 
    JOIN `guilherme-454214.locadora.aluguel` a 
      ON cli.codcliente = a.codcliente 
    JOIN `guilherme-454214.locadora.carro` ca 
      ON a.codcarro = ca.codcarro 
    WHERE 
      EXTRACT(MONTH FROM a.data_aluguel) = 4 
      AND EXTRACT(YEAR FROM a.data_aluguel) = 2023
    ORDER BY a.data_aluguel
    """,
    
    # Questão 50
    "Q50": """
    SELECT cli.nome, ca.modelo, ma.marca, SUM(ca.valor) AS total_gasto  
    FROM `guilherme-454214.locadora.cliente` cli 
    JOIN `guilherme-454214.locadora.aluguel` a 
      ON cli.codcliente = a.codcliente 
    JOIN `guilherme-454214.locadora.carro` ca 
      ON a.codcarro = ca.codcarro 
    JOIN `guilherme-454214.locadora.marca` ma 
      ON ca.codmarca = ma.codmarca 
    WHERE a.data_aluguel BETWEEN '2023-04-01' AND '2023-04-30'
    GROUP BY cli.codcliente, ca.codcarro, cli.nome, ca.modelo, ma.marca
    """
}

def run_query(query_name):
    """Executa uma query e retorna um DataFrame"""
    query = queries.get(query_name)
    if not query:
        raise ValueError(f"Query {query_name} não encontrada")
    
    query_job = client.query(query)
    results = query_job.result()
    return results.to_dataframe()

# Exemplo de uso:
if __name__ == "__main__":
    # Executar todas as queries e salvar em DataFrames
    dfs = {}
    for qname in queries.keys():
        dfs[qname] = run_query(qname)
        print(f"Query {qname} executada com sucesso!")
        print(f"Resultados ({qname}):\n{dfs[qname].head()}\n")