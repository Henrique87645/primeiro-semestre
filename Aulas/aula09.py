<<<<<<< HEAD
#MANIPULANDO TEXTOS

frase = 'Olá estou aprendendo Python'
#MANIPULAR AS PALAVRAS
print('-'*36)
print(frase[0:])
print(frase[0:9])
print(frase[0::2])
print(frase[4:9])
print(frase[22])
print(frase[10:27:2])
print(frase[::2])
print('-'*36)
#CONTAR LETRAS
print(frase.count('o'))
print(frase.count('a'))
print(frase.count('dendo'))
print('-'*36)
#MANDAR PARA MAIUSCULO
print(frase.upper().count('O'))
print('-'*36)
#MEDIR O TAMANHO DA FRASE
print(len(frase))
print('-'*36)
#VERIFICANDO PALAVRAS
print('Olá' in frase)
print('-'*36)
#CONTANDO POR FRASE
print(frase.upper().find('ESTOU'))
print('-'*36)
#DIVIDINDO POR BLOCOS
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3][1])
print('-'*36)
#REMOVER ESPAÇOS INDEZEJADOS
palavra = '  A frase tem espaco no começo e fim  '
print(len(palavra))
print(len(palavra.strip()))
#TROCANDO PALAVRAS
palavra = print(palavra.replace('fim', 'troque a palavra fim'))
print('-'*36)


print(""""Olá vou escrever um texto de exemplo, 
mostrando que se utilizar 3 aspas no print é 
possivel escrever um texto com quebras de pargrafos.""")
=======
#MANIPULANDO TEXTOS

frase = 'Olá estou aprendendo Python'
#MANIPULAR AS PALAVRAS
print('-'*36)
print(frase[0:])
print(frase[0:9])
print(frase[0::2])
print(frase[4:9])
print(frase[22])
print(frase[10:27:2])
print(frase[::2])
print('-'*36)
#CONTAR LETRAS
print(frase.count('o'))
print(frase.count('a'))
print(frase.count('dendo'))
print('-'*36)
#MANDAR PARA MAIUSCULO
print(frase.upper().count('O'))
print('-'*36)
#MEDIR O TAMANHO DA FRASE
print(len(frase))
print('-'*36)
#VERIFICANDO PALAVRAS
print('Olá' in frase)
print('-'*36)
#CONTANDO POR FRASE
print(frase.upper().find('ESTOU'))
print('-'*36)
#DIVIDINDO POR BLOCOS
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3][1])
print('-'*36)
#REMOVER ESPAÇOS INDEZEJADOS
palavra = '  A frase tem espaco no começo e fim  '
print(len(palavra))
print(len(palavra.strip()))
#TROCANDO PALAVRAS
palavra = print(palavra.replace('fim', 'troque a palavra fim'))
print('-'*36)


print(""""Olá vou escrever um texto de exemplo, 
mostrando que se utilizar 3 aspas no print é 
possivel escrever um texto com quebras de pargrafos.""")
>>>>>>> 5e1e66058506390d589a31faeb66ddd3e63232e3
print('-'*36)