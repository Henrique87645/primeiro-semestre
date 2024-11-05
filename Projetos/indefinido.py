<<<<<<< HEAD
soma_valores = 0
total_valores = 0
valores_positivos = 0
valores_negativos = 0

print("Digite os valores.")
print("Digite '0' para encerrar a entrada de valores.")
for i in range(100):
    valor = float(input("Digite um valor: "))
    if valor == 0:
        break
    soma_valores += valor
    total_valores += 1
    if valor > 0:
        valores_positivos += 1
    elif valor < 0:
        valores_negativos += 1
if total_valores > 0:
    media = soma_valores / total_valores
else:
    media = 0
if total_valores > 0:
    percentual_positivos = (valores_positivos / total_valores) * 100
    percentual_negativos = (valores_negativos / total_valores) * 100
else:
    percentual_positivos = 0
    percentual_negativos = 0

print("Média aritmética dos valores: {}".format(media))
print("Quantidade de valores positivos: {}".format(valores_positivos))
print("Quantidade de valores negativos: {}".format(valores_negativos))
print("Percentual de valores positivos: {:.2f}%".format(percentual_positivos))
print("Percentual de valores negativos: {:.2f}%".format(percentual_negativos))
=======
soma_valores = 0
total_valores = 0
valores_positivos = 0
valores_negativos = 0

print("Digite os valores.")
print("Digite '0' para encerrar a entrada de valores.")
for i in range(100):
    valor = float(input("Digite um valor: "))
    if valor == 0:
        break
    soma_valores += valor
    total_valores += 1
    if valor > 0:
        valores_positivos += 1
    elif valor < 0:
        valores_negativos += 1
if total_valores > 0:
    media = soma_valores / total_valores
else:
    media = 0
if total_valores > 0:
    percentual_positivos = (valores_positivos / total_valores) * 100
    percentual_negativos = (valores_negativos / total_valores) * 100
else:
    percentual_positivos = 0
    percentual_negativos = 0

print("Média aritmética dos valores: {}".format(media))
print("Quantidade de valores positivos: {}".format(valores_positivos))
print("Quantidade de valores negativos: {}".format(valores_negativos))
print("Percentual de valores positivos: {:.2f}%".format(percentual_positivos))
print("Percentual de valores negativos: {:.2f}%".format(percentual_negativos))
>>>>>>> 5e1e66058506390d589a31faeb66ddd3e63232e3
