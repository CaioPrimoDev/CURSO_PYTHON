# Bibliotecas
import requests # importação geral
import json

from decimal import Decimal # importação especifica

# FIM - BIBLIOTECAS

# Link geral (selecionar a moeda requerida)
#  https://economia.awesomeapi.com.br/json/last/:moedas
# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

api = " https://economia.awesomeapi.com.br/json/last/USD-BRL"

# resp = resposta
resp = requests.get(api)
content = resp.content
cotacao = json.loads(content)
value = cotacao['USDBRL']['bid']

dollar = Decimal(value)

print("Preço do dolar: $", cotacao['USDBRL']['bid'])
print("Preço do dolar: $", dollar)

real = input("Digite uma valor em Reais: ")
# real = Decimal(real)

value_dollar = Decimal(real) / dollar
print("Valor em Dollar:", value_dollar)


value_real = input("Digite o valor em dolares: ")
value_real = Decimal(value_real)

print("Valor em reais: R$", value_real*dollar)

'''
print(type(content))
print(type(cotacao))

print(content)
print(cotacao)
'''