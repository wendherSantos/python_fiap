primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

# MINHA RESPOSTA

# if primeiro_valor > segundo_valor:
#     print('O primeiro valor:', primeiro_valor, 'é maior do que o segundo valor:', segundo_valor)
# elif segundo_valor == primeiro_valor:
#     print('O segundo valor:', segundo_valor, 'é igual ao primeiro valor:', primeiro_valor)
# else:
#     print('O segundo valor:', segundo_valor, 'é maior do que o primeiro valor:', primeiro_valor)

if primeiro_valor > segundo_valor:
    print(
       f'{primeiro_valor=} é maior ao que {segundo_valor=}' 
    )
elif segundo_valor == primeiro_valor:
    print(
        f'{primeiro_valor=} é igual ao o {segundo_valor=}'
    )
else:
    print(
       f'{segundo_valor=} é maior ao que {primeiro_valor=}' 
    )