# HADOOP

# Links auxiliares
- https://www.youtube.com/watch?v=knAS0w-jiUk&ab_channel=IvyProSchool (Instalar o Hadoop no Windows 10)
- https://www.youtube.com/watch?v=OmcSTQVkrvo&t=104s&ab_channel=AmpCode (Instalar Apache PySpark)

# Comandos (Hadoop Instalado Localmente)
- cd c:\hadoop\sbin\ (Pasta do hadoop, altere correspondente a sua máquina) 
    - start-dfs.cmd
    - start-yarn.cmd
    - stop-all.cmd (Para encerrar)
    - jps (Para verificar se todos os clusters estão rodando)

# Comandos (Spark Instalado Localmente)
- cd c:\spark\spark-3.5.0-bin-hadoop3\bin (Pasta do Spark, altere correspondente a sua máquina)
    - spark-shell (Para iniciar o Spark)

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
- docker cp client_data.csv namenode:/tmp/ (Para enviar o arquivo na pasta temporária do namenode)
- docker exec -it namenode /bin/bash (Acessando a linha de comando do namenode dentro do Docker)
- Dentro do namenode:
    cd /tmp/ (Para acessar a pasta temporária)
    hdfs dfs -mkdir -p /user/root/input (Cria um diretório onde será utilizado para armazenar os dados)
    hdfs dfs -put client_data.csv /user/root/input/ (Para transferir o arquivo csv para a pasta do namenode)
    hdfs dfs -cat /user/root/input/client_data.csv (Para ler o que esta no arquivo)

## URLs de acesso:
- localhost:9870 -> Namenode UID
- localhost:9000 -> Namenode para requests
- localhost:8088 -> Hadoop Cluster


