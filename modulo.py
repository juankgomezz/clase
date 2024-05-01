def modulo(num1, num2):
    if num2 == 0:
        print("Error: División por cero no es permitida en la operación de módulo")
        return None
    result = num1 % num2
    print(f'El módulo de {num1} dividido por {num2} es {result}')
    return result
