# Condicionais:
# estruturas do Python que permitem executar trechos de código diferentes dependendo de condições verdadeiras ou falsas
# usam if, elif e else para testar valores e escolher o caminho a seguir        

idade = 18;

if idade >= 18:
    print("Você é maior de idade.");
else:
    print("Você é menor de idade!");

nota = 61

if nota < 60:
    print(f"Você não alcançou a nota suficiente para passar nota atual: {nota}")
elif nota == 60:
    print(f"Sua nota ficou na media para ser aprovado, nota atual: {nota} ")
else:
    print(f"Parabens Foi aprovado, nota atual: {nota}")

faculdade = True
trabalhando = True

if trabalhando and faculdade:
    print("Aluno é estagiário")
elif trabalhando and not faculdade:
    print("Trabalhador")
elif faculdade and not trabalhando:
    print("Estudante")
else:
    print("Desempregado")

#Praticando loops

numeros = [1,2,3,4,5,6,7,8,9,10]

for number in numeros:
    if number % 2 == 0:
        print('Even')
    else:
        print("Odd")

count = 0

while count <= 15:
    print(f'Contador: {count}')
    count += 1

# Exercício 1
# Peça a idade do usuário e diga se ele é "Menor de idade", 
# "Adulto" (18 a 59) ou "Idoso" (60+).

idade = int(input("Qual sua idade?"))
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade <= 59:
    print("Você já é um adulto")
else:
    print("Você é um vovôzinho")

# Exercício 2
# Peça um número e diga se ele é par ou ímpar (use o operador %).

numeros = [1,2,3,4,5,6,7,8,9,10]

for number in numeros:
    if number % 2 == 0:
        print('Even')
    else:
        print("Odd")

# Exercício 3
# Peça duas notas (0 a 10) e calcule a média. 
# Se a média for >= 7, imprima "Aprovado"; 
# se estiver entre 5 e 6.9, imprima "Recuperação"; 
# abaixo de 5, imprima "Reprovado".
nota1 = int(input("Digite a 1ª nota."))
nota2 = int(input("Digite a 2ª nota."))
media = round((nota1 + nota2) / 2, 2)
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print('Recuperação')
else:
    print("Reprovado")
    

# Exercício 4
# Peça um número e diga se ele é positivo, negativo ou zero.
numero = int(input("Número por favor."));
if numero > 0:
    print("Positívo")
elif numero == 0:
    print("Zero")
else:
    print("Negativo")

# Exercício 5
# Crie variáveis "tem_carteira" (True/False) e "idade". 
# Diga se a pessoa pode dirigir: só pode se tiver 18+ E tiver carteira.
tem_carteira = False
idade = 18
if idade >= 18 and tem_carteira:
    print("Pode dirigir!")
elif (idade >= 18 and not tem_carteira) or (idade < 18 and tem_carteira):
    print("Não pode dirigir");
else:
    print("Você pode ter cartereira mesmo?")
