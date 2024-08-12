class ContaBancaria:
    contador_id = 1

    def __init__(self, nome, cpf):
        self.id = ContaBancaria.contador_id
        ContaBancaria.contador_id += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso
conta1 = ContaBancaria("João Silva", "123.456.789-00")
print(f"Conta criada com sucesso. ID: {conta1.id}, Nome: {conta1.nome}, CPF: {conta1.cpf}, Saldo: R${conta1.saldo:.2f}")

conta1.depositar(500)
conta1.mostrar_saldo()

conta1.sacar(200)
conta1.mostrar_saldo()







