import requests

url = 'https://jsonplaceholder.typicode.com/users'

try:
    resposta = requests.get(url)
    users = resposta.json()

    # Extrair os campos necessários
    dados_users = []
    for user in users:
        dados_users.append({
            'nome': user['name'],
            'username': user['username'],
            'email': user['email'],
            'rua': user['address']['street'],
            'numero': user['address']['suite']
        })

    print(dados_users)
except Exception as e:
    print(f'Erro ao buscar dados dos usuários: {e}')

#utilizei a biblioteca requests para fazer a requisição HTTP dos dados
#apos obter os dados de cada usuário eles foram salvos no formato desejado, extraindo os campos relevantes
#essa solução se baseia na simplicidade de uso, disponibilidade da API e facilidade de extração dos dados necessários
