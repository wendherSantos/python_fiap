resposta="SIM"
while resposta=="SIM":
    for numero in range(0,int(input("Digite um numero para determinar o fim: ")),2000):
        print("  " + str(numero))
resposta = input("Digite SIM para continuar: ").upper()