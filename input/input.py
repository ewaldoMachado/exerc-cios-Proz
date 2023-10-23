def calcular():
  num1 = 0
  num2 = 0
  operacao = 0

  print("Escolha uma Operação:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 0 - Sair")
  operacao = input()

  if (operacao != '0' and operacao != '1' and operacao != '2' and operacao != '3' and operacao != '4'):
     print("Essa opção não existe")
     calcular()
  elif (operacao == '0'):
     print("Operação encerrada")
  elif (operacao == '1'):
     print("Digite o primreiro valor: ")
     num1 = int(input())
     print("Digite o segundo valor: ")
     num2 = int(input())
     resultado = num1 + num2
     print("O resultado é: ", resultado)
     calcular()
  elif operacao == '2':
     print("Digite o primreiro valor: ")
     num1 = int(input())
     print("Digite o segundo valor: ")
     num2 = int(input())
     resultado = num1 - num2
     print("O resultado é: ", resultado)
     calcular()    
  elif operacao == '3':
     print("Digite o primreiro valor: ")
     num1 = int(input())
     print("Digite o segundo valor: ")
     num2 = int(input())
     resultado = num1 * num2
     print("O resultado é: ", resultado)
     calcular()
  elif operacao == '4':
     print("Digite o primreiro valor: ")
     num1 = int(input())
     print("Digite o segundo valor: ")
     num2 = int(input())
     resultado = num1 / num2
     print("O resultado é: ", resultado)
     calcular()
      
calcular()