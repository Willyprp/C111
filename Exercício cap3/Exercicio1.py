#Criando Lista
colocacoes = ['Real Madrid', 'Bayern München', 'PSG', 'Barcelona', 'Chelsea']

# Exercício 1a:
print("Os 3 primeiros colocados são: ")
print(colocacoes[0])
print(colocacoes[1])
print(colocacoes[2])

# Exercício 1b:
print("O penúltimo colocado é: ")
print(colocacoes[-2])
print("O último colocado é: ")
print(colocacoes[-1])

# Exercício 1c:
print("Lista em ordem alfabética: ")
colocacoes.sort()
print(colocacoes)

# Exercício 1d:
colocacoes = ['Real Madrid', 'Bayern München', 'PSG', 'Barcelona', 'Chelsea']
print("O Barcelona está na posição: ")
print(1 + colocacoes.index('Barcelona'))
