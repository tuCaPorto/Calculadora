# Exercício guiado - Calculadora
"""
Calculadora com while
"""

while True:
    n1 = int(input("Digite o 1° numero: "))
    n2 = int(input("Digite o 2° numero: "))
    op = input("Digite o operador: ")
    
    if op == '+':
        n1 + n2
        resultado = n1 + n2
        print(resultado)
    elif op == '-':
        n1 - n2
        resultado = n1 - n2
        print(resultado)
    elif op == '*':
        n1 * n2
        resultado = n1 * n2
        print(resultado)
    elif op == '/':
        n1 / n2
        resultado = n1 / n2
        print(resultado)
    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    
    if sair is True:
        break