# A função range() gera uma sequência de números de acordo com os parâmetros fornecidos. 
# Essa sequência é frequentemente usada em loops "for" para iterar sobre uma série de valores.
# A função range é uma built-in do python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). 
# Se usarmos range(i, j) será produzido:
# i, i+1, i+2, i+3, ..., j-1
# Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step(opcional)


# Tabuada do 5
for tabuada in range(0, 51, 5):
    print(tabuada, end=" ")