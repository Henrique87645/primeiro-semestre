<<<<<<< HEAD
preco = float(input('Digite o valor do produto: '))
print('1° a vista no pix = pix')
print('2° cartão = cartão')
print('3° parcelado no cartão = parcelado')
print('4° parcelado em 12 vezes no cartão = parcelado em 12')

pg = input('insira a forma de pagamento: ')
pix = (preco * 0.90)
cartao = (preco * 0.85)
parcela = (preco * 1)
par12vezez = (preco * 1.10)

if pg == 'pix':
    print(pix)

elif pg == 'cartão':
    print(cartao)

elif pg == 'parcelado':

    print(parcela)

elif pg == 'parcelado em 12':
    print(par12vezez)
else:
=======
preco = float(input('Digite o valor do produto: '))
print('1° a vista no pix = pix')
print('2° cartão = cartão')
print('3° parcelado no cartão = parcelado')
print('4° parcelado em 12 vezes no cartão = parcelado em 12')

pg = input('insira a forma de pagamento: ')
pix = (preco * 0.90)
cartao = (preco * 0.85)
parcela = (preco * 1)
par12vezez = (preco * 1.10)

if pg == 'pix':
    print(pix)

elif pg == 'cartão':
    print(cartao)

elif pg == 'parcelado':

    print(parcela)

elif pg == 'parcelado em 12':
    print(par12vezez)
else:
>>>>>>> 5e1e66058506390d589a31faeb66ddd3e63232e3
    print('código inserido invalido')