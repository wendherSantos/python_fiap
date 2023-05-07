def chamar_menu():
    opcao = int(input("\nDigite: \n"
                  "\n<1> para registrar o ativo\n"
                  "<2> para persistir em arquivo\n"
                  "<3> para exibir ativos armazenados: "))
    return opcao

def registrar (dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("\nDigite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp = input("\nDigite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
            for chave, valor in dicionario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + valor[2]+"\n")
                return "Persistido com sucesso!"

def exibir():
    with open("inventario.csv", "r") as inv:
            linhas=inv.readline()
    return linhas