#Declaração das variáveis
andar = 21

#Estrutura de repetição for
for i in range(21, 1, -1):
    andar = andar - 1
    if(andar == 13):
        continue
    print(andar)