# operadores logicos

# not:
# usado para inverter expressor
# not True = False
# not False = True

senha = input('Senha: ')

if not senha == 123456:
    print('Entrou')
else:
    print('Senha incorreta!')

print(not True)
print(not False)