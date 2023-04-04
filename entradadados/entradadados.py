# Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, 
# o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos,
# no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. 
# Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.
# Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:
nomeCliente = input('Digite o nome do cliente: \n')
diaVencimento = input('Digite o dia de vencimento:\n')
mesVencimento = input('Digite o mês de vencimento: \n')
valorFatura= input('Digite o valor da fatura: \n')

print('Olá ' + nomeCliente + ' A sua fatura com vencimento em ' + diaVencimento +' ' + mesVencimento + ' no valor de R$ ' + valorFatura + ' está fechada.')
