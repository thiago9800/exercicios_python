import requests
def contar_tarefas():

    url = "https://jsonplaceholder.typicode.com/todos"
    completadas = 0
    pendentes = 0
    
    try:
        resposta = requests.get(url)       
        data = resposta.json()
        
        for task in data:
            if task["completed"]:
                completadas += 1
            else:
                pendentes += 1  
        return completadas, pendentes, 1
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {resposta.status_code}")
        return 0, 0, 0

completadas, pendentes, conec = contar_tarefas()
if conec == 1:
    print(f"Tarefas completadas: {completadas}")
    print(f"Tarefas pendentes: {pendentes}")
else:
    print("Não foi possível obter as tarefas.")

#Escolhi usar a biblioteca requests porque ela é amplamente utilizada para fazer requisições HTTP em Python.
#A função contar_tarefas() faz a requisição, verifica se a resposta foi bem-sucedida (código de status 200), 
#analisa o JSON e calcula a quantidade de tarefas completadas e pendentes
#o codigo salva a decodificação JSON à variável "data" e apartir disso percorre todo o json para verificar se as tasks foram completada ou não