# 2 listas que são iterables
funcionario = ['Maria','Jose','Antonio','João','Francisco','Ana','Luiz','Paulo','Carlos','Manoel','Pedro','Francisca','Marcos','Gustavo','Gabriel','Renan','Carol','Eduarda']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 450, 400, 300, 120, 90, 80, 70]

# o range tem um função de começar e terminar em valores especificos, como nos exemplos a baixo
print("Classe A: 10% melhor")
for i in range(0,2):
    print(f"{funcionario[i]} vendeu = {vendas[i]}")

print("\nClasse B: 80% mantem/buscam melhorar")
for i in range(2,15):
    print(f"{funcionario[i]} vendeu = {vendas[i]}")

print("\nClasse C: 10% pior")
for i in range(16,18):
    print(f"{funcionario[i]} vendeu = {vendas[i]}")

#ele vai ate o 10, mas n printa por seguir a logica do "se for igual, pare"
print('\n-------')
print(range(0,10,2))
for i in range(0,10,2):
    print(i)