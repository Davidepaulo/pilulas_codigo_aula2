import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
r1 = float(input('receita mês 1:'))
r2 = float(input('receita mês 2:'))
r3 = float(input('receita mês 3:'))
total = r1+r2+r3
print(f'mês 1: {locale.currency(r1, grouping=true)}')
print(f'mês 2: {locale.currency(r2, grouping=true)}')
print(f'mês 3: {locale.currency(r3, grouping=true)}')
print(f'mês 1: {locale.currency(total, grouping=true)}')