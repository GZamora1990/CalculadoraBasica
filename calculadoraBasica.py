while True:
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    operador = input("Operador aritmetico (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operador == "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operador == "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Error: División por cero no permitida.")
            continue
    else:
        print("Operador no válido.")
        continue

    while True:
        condicion = input("Desea volver a operar con el resultado? (s/n): ").lower()
        if condicion == "s":
            num2 = num2
            reoperar = resultado + num2
            resultado = reoperar
            print(f"Nuevo resultado: {reoperar}")
        else:
            continuar = input("Desea finalizar? (s/n): ").lower()
            if continuar == "s":
                break
            else:
                break
    if continuar == "s":
        break
