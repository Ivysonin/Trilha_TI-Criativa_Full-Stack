'''
EXERCICIO:
Explique o passo a passo para prever chuva usando apenas sinais da natureza, 
sem acesso a aplicativos ou meteorologia online
'''

sinal = 0

print('\n=== PREVISÃO DE CHUVA ===\n')

# Verificando as NUVENS
print('Como as nuvens estão no céu hoje?')
print('1 - Escuras')
print('2 - Acinzentado')
print('3 - Claras')
nuvem = input("Digite apenas uma alternativa(1-3): ")

match nuvem:
    case "1":
        sinal += 1
    case "2":
        sinal += 1
    case "3":
        sinal += 0

# Verificando o VENTO
print('\nComo o vento está hoje?')
print('1 - Forte')
print('2 - Velocidade crescente')
print('3 - Suave')
vento = input("Digite apenas uma alternativa(1-3): ")

match vento:
    case "1":
        sinal += 1
    case "2":
        sinal += 1
    case "3":
        sinal += 0

# Verificando os ANIMAIS
print('\nComo os animais estão se comportando hoje?')
print('1 - Buscando abrigo')
print('2 - Tranquilos')
print('3 - Mudanças de comportamento')
animal = input("Digite apenas uma alternativa(1-3): ")

match animal:
    case "1":
        sinal += 1
    case "2":
        sinal += 0
    case "3":
        sinal += 1

# Verificando o total de sinais
if sinal == 3:
    print('\nRESULTADO: Grande tendencia de chuva')
elif sinal == 2:
    print('\nRESULTADO: Pode chover nos proximos dias')
else:
    print('\nRESULTADO: A chance de chuva é muito baixa')