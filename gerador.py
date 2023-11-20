from faker import Faker
import csv
from hdfs import InsecureClient

# Inicializa a biblioteca Faker para criar dados falsos.
fake = Faker()

# Define o número de clientes e inicia uma lista vazia para armazenar os dados gerados.
num_clientes = 1000
teste = []

# Para cada cliente, gera dados falsos de nome, endereço, email e número de telefone, utilizando o Faker.
for _ in range(num_clientes):
    nome = fake.name()
    endereco = fake.address()
    email = fake.email()
    numero_telefone = fake.phone_number()

    # Adiciona um dicionário contendo os dados do cliente à lista.
    teste.append({
        'nome': nome,
        'endereco': endereco,
        'email': email,
        'numero_telefone': numero_telefone,     
    })

# Define o caminho local onde o arquivo CSV será criado.
local_file_path = './exemplos_csv/teste.csv'

# Abre o arquivo CSV no modo de escrita, cria um escritor CSV e escreve os dados da lista no arquivo CSV.
with open(local_file_path, 'w', newline='') as file:
    fieldnames = ['nome', 'endereco', 'email', 'numero_telefone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(teste)

# Cria um Client para interagir com o Hadoop utilizando o InsecureClient.
client = InsecureClient('http://localhost:9870', user='animo', root="/webhdfs/v1")

# Define o caminho e o nome do arquivo no Hadoop.
hadoop_directory = '/cay'
file_name = 'teste.csv'
hadoop_path = f"{hadoop_directory}/{file_name}"

# Abre o arquivo CSV local no modo de leitura binária e utiliza o Client para escrever esse arquivo no Hadoop.
with open(local_file_path, 'rb') as hdfs_file:
    client.write(hadoop_path, hdfs_file, overwrite=True)

# Exibe uma mensagem informando que o arquivo foi enviado com sucesso para o Hadoop.
print(f"Arquivo {file_name} enviado para {hadoop_directory} no HDFS com sucesso!")


