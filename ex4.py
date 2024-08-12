# Lista original
lista = ["   joao   ","   maria   ","  joana  "]

# Nova lista para armazenar os itens processados
nova_lista = []

# Iterando sobre a lista original e removendo espaços
for item in lista:
    novo_item = item.strip()  # Remove espaços no início e no final
    nova_lista.append(novo_item)

# Exibindo a nova lista
print(nova_lista)

