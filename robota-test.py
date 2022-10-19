#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#

import re #RegEx: Biblioteca para busca

#Sempre que o código for analisado, ele retornara ao início
while True:
    print('||---||---||---||---||---||---||---||---||\n')
    print('Insira o código desejado para análise:')
    codigo = input()
    for n in range(len(codigo)):
        if '???' in codigo:
            test1 = codigo.index('???')
            lista1 = codigo[0:test1]
            lista1 = re.sub('[^0-9]','',lista1)
            if lista1 is not '':
                lista1 = list(lista1)
                return1 = lista1.pop()
            else:
                print('false')
                break
            '''
            Retorna o último valor da lista que foi particionada, se houver algum
            valor na lista ira analisar, se não, ira voltar para o loop
            '''
            test2 = codigo.index('???') + 3
            lista2 = codigo[test2:None]
            lista2 = re.sub('[^0-9]','',lista2)
            if lista2 is not '':
                lista2 = list(lista2)
                return2 = lista2.pop(0)
            else:
                print('false')
                break
            '''
            Retorna o último valor da lista que foi particionada, se houver algum
            valor na lista ira analisar, se não, ira voltar para o loop
            '''     
            resul = int(return1) + int(return2)
            #Soma os valores particionados
            if resul == 10:
                print('true\n')
                break
            else:
                codigo = codigo[test2:None]
        else:
            print('false\n')
            break
        
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#
