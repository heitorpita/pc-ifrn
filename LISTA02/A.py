nome = (input())
horas = int(input())
pagas = float(input())

salario = horas * pagas
print(nome)
print(f"{salario:.2f}")




nome = input()
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = horas_trabalhadas * valor_hora
print(nome)
print("R$ {:.2f}".format(salario))
