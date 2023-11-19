from faker import Faker
import csv

fake = Faker()

num_clientes = 1000
client_data = []
for _ in range(num_clientes):
    client_data.append({
        'nome': fake.name(),
        'endereco': fake.address(),
        'email': fake.email(),
        'numero_telefone': fake.phone_number(),
    })

with open('client_data.csv', 'w', newline='') as file:
    fieldnames = ['nome', 'endereco', 'email', 'numero_telefone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(client_data)