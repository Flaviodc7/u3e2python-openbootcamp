nombre = input(f"Ingrese su nombre:")
peso = float(input(f"Hola {nombre}, ingresa tu peso:"))
altura = float(input(f"Ingresa tu estatura para calcular el IMC:"))
print(peso / (altura ** altura))