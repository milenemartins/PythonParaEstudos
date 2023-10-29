# O comando break é uma instrução em Python que é utilizada para interromper a execução de um loop antes que a condição de término normal seja atingida. 
# Ele é frequentemente usado em conjunto com loops while e for para sair do loop prematuramente com base em uma condição específica.

contador = 0

while contador < 11:
    print(contador)
    if contador == 10:
        break # Sai do loop quando contador atinge 10
    contador += 1
    
print("Loop finalizado.")
