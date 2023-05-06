nome=input("Digite o seu nome aqui: ")
idade=int(input('Digite a sua idade: '))
if idade>64:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")