import random 
#entradas
cotacao = float (input('cotação atual do dolar: '))
#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print(f'variação simulada: {variacao: .3%}')
print(f'nova cotação: R$ {nova_cotacao:.4f}')