# Maneiras de definir listas
frutas = ["Maça", "Banana", "Laranja"]
compras = []
itens = list()

print(frutas[0])                     # Acessar Maça

frutas.append("uva")                 # Adiciona um novo item na lista

frutas.pop(1)                        # Remove usando o indice

frutas.remove("Banana")              # Remove o item "Banana" da lista

frutas.insert(1, "Abacaxi")          # Insere "Abacaxi" na posição 1

frutas.sort()                        # Ordena a lista em ordem alfabética

frutas.reverse()                     # Inverte a ordem da lista

frutas.index("Maça")                 # Retorna o índice do item "Maça"

frutas.count("Laranja")              # Conta quantas vezes "Laranja" aparece

frutas.extend(["Melancia", "Pera"])  # Adiciona múltiplos itens à lista

frutas.clear()                       # Remove todos os itens da lista