<<<<<<< HEAD
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu peimeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
=======
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu peimeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
>>>>>>> 5e1e66058506390d589a31faeb66ddd3e63232e3
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))