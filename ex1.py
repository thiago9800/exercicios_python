response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

# Lista para armazenar os produtos filtrados
produtos_filtrados = []

# Iterando sobre as lojas e produtos
for loja in response: # lup para percorrer cada item ou loja no JSON
    for produto in loja["produtos"]: # lup para percorrer somento os produtos das loja no JSON
        if produto["preço"] > 30: # verificação se o preço e superior a 30
            produtos_filtrados.append(produto) #se é superior armazena a informaçao 

# Em resumo, o código percorre primeiro as lojas e, para cada loja, examina seus produtos. 
# Isso nos permite aplicar a condição de filtro a cada produto individualmente

# Exibindo os produtos filtrados
for produto in produtos_filtrados:
    print(f"Produto: {produto['nome']} - Preço: R$ {produto['preço']:.2f}")


#eu decidi fazer algo simples já que obrigatoriamente teria que verificar todo o arquivo JSON, fiz um lup para percorrer ele e pegar os dados dos solicitados