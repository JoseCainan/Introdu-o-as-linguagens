# listas

vendas = [ 100, 50, 500, 800, 100, 20, 90, 27]

total_vendas = sum(vendas) #retorna a somma dos elementos da lista
print(total_vendas)

quantidade_vendas = len(vendas)# retorna o tamanho da lista
print(quantidade_vendas)

maior = max(vendas)#retorna o maior valor
menor = min(vendas)#retorna o menor valor

print(f"o maior valor da lista: {maior}\n"
      f"o menor valor: {menor}\n")

lista_produtos = ['ps5', 'xbox', 'nintendo', 'dualsense', 'mortalkombat']

produto = input('qual produt deseja procurar')
produto.lower()#deixa todas as letra minúscula

verifica = produto in lista_produtos
print(verifica)



lista_produtos = ['ps5', 'xbox', 'nintendo', 'dualsense','ps5', 'mortalkombat', 'nintendo']

#adicionando um item na lista
lista_produtos.append('ps4')
print(lista_produtos)

#removendo um item da lista
lista_produtos.remove('ps4')#remove voce passa o nome do item que deseja remover
print(lista_produtos)

lista_produtos.pop(0)#com o pop voce passa posição do item nesse caso o ps5
print(lista_produtos)

#editando o valor de uma lista
preços = [ 100, 50, 500, 800, 100, 20, 90, 27]

preços[0] = 200 #aqui eu altero o 100 para 200
print(preços)

preços[0] = preços[0] * 1.5 # agora eu aumento em 50% o valor de 200
print(preços)

#conferindo quantas vezes um elemento aparece na lista
print(lista_produtos.count('nintendo'))

lista_produtos.sort()#ordena a lista
print(lista_produtos)

lista_produtos.sort(reverse=True)# ordena na ordem decrescente
print(lista_produtos)