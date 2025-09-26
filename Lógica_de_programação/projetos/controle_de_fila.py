import time

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_amarelo = '\033[33m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# Lista simulando banco de dados
fila_entrada = [
    {"nome": "Ivyson", "codigo_valido": 1, "participando": False},
    {"nome": "Felipe", "codigo_valido": 2, "participando": False},
    {"nome": "José Pedro", "codigo_valido": 3, "participando": False},
    {"nome": "Alexandre", "codigo_valido": 4, "participando": False},
    {"nome": "Bárbara", "codigo_valido": 5, "participando": False},
    {"nome": "Eduardo", "codigo_valido": 6, "participando": False},
    {"nome": "Eduardo", "codigo_valido": 7, "participando": False},
    {"nome": "Will", "codigo_valido": 8, "participando": False},
    {"nome": "Pedro", "codigo_valido": 9, "participando": False},
    {"nome": "Vicente", "codigo_valido": 10, "participando": False},
    {"nome": "Paulo", "codigo_valido": 11, "participando": False},
    {"nome": "Henrique", "codigo_valido": 12, "participando": False}
]

print(f"{cor_amarelo}\nIniciando controle de entrada no evento...\n{reset_cor}")
time.sleep(2)

# A função any() só para de executar quando todos da lista for True.
# Percorre a fila de entrada por pessoa. Se o "participando" for False retorna True porque estou usando o not.
while any(not pessoa["participando"] for pessoa in fila_entrada):
    print(f"{cor_ciano}Processando a entrada de pessoas para o evento...\n{reset_cor}")

    nome = input('Digite o seu nome: ')
    codigo = int(input('Digite seu código: '))

    for pessoa in fila_entrada:
        if pessoa["nome"] == nome and pessoa["codigo_valido"] == codigo:
            if pessoa["participando"]:
                print(f'{cor_vermelho}\n{nome} já entrou no evento!{reset_cor}')
            else:
                pessoa["participando"] = True
                print(f"\n{cor_verde}{nome} teve o ingresso validado e entrou no evento.{reset_cor}")
        
    print(f"{cor_amarelo}\nAguardando próximo lote...\n{reset_cor}")
    time.sleep(2)

print(f"{cor_verde}Todos os participantes foram processados. Entrada encerrada.\n{reset_cor}")