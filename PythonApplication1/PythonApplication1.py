
from datetime import datetime
def obter_limite():
    print("Bem Vindo à Loja de Jakeline Victor Pereira! Esta é a melhor Loja da Cidade! ")

    cargo = input('Informe seu cargo: ')
    salario = float(input('Informe seu salario: '))
    ano_de_nascimento = int(input('Informe o ano de nascimento: '))

    data_e_hora_atuais = datetime.now()
    ano_atual =int(data_e_hora_atuais.strftime('%Y'))

    global idade
    idade = int(ano_atual - ano_de_nascimento)

    limite_de_gastos = salario * (idade / 1000) + int(100)

    print('Os dados que você digitou foram: ')
    print('Cargo: ' + cargo)
    print('Salario: ' , salario)
    print('Ano de Nascimento: ', ano_de_nascimento)
    print(idade,' anos') 
    print('Limite de Gastos: ' , limite_de_gastos)

    return limite_de_gastos

def verificar_produto(limite_de_gastos):
    produto = input('Digite o nome do produto: ')
    nome ='Jakeline Victor Pereira'
    tamanho_nome_completo = len(nome)
    tamanho_primeiro_nome = len(nome.split(" ")[0])
    preco = float(input('Digite o valor do produto: '))

    global valor_total_produtos
    valor_total_produtos = valor_total_produtos + preco

    if valor_total_produtos < limite_de_gastos * 0.6:
        print('Liberado!')
    elif (valor_total_produtos >= limite_de_gastos * 0.6 and valor_total_produtos < limite_de_gastos * 0.9):
        print('Liberado ao parcelar em até 2 vezes!')
    elif (valor_total_produtos >= limite_de_gastos * 0.9 and valor_total_produtos <= limite_de_gastos * 1.0):
        print('Liberado ao parcelar em 3 ou mais vezes!')
    else:
        print('Bloqueado!')

    print('Nome do Produto: ' + produto)
    print('Preço: R$ ', preco)
    print('Valor da soma dos produtos: R$ ', valor_total_produtos)

    global idade

    if (preco >= tamanho_nome_completo and preco <= idade):
        print('Você terá um desconto de ', tamanho_primeiro_nome, '%!')
        preco_desconto = preco - preco*(tamanho_primeiro_nome/100)
        print('Preço do produto com desconto: ', preco_desconto)

def main():
   
    limite_de_gastos = obter_limite()

    quantidade_de_produtos = int(input('Quantidade de produtos que deseja cadastrar? '))
    print(quantidade_de_produtos)
    n = 0
    while n < quantidade_de_produtos:
        verificar_produto(limite_de_gastos)
        n = n + 1

##Fluxo principal

idade = 0
valor_total_produtos =float(0)
main()