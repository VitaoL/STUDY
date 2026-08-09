# rotudo que guarda algum dado.
#Não precisa declarar o tipo da variável
# Isso significa que o Python é uma linguagem de tipagem dinâmica.
nome = "Marina";
idade = 28;
altura = 1.66;
trabalhando = True;

#typeof em python é type()

print(type(nome));
print(type(altura));

# Podemos reatribuir valores

print(nome);
nome = "Marina Pena";
print(nome);

# Juntar texto com variaveis

print(f"O nome da minha namorada é {nome} e ela tem {idade} anos. Hoje é -> 16/08/2026 ");

#Captar dados  input() sempre retorna string se quiser numero converta - int()
# nome = input("Qual seu nome? ")   # input() sempre retorna string



# Exercício 1
# Crie uma variável com seu nome e outra com sua idade, 
# e imprima uma frase usando as duas (use f-string).

nome = "Victor Lustosa";
idade = 28;
print(f"Meu nome é {nome} e tenho {idade} anos.")


# Exercício 2
# Crie duas variáveis numéricas (num1 e num2) e imprima 
# a soma, subtração, multiplicação e divisão entre elas.

numero1 = 10;
numero2 = 5;
soma = numero1 + numero2;
subtracao = numero1 - numero2;
subtracao_negativa = numero2 - numero1;
multiplicacao = numero1 * numero2;
divisao = numero1 / numero2;
divisao_errada = numero2 / numero1;
divisao_inteiro = numero1 // numero2;
resto = numero2 % numero1;

print(f"Numeros : {numero1}  <--> {numero2}");
print(f"soma: {soma}");
print(f"subtracao: {subtracao}");
print(f"subtracao negativo {subtracao_negativa}");
print(f"multiplicacao: {multiplicacao}");
print(f"divisao: {divisao}");
print(f"divisao errada: {divisao_errada}")
print(f"divisao inteira: {divisao_inteiro}");
print(f"resto: {resto}")

# Exercício 3
# Peça o nome do usuário com input() e imprima 
# "Olá, seu_nome! Seja bem-vindo(a)."
nome = input("Qual o seu nome?");
print(f"Olá, {nome}! Seja bem-vindo(a).")


# Exercício 4
# Peça a idade do usuário com input(); 
# e calcule/imprima em que ano ele nasceu, considerando o ano atual.

idade = int(input("Qual a sua idade?"));
ano_atual = 2026;
ano_nascimento = ano_atual - idade;
print(f"Se voce tem {idade}, quer dizer que no nasceu no ano de {ano_nascimento}");


# Exercício 5
# Crie uma variável "preco" com um valor decimal e uma variável 
# "quantidade" com um valor inteiro. Calcule e imprima o total da compra.

preco = 10.30;
quantidade = 3;

total = quantidade  * preco;
total_arredondado = round(total, 2);
print(f"Total da compra: {total_arredondado} ");
print(f"Total de compra: {total:.2f}")
