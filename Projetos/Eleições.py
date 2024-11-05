<<<<<<< HEAD
votos_candidato0 = 0
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_nulos = 0
votos_em_branco = 0
qtd = int(input('Quantos eleitores serão: '))
for i in range(qtd):
    for c in range(1, 4+1):
        print('Escolha um dos seguintes candidatos, {}'.format(c))
    print('Caso queira votar nulo, 5')
    print('Caso queira votar em branco, 6')
    print('Para encerrar a votação, 0')
    cand = int(input('Qual seu voto: '))
    if cand == 0:
        break
    if cand == 1:
        votos_candidato0 += 1
    elif cand == 2:
        votos_candidato1 += 1
    elif cand == 3:
        votos_candidato2 += 1
    elif cand == 4:
        votos_candidato3 += 1
    elif cand == 5:
        votos_nulos += 1
    elif cand == 6:
        votos_em_branco += 1
    else:
        print("Código inválido. Por favor, insira um número entre 1 e 6.")
print("Total de votos para o candidato 1: {}".format(votos_candidato0))
print("Total de votos para o candidato 2: {}".format(votos_candidato1))
print("Total de votos para o candidato 3: {}".format(votos_candidato2))
print("Total de votos para o candidato 4: {}".format(votos_candidato3))
print("Total de votos nulos: {}".format(votos_nulos))
print("Total de votos em branco: {}".format(votos_em_branco))
=======
votos_candidato0 = 0
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_nulos = 0
votos_em_branco = 0
qtd = int(input('Quantos eleitores serão: '))
for i in range(qtd):
    for c in range(1, 4+1):
        print('Escolha um dos seguintes candidatos, {}'.format(c))
    print('Caso queira votar nulo, 5')
    print('Caso queira votar em branco, 6')
    print('Para encerrar a votação, 0')
    cand = int(input('Qual seu voto: '))
    if cand == 0:
        break
    if cand == 1:
        votos_candidato0 += 1
    elif cand == 2:
        votos_candidato1 += 1
    elif cand == 3:
        votos_candidato2 += 1
    elif cand == 4:
        votos_candidato3 += 1
    elif cand == 5:
        votos_nulos += 1
    elif cand == 6:
        votos_em_branco += 1
    else:
        print("Código inválido. Por favor, insira um número entre 1 e 6.")
print("Total de votos para o candidato 1: {}".format(votos_candidato0))
print("Total de votos para o candidato 2: {}".format(votos_candidato1))
print("Total de votos para o candidato 3: {}".format(votos_candidato2))
print("Total de votos para o candidato 4: {}".format(votos_candidato3))
print("Total de votos nulos: {}".format(votos_nulos))
print("Total de votos em branco: {}".format(votos_em_branco))
>>>>>>> 5e1e66058506390d589a31faeb66ddd3e63232e3
