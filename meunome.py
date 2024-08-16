import time

nome = "Sidney"
for letra in nome:
    print(letra, end='', flush=True)
    time.sleep(0.3)  # Atraso de 0.3 segundos entre as letras
