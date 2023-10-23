# Declarando Função
def calcular():
  if(operacao == '1'):
    resultado = num1 + num2
    print(resultado)

  elif(operacao == '2'):
    resultado = num1 - num2
    print(resultado)

  elif(operacao == '3'):
    resultado = num1 * num2
    print(resultado)

  elif(operacao == '4'):
    resultado = num1 / num2
    print(resultado)

  else: 
    resultado = 0
    print(resultado)

  
# Declaração de variaveis.
num1 = 0
num2 = 0
operacao = 0

print("Digite o primeiro numero")
num1 = int(input())
print("Digite o segundo número")
num2 = int(input())
print("Escolha a Operação: 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir")
operacao = input()

# Chamando a Função
calcular()
