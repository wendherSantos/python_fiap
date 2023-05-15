# operadores logicos

# and:
# todas as condicoes precisam ser verdadeiras, se qualquer valor for considerado falso, a expressao inteira sera avaliada naquela valor falso
# sao considerados falsy (que voce já viu):
# 0 0.0 '' == False
# também existe o tipo Mone que é usado para representar um nao valor

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
# .....

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# avaliacao de curto circuito

print(True and True and False)
print(True and None and False)