# converter temperatuaentre Celsius, Fahrenheit e Kelvin

temp = float(input("Digite a temperatura: "))
origem = input("Digite a origem da temperatura (C, F ou K): ").upper()
destino = input("Digite o destino da temperatura (C, F ou K): \n").upper()

if origem == "C" and destino == "F":
    temp_convertida = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    temp_convertida = temp + 273.15
elif origem == "F" and destino == "C":
    temp_convertida = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    temp_convertida = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    temp_convertida = temp - 273.15
elif origem == "K" and destino == "F":
    temp_convertida = (temp - 273.15) * 9/5 + 32
else:
    print("Origem e destino inválidos.")
print(f"A temperatura convertida é: {temp_convertida}°{destino}")    