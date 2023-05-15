# operadores logicos

# or:
# qualquer condicao verdadeira avalia toda a expressao como verdadeira
# se qualquer valor for considerado verdadeiro, a expressao inteira sera avaliada naquele valor
# sao considerados falsy (que voce já viu):
# 0 0.0 '' == False
# também existe o tipo Mone que é usado para representar um nao valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
# .....

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# avaliacao de curto circuito

print(True or True or False)
print(True or None or False)
print(True or 0 or False)
print(0 or 1)
print(0 or 'Wendher')
