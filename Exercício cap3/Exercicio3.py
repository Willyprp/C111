#Criando dicionário
estudante = {}

# Entrada de dados
print('Entre com seu nome: ')
nome = input()
estudante['nome'] = nome
print('Entre com sua média: ')
media = input()
estudante['media'] = int(media)

#Verificando situiação final
if estudante['media'] >= 60:
    estudante['situação final'] = 'AP'
else:
    estudante['situação final'] = 'RP'

print(estudante)
