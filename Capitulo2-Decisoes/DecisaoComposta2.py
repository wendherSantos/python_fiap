nome=input("Nome: ")
idade=int(input("Idade: "))
doenca_infectocontagiosa=input("Suspeita de doença contagiosa? ").upper()
if idade>=65:
    print("O paciente " + nome + " possui atendimento prioritário!")
elif doenca_infectocontagiosa=="SIM":
    print("O paciente" + nome + " deve ser direcionado para a asala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")
