# 1.Escreva uma função validar_cpf(cpf) que recebe uma string e retorna True/False 
# (só a validação de formato, sem dígito verificador ainda).
def cpfValidator(cpf: str) -> bool :
    if len(cpf) != 14:
        return False;
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False;
    numero = cpf.replace('.','').replace('-', '')
    return numero.isdigit();

print(cpfValidator('568.056.845-78'))
print(cpfValidator('568.056.845-7a'))
print(cpfValidator('568.056.84571'))

# 2. Pratique *args e **kwargs: crie uma função resumo(**dados) que recebe pares chave-valor e imprime um relatório formatado.
def resumo(**kwargs: object) -> None:
    for chave, valor in kwargs.items():
        print(f'Chave: {chave} -  Valor: {valor}')
resumo(nome='Victor', idade= 28, profissao='Cientista da Computação')

def mediaGeral(**kwargs: object) -> float:
    total = 0;
    qtd = 0;
    media = 0;
    for chave, valor in kwargs.items():
        qtd += 1;
        total += valor;
    media = total / qtd;
    return media;
print(mediaGeral(matematica= 6, portugues=3, fisica=8, geografia=7, historia=5 ))
# 3. Funções como cidadãos de primeira classe: crie uma lista de funções (operacoes = [soma, subtracao, multiplicacao]) e 
# itere aplicando cada uma sobre dois números.
def soma(a: float, b: float) -> float:
    return a + b;
def subtracao(a: float, b: float) -> float:
    return a - b;
def multiplicacao(a: float, b: float) -> float:
    return a * b;
operacoes = [soma, subtracao, multiplicacao];
print(operacoes[0](2,3));
print(operacoes[1](4,3));
print(operacoes[2](0,3));
for op in operacoes:
    print(op(2,1))
# 4. Uso de Class Fazer uma classe contaBancaria qeu tem depositar sacar... com seus validadores
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular  = titular
        self.saldo = saldo;
    

    
    def depositar(self, valor):
        self.saldo += valor
        return f'Deposito realizado com sucesso, saldo atual: {self.saldo}'
    
    def sacar(self, valor):
        if valor > self.saldo:
            return f'Valor muito alto, saldo atual = {self.saldo}'
        if valor <= 0:
            return 'Valor invalido tente um numero maior que 0'
        
        self.saldo = self.saldo - valor;
        return f'Valor - {valor} retirado com sucesso, saldo atual {self.saldo}'

conta = ContaBancaria("Victor", 100)
print(conta.depositar(50))
print(conta.sacar(200))
print(conta.sacar(30))
print(conta.saldo)