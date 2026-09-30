1: questão 
try:
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida.")
    elif idade >= 18:
        print("Pode participar da atividade.")
    else:
        print("Não pode participar da atividade.")

except ValueError:
    print("Digite uma idade válida.")

2: questão 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
quantidade = int(input("Digite a quantidade de notas: "))

if quantidade == 0:
    print("Não é possível dividir por zero.")
else:
    media = (nota1 + nota2) / quantidade
    print("Média:", media)

3: questão 
alunos = ["João", "Maria", "Pedro", "Lucas"]

indice = int(input("Digite o índice do aluno: "))

if indice >= 0 and indice < len(alunos):
    print("Aluno:", alunos[indice])
else:
    print("Índice inválido.")

4: questão 
try:
    preco = float(input("Digite o preço: ").strip())

    quantidade = int(input("Digite a quantidade: "))

    total = preco * quantidade

    print("Valor total:", total)

except ValueError:
    print("Digite valores numéricos válidos.")

5: questão 
try:
    nota = float(input("Digite a nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida.")
    elif nota >= 7:
        print("Aprovado.")
    elif nota >= 5:
        print("Recuperação.")
    else:
        print("Reprovado.")

except ValueError:
    print("Digite uma nota válida.")

6: questão 
senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        print("Senha incorreta.")

if tentativas == 3 and senha != senha_correta:
    print("Número máximo de tentativas atingido.")

7: questão 
cpf = input("Digite o CPF: ").strip()

if len(cpf) == 11 and cpf.isdigit():
    print("Identificador válido.")
else:
    print("Identificador inválido.")

8: questão 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Média:", media)

9: questão 
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 7:
    print("Aprovado.")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")

10: questão 
while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    print("Você digitou:", numero)

print("Programa encerrado.")

