nome=input("Insira o seu nome: ")
idade=int(input("Insira a sua idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " tem atendimento prioritário? " + prioridade)