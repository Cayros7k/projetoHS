from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import os

# Inicialização de uma sessão Spark.
spark = SparkSession.builder \
    .appName("Lendo arquivo CSV do Hadoop") \
    .master("local") \
    .getOrCreate()

# Definição do caminho do arquivo CSV no hadoop.
file_path = "hdfs://localhost:9000/cay/teste.csv"

# Leitura do arquivo CSV localizado no hadoop para criar um DataFrame Spark.
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Preenche valores nulos nas colunas 'email' e 'numero_telefone' do DataFrame com valores padrão.
df = df.fillna({'email': 'email@example.com', 'numero_telefone': '000-000-0000'})

# Comandos para excluir um diretório no Hadoop
'''
diretorio_a_remover = "hdfs://localhost:9000/cay/teste_tratado.csv"

comando_remover = f"hdfs dfs -rm -r -skipTrash {diretorio_a_remover}"

os.system(comando_remover)
'''


