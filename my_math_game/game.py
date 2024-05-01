# Operaciones aritméticas básicas

def suma(num_1, num_2):
    return num_1 + num_2

def resta(num_1, num_2):
    return num_1 - num_2

def multiplicacion(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        return None

def potenciacion(num_1, num_2):
    return num_1 ** num_2

def modulo(num_1, num_2):
    return num_1 % num_2

# Juego de operaciones aritméticas

def game():
    score = 0
    operations = [suma, resta, multiplicacion, division, potenciacion, modulo]
    operation_names = ["suma", "resta", "Multiplicacion", "Division", "potenciacion", "Modulo"]
    points = [1, 1, 2, 2, 4, 4]

    while True:
        print("======== Menu ========")
        print("\n".join(f"{i+1}. {name}" for i, name in enumerate(operation_names)))
        print("0. salir")
        option = int(input("\nElige una opcion: "))

        if option == 0:
            break

        if 1 <= option <= 6:
            num_1 = int(input("ingresa el primer numero: "))
            num_2 = int(input("ingrese el segundo numero: "))
            correct_answer = operations[option-1](num_1, num_2)
            user_answer = float(input("cual es tu respuesta? "))

            if user_answer == correct_answer:
                score += points[option-1]
                print("Correcto!")
            else:
                print("incorrecto. la respuesta correcta es:", correct_answer)
        else:
            print("opcion invalida. Por favor elige una opcion valida.")

        print(f"Tu puntuacion actual es: {score}")

    print(f"======== Game Over ========\nTu puntaje final es {score}\nsigue intentando!")

# Llamar al juego para iniciar
if __name__ == "__main__":
    game()
