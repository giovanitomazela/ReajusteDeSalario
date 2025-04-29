s = float(input('Digite seu salário: '))

print('Seu salário é de: R${}'.format(s))

if s > 2000:
    print('O novo salário é de: R$ {}'.format((s*0.10) + s))
else:
    print('O novo salário é de: R$ {}'.format((s * 0.15) + s))
