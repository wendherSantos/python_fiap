from funcoes.funcoes_arquivos import *

inventario = {}

opcao = chamar_menu()
while opcao>0 and opcao<4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            print(linha[2:-1])
    opcao = chamar_menu()