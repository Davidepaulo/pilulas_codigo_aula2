import datetime
# entrada
data_compra + input('Digite a data da compra d/m/aaaa: ')
meses = int (input('prazo de garantia:'))
#processamento
data_inicial = datetime.datatime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + datetime.timedelta (days-meses * 30)
#saida
print (f'garantia válidade até {data_final.strftime('%d/%m/%Y')}')
print (f'Dia da semana: {data_final.strftime('%A')}')
