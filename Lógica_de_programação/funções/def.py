# Como definir uma função
def ola():
    print("Ola mundo!")

# Usando parâmetro
def olaNome(nome:str):
    print(f'Ola {nome}')

# Função com valor padrão (default)
def apresentar(nome:str = "Visitante"):
    print(f"Bem-vindo, {nome}!")