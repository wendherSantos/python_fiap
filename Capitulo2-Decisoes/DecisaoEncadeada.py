nome=input("Nome: ")
idade=int(input("Idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade >= 65:
    print("Paciente COM prioridade!")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO!")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO!")