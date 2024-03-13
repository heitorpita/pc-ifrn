nome = input()
sf = float(input())
sb = float(input())
comissao = (15 * sb) / 100
total = sf + comissao

print(nome)
print("R$ {:.2f}".format(total))