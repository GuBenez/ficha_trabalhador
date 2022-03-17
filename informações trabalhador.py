"""crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
se por acaso a CPTS for diferente de Zero, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, alem da idade, com quantos anos essa pessoa vai se aposentar."""

from datetime import date
hoje = date.today().year
trabalho = {}
trabalho["nome"] = str(input("INsira o nome do funcionário: "))
ano = int(input("Insira o ano de nascimento: "))
idade = hoje - ano
trabalho["idade"] = idade
trabalho["carteira"] = int(input("Insira a CPTS: "))
if trabalho["carteira"] == 0:

    print("-=" * 30)
    print(f"{trabalho['nome']}, possui {trabalho['idade']} anos, mas nunca trabalhou antes")
if trabalho["carteira"] != 0:
    trabalho["ano contratação"] = int(input("Qual o ano de contratação: "))
    trabalho["aposentadoria"] = trabalho["ano contratação"] + 35
    trabalho["salário"] = float(input("Qual o salário desse trabalhador: R$ "))
    print("-=" * 30)
    print(f"No fim de {hoje} {trabalho['nome']} terá {trabalho['idade']} anos. Sua contratação foi em {trabalho['ano contratação']}, sua aposentadoria será no ano {trabalho['aposentadoria']}, e seu salário de contratação era R$ {trabalho['salário']:.2f}")

