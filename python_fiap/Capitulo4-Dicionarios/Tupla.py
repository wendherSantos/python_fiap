ips={}
resp="S"
while resp=="S":
    ips[(input("\nDigite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))]=input("\nNome da máquina: ")
    resp=input("Digite <S> para continuar: \n").upper()

print("\nExibindo ip's: \n")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("\nExibindo máquinas com o mesmo endereço: \n")
pesquisa=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):
        print(nome)

print("\nExibindo as máquinas que compõem uma mesma rede: \n")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)
