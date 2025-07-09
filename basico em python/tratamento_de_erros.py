# usando try...except

def subtracao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError: #coloca o nome do erro aqui
        print("Erro: impossível dividir por 0")

subtracao(4,2)
subtracao(3,0)

# erros mais comuns:

# TypeError

def subtracao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except TypeError as e:
        print(f"O tipo do dado inserido é incorreto. Mais detalhes: {e}")

subtracao(1,"a")


try:
    print("a")
except ValueError, TypeError:
    print()
