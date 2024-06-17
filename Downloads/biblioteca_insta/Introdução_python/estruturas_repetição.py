"""introdução  as estruturas de repetição em python
sao elas: for e while"""

# while funciona assim voce passa uma condição e enquanto essa condição nao for verdadeira ele fará algo demonstração

aux = 10
while aux > 0:
    print(f"{aux} - 1")  # imprime o valor o do aux atual - 1
    aux = aux - 1
    # enquanto o aux for maior que zero ele faz aux - 1

print(aux)  # informa o valor do aux quando o loop de repetição acaba

# outro exemplo
while (
    aux < 10
):  # aqui eu faço o oposto do loop anterior agora eu aumento o aux ate chegar a 10
    print(f"{aux} + 1")
    aux = aux + 1

print(aux)

# o que o codigo faz dentro do loop pode ser qualquer coisa voce que escolhe

"""introduzindo as listas
lista é um tipo de variavel, essa variavel guarda mais de um valor ao mesmo tempo"""

lista_jogos = [
    "mortal kombat",
    "GTA",
    "Outlast",
    "FIFA",
    "minecraft",
]  # aqui eu tenho uma lista de jogos, cada elemento deve ser separado por vírgula

lista_mista = [
    20,
    27,
    "vitoria",
    4.5,
    18,
    True,
]  # aqui eu tenho um lista com elementos de tipos diferentes aqui tem int, float, string e boleano

# os elementos da lista tem posições
# em lista_jogos
# mortal kombat esta na posição 0
# GTA esta na posiçao 1
# Outlast esta na posição 2 e assim por diante

print(lista_jogos[4])  # aqui eu imprimo o elemento da posição 4 qual vai ser?

"""introdução a estrutura de repetição for"""

for jogo in lista_jogos:
    print(jogo)  # a variavel jogo recebe quanda item da lista_jogos um de cada vez

for itens in lista_mista:
    print(itens)  # aqui eu imrimo cada item de lista_mista


"""Agora faça esses exercicios para praticar os conceitos introduzidos nesse arquivo

1- faça um loop que multiplique 2  com todos os numeros de 0 a 10 (tabuada do 2)

2- faça uma lista de itens da sua preferencia, e imprima os elementos de tras para frente exemplo se tiver 10 elementos imprima o elemento 9, 8, 7 assim por diante ate o elemento 0

3- faça uma while que imprima os numeros pares de 0 a 20 dica: imprima os numero de dois em dois"""
