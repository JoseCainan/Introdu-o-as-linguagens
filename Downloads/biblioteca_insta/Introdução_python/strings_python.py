faturamento = 1200
custo = 700
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")


email = 'josecainan2009@gmail.com'

# tranformar tudo em maiússculo
email = email.upper()
print(email)

# tudo em minusculo
email = email.lower()
print(email)

# buscando um elemento dentro de um texo
position = email.find("@")# isso retorna a posição do elemento buscado
print(position)# -1 quando não encontrar o elemento buscado

# pegando o tamanho do texto
tamanho_text = len(email)
print(tamanho_text)

# pega os elementos da posição position ate a -4
print(email[position:-4])

# agora pega de 1 ate a 10
print(email[1:10])

# substituindo um trecho do texto
novo_email = email.replace('gmail.com', 'hotmail.com')
print(novo_email)


nome = 'lavineg vitoria'

print(nome.capitalize()) #essa função deixa a primeira letra maiúscla e as outras minúsculas
print(nome.title())#essa deixa a primeira de cada palavra maiúscula

position_space = nome.find(" ")#retorna a posição do espaço
primeiro_nome = nome[:position_space]#do começo ate a posição do espaço
segundo_nome = nome[position_space:]#da posição do espaço ate o final

print(f'primeiro nome: {primeiro_nome.capitalize()}')
print(f'Segundo nome: {segundo_nome.capitalize()}')
