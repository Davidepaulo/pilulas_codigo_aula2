import math
#entradas
assinantes = int(input ('assinantes atuais:'))
mensalidade = float (input('valor da mensalidade:'))
taxa = float (input('taxa de crescimento mensal (%): '))/100
meses = int (input('meses de projeção:'))
#processamento
assinantes_finais = assinantes * math.pow ((1+taxa),meses)
receita_final = assinantes_finais * mensalidade 
# saida
print(f'assinates estimados:{ assinantes_finais:.0f}')
print(f'receita mensal estimada R$:) {receita_final:.2f}')

