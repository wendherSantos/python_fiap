nome=input("Nome: ")
idade=int(input("Idade: "))
doenca_infectocontagiosa=input("Suspeita de doença contagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para a sala AMARELA - COM prioridade")
elif idade<65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para a sala AMARELA - SEM prioridade")
elif idade>=65 and doenca_infectocontagiosa=="NAO":
    print("O paciente será direcionado para a sala BRANCA - COM prioridade")
elif idade<65 and doenca_infectocontagiosa=="NAO":
    print("O paciente será direcionado para a sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeite de doenção infectocontagiosa com SIM ou NAO.")