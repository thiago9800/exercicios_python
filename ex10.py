from collections import deque

# Criação da lista (deque) FIFO
fila = deque()

# Função para adicionar um item à fila
def add_fila(queue, item):
    queue.append(item)  # Adiciona o item no final da fila

# Função para remover o item mais antigo (FIFO)
def remove_fila(queue):
    if queue:
        return queue.popleft()  # Remove e retorna o item mais antigo
    else:
        return None  # Retorna None se a fila estiver vazia

# Adicionando itens à fila
add_fila(fila, "item1")
add_fila(fila, "item2")
add_fila(fila, "item3")

# Mostrando a fila após adições
print("Fila após adições:", list(fila))

# Removendo um item da fila (FIFO)
removed_item = remove_fila(fila)
print("Item removido:", removed_item)

# Mostrando a fila após remoção
print("Fila após remoção:", list(fila))

#eu usei o comando "deque"(abreviação de “double-ended queue”, que significa “fila de duas extremidades”) na criação da lista
#deque é uma estrutura de dados em Python que combina características de pilha (stack) e fila (queue) ou seja
#é uma fila na qual você pode adicionar e remover elementos tanto no início quanto no final. 
#Ele é otimizado para operações de inserção e remoção rápidas em ambas as extremidades.

#A função add_fila adiciona itens ao final da fila e a função remove_fila remove o item mais antigo do início da fila
#so foi necesario fazer a função "add_fila" que adiciona itens ao topo da pilha 
# e a função "remove_fila" remove o item mais recente do topo da pilha