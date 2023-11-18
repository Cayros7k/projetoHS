# HADOOP

## Utilizando o VENV:
- python -m venv .venv
- .venv\Scripts\activate (Windows)
- source .venv\bin\activate (Ubuntu)

## Instalar todas as bibliotecas utilizadas:
- pip install -r requirements.txt

## Executar o Container do Hadoop:
- cd .\hadoopDockerCompose\ (Acessando a pasta destino do arquivo .yml)
- docker-compose -f hadoop-compose.yml up -d (Para executar  arquivo .yml)

## Comandos importantes:
- docker exec -it namenode /bin/bash (Acessando a linha de comando do namenode dentro do Docker)
- Dentro do namenode:
    hdfs dfs -mkdir -p /user/root (Cria um diretório onde será utilizado para armazenar os dados)

## URLs de acesso:
- localhost:9870 -> Namenode

