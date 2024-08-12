# Criação da lista LIFO (pilha)
pilha = []

# Função para adicionar um item à pilha
def add_pilha(stack, item):
    stack.append(item)  # Adiciona o item no topo da pilha

# Função para remover o item mais recente (LIFO)
def remove_pilha(stack):
    if stack:
        return stack.pop()  # Remove e retorna o item no topo da pilha
    else:
        return None  # Retorna None se a pilha estiver vazia

# Adicionando itens à pilha
add_pilha(pilha, "item1")
add_pilha(pilha, "item2")
add_pilha(pilha, "item3")

# Mostrando a pilha após adições
print("Pilha após adições:", pilha)

# Removendo um item da pilha (LIFO)
removed_item = remove_pilha(pilha)
print("Item removido:", removed_item)

# Mostrando a pilha após remoção
print("Pilha após remoção:", pilha)


#ao contrario do exercicio 10 que foi necesario utilizar um comando adicional de uma biblioteca para fazer o armagenamento de dados no formato FIFO
#neste o proprio Python ja faz isso de forma nativa com a função de lista 