""" Esse é um código de introdução ao python nesse código seram 
apresentados os conceitos básicos """



#printando algo na tela, nesse caso uma mensagem, mas poderia ser uma variável também
print('olá, mundo')

# variáveis são "caixas" que guardam algum tipo de dado
# variáveis em python - alguns dos tipos de variáveis
mensagem = 'Esse é um código de introdução ao python de Cainan.dev' # string são palavras 

numero_int = 18 # int são números do tipo inteiro(não assume valores "quebrados")
numero_float = 20.09 # float são número de valores decimais(ponto flutuante)

boleano = True # boleano só assume dois valores True ou False 


# imprimindo os valores das variáveis 
print(mensagem)
print(numero_int)
print(numero_float)
print(boleano)

#você tambem pode imprimir mais de uma variavel em único print
print(mensagem, numero_float, numero_int, boleano)

#input - o input você usa quando quer receber algum dado ou informação do usuário
seu_nome = input('informe o seu nome por favor')#aqui o que o usuario digitar vai ser guardado na variavel seu_nome

print("Bem vindo, " + seu_nome +"  , esse é o código de introdução ao python")# exemplo de como mesclar mensagem e variavel no mesmo print


# mostrei a diferença de inteiro float boleano e string agora vamos aprender a converter eles de um para o outro 

idade_string = input('informe a sua idade, digite um numero!') # se você nao dizer o tipo de dado no input ele recebe por padrao uma string

idade_int = int(idade_string) #nao converto para float pois idade é melhor tratar como inteiro

laranha_float = float(input('informe quantas laranjas você tem')) #aqui recebo laranja como float

laranja_string = str(laranha_float)#transformando um float em string

#lembrando que para colocar um numero float(decimal) use o ponto no lugar da vírgula

# recebendo dois numero um int e um float e somando eles 
numero_float = float(input('informe um numero '))
numero_int = int(input('informe outro numero'))

soma = numero_float + numero_int

print(soma)



# dica: voce pode comentar o codigo e deixar so a parte que voce quer ver a execução 



''' introduzindo as operações matemáticas e os operadores aritmeticos 
    para somar ou subtrair use + ou - exemplo:'''

soma = 6 + 4 # saída igual a 10
print(soma)

soma = soma + 15 # saída igual a 25
print(soma)
# como a variavel soma esta guardando o valor 10, entao será somado 10 + 15

menos = 15 - 10 #saída igual a 5
print(menos)

menos = menos - 10 #saída igual a -5
print(menos)

# para multiplicar e dividir use * e / respectivamente 
multiplica = 10 * 10 #saída igual a 100
print(multiplica)

divide = multiplica / 25 #saída igual a 4
print(divide)

#você pode fazer operações entre int e float mas nao pode fazer entre string e int ou string e float
#alguns erros de tipos

erro_tipo = '5' + 10 # isso é um erro pois esta somando umas string com inteiro 

erro_tipo2 = '10' + 10.5 # outro erro agora soma de string com float

'''Introdução a estruturas condicionais  If e Elif'''

# ao pé da letra if significa se, exemplo se 10 é menor que 11 faça algo demonstração abaixo

num = int(input('informe um numero inteiro'))
aux = 11

if num < aux: # aqui eu verifico se o numero que vc informou é menor que aux(11)
    print('num é menor que aux') # se for menor que aux a mensagem será exibida
elif num > aux: #aqui verifico se num é maior que aux(11)
    print('num é maior que aux') #mensagem exibida se for maior que aux
elif num == aux: # aqui eu verifico se num e aux sao iguais
    print('num e aux sao iguais')
    
#primeiro a condição do if depois uma intrução do que fazer se a condição for verdadeira
num1 = 10
num2 = 10

if num1 != num2:
    print('os numeros sao diferentes')
else:
    print('os numero sao iguais')

#aqui eu verifico se o numero sao diferente com o if, como essa condição é falsa ele executa a segunda ação, no else

# o else é a ação que sera executada se a condição do if for falsa



'''Faça esses 3 exercícios para você praticar os conceitos apresentados nesse código

1- faça um codigo que receba dois numeros do usuario e verifique se o primeiro é maior que o segundo

2- faça um codigo que receba tres numeros do usuario e retorne a soma dos tres numeros e a multiplicação dos tres 

3- faça um codigo que receba dois numero, mas em formato de string, depois converta eles para float e divida o primeiro pelo segundo'''