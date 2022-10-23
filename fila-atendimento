import time
temporizador = time.time()
último = 0
fila = list(range(1,último+1))
#fila2 = list(range(1,último2+1))
#fila3 = list(range(1,último3+1))
while True:
     print("\nExistem %d clientes na fila" % len(fila))
     print("Fila atual:", fila)
     print("Digite F para adicionar um cliente ao fim da fila, \nou A para realizar o atendimento. S para sair.")
     print('Ou digite C para se cadastrar no servidor')
     
     operação = input("Operação (C, F, A ou S):")
     
     if operação == "C":
         if(len(fila)):
               print('Escolha o seu número: ' + input(numero))
               print('Escolha um nome: ') + input(nome)
               fila[numero] = "nome"
               print("\nCliente %d registrado" % nome)
               
     if operação == "A":
         if(len(fila))>0:
               atendido = fila.pop(0)
               print("\nCliente %d atendido" % atendido)
         else:
               print("\nFila vazia! Ninguém para atender.")
     elif operação == "F":
         if(len(fila))<5:
             último += 1 # Increnta o ticket do novo cliente
             fila.append(último)
             print("\nCliente registrado")
         else:
             print('\nFILA CHEIA, VOCÊ SERA REDIRECIONADO PARA OUTRO SERVIDOR')
     elif operação == "S":
         break
     else:
         print("\nERROR! Operação inválida! Digite apenas C, F, A ou S")
