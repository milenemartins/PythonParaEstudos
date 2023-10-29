# O comando continue é outra instrução de controle de fluxo em Python que é usada principalmente em loops (for ou while). 
# Ao contrário do break, que encerra completamente a execução do loop, o continue interrompe a iteração atual do loop e continua com a próxima iteração.

for i in range(5):
    if i == 2:
        continue # Pula para a próxima iteração quando i é igual a 2
    print(i)
    
print("Loop finalizado.")
