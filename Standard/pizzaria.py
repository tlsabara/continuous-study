# Importa as bibliotecas necessárias
import datetime
import json

# Define as classes necessárias
class Pizza:
    def __init__(self, nome, tamanho, ingredientes, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.ingredientes = ingredientes
        self.preco = preco

class Pedido:
    def __init__(self, pizzas, data, hora):
        self.pizzas = pizzas
        self.data = data
        self.hora = hora

# Define as pizzas disponíveis
pizzas = [
    Pizza("Mussarela", "Pequena", ["Mussarela"], 20),
    Pizza("Marguerita", "Média", ["Molho de tomate", "Queijo mussarela", "Tomate"], 30),
    Pizza("Calabresa", "Grande", ["Molho de tomate", "Queijo mussarela", "Calabresa"], 40),
]

# Define a função para criar um pedido
def criar_pedido():
    # Pega as informações do pedido do usuário
    pizzas = []
    while True:
        nome = input("Nome da pizza: ")
        if nome == "":
            break
        tamanho = input("Tamanho da pizza (Pequena, Média ou Grande): ")
        ingredientes = input("Ingredientes da pizza: ")
        preco = input("Preço da pizza: ")
        pizzas.append(Pizza(nome, tamanho, ingredientes, preco))

    # Pega a data e a hora do pedido
    data = datetime.datetime.now()
    hora = datetime.datetime.now().time()

    # Cria um objeto Pedido com as informações coletadas
    pedido = Pedido(pizzas, data, hora)

    # Salva o pedido em um arquivo JSON
    with open("pedidos.json", "w") as f:
        f.write(json.dumps(pedido.__dict__))

# Chama a função para criar um pedido
criar_pedido()
