a = 'A'
b = 'B'
c = 1.1

texto = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = texto.format(
    nome1= a,
    nome2= b,
    nome3= c
)

print(formato)