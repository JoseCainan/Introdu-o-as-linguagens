dic_produtos = {'mortal kombat': 204, 'gta5': 100, 'cadeira gamer': 1000, 'acer nitro v': 5000}
# cahve = é o nome de cada produto: mortal kombat cadeira gamer, gta5 ...
#valor = é o preço de cada produto: 204, 100, 1000 
#pegadno um elemento 
elemento = dic_produtos['cadeira gamer']
print(elemento)


#editando um elemento
dic_produtos['acer nitro v'] = dic_produtos["acer nitro v"] * 1.5
print(dic_produtos['acer nitro v'])

#quantidade de itens no dicionario
tamanho = len(dic_produtos)
print(tamanho)

#removendo um item
dic_produtos.pop('mortal kombat')
print(dic_produtos)

#adicionando um elmeno
dic_produtos['galaxy book'] = 4800
print(dic_produtos)

# como saber se um item existe no dicionario
""" existem duas formas ou voce verifica se uma chave existe ou voce verifica se um valor exixte
 """

if 'mortal kombat' in dic_produtos:#aqui eu verifico atraves da chave
    print('esse produto existe')
else:
    print('nao existe no produto')


if 5000 in dic_produtos.values():
    print('esse produto existe')
else:
    print('nao existe no produto')


nome_produto = input('informe o nome do produto')
preço_produto = float(input('informe o preço do produto'))

nome_produto = nome_produto.lower()

dic_produtos[nome_produto] = preço_produto

for item in dic_produtos:# cada item é um produto 
    novo_preço = dic_produtos[item] * 1.1 #aqui cada valor de cada produto é multilicado por 1.1
    dic_produtos[item] = novo_preço# agora cada produto rece o novo preço

print(dic_produtos)









