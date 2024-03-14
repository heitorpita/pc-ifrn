d = int(input())
v = int(input())
temp = d / v
horas = int(temp)
min = (temp - horas) * 60 
print(f"{horas:02d}:{int(min):02d}")