#Lista - nome ja fala lista de dados.
nomes = ["Victor", "Marina", "Daniel"];

frutas = ["Pera", "Maça"];

frutas.append("Melancia"); #Adicionar no final.
print(frutas[0]) #Acessar posições

#Tuplas  tipo uma lista mas travado - usado em coordenadas ou cor ou algo assim .
cor = (0 ,0)
print(cor[0])

#Dicionários - pares chave/valor
pessoa_eu = {"nome": "Victor ", "idade": 28}
print(pessoa_eu['nome'])
pessoa_eu["nome"] = "Marina"
print(pessoa_eu['nome'])
print(pessoa_eu.get('altura')) #focar em usar o get mais confiavel e o null retorna None

#Slice funciona em todas estruturas

print(nomes[0:2])

# .sort() ordena
# .pop() remove o ultmo


# Uma lista com 5 filmes/livros que você gosta
filmes = ["Senhor Dos Anéis", "StarWars", "Hobbit", "Harry Potter", "007"]

# Ordene ela com .sort() e imprima
print(filmes)
filmes.sort()
print(filmes)
# Um dicionário representando você: {"nome": ..., "idade": ..., "cidade": ...}
eu = {'nome': 'Victor Lustosa', 'idade': 28, 'cidade' : "Belo Horizonte"}
print(eu.get('nome'))
# Bônus: usando fatiamento, imprima só os 3 primeiros itens da lista de filmes
print(filmes[0:3])