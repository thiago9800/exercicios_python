responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

preco_produto_B = responsejson["produtos"][1]["preço"]
print(f"Preço do Produto B: R$ {preco_produto_B:.2f}")

#Como o JSON já possui uma estrutura organizada, pode acessar diretamente o preço do produto B
#Essa abordagem é simples e eficiente, pois acessa diretamente o valor desejado sem a necessidade de loops ou iterações.
#Dado que o JSON tem uma estrutura fixa e conhecida, não precisamos percorrer todos os produtos.
#Portanto, escolhi essa solução direta para obter o preço do produto B.