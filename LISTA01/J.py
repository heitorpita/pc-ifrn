
valor = int(input())
print(valor)
n100 = valor // 100
print(f"{n100} nota(s) de R$ 100,00")
valor %=100
n50 = valor // 50 
print(f"{n50} nota(s) de R$ 50,00")
valor %= 50
n20 = valor // 20
print(f"{n20} nota(s) de R$ 20,00")
valor %= 20
n10 = valor // 10
print(f"{n10} nota(s) de R$ 10,00")
valor %= 10
n5 = valor // 5
print(f"{n5} nota(s) de R$ 5,00")
valor %= 5
n2 = valor // 2
valor %= 2
print(f"{n2} nota(s) de R$ 2,00")
n1 = valor
print(f"{n1} nota(s) de R$ 1,00")

