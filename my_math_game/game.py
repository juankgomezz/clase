# Operaciones aritméticas básicas

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        return None

def power(num_1, num_2):
    return num_1 ** num_2

def modulo(num_1, num_2):
    return num_1 % num_2

# Juego de operaciones aritméticas

def game():
    score = 0
    operations = [add, subtract, multiply, divide, power, modulo]
    operation_names = ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Modulo"]
    points = [1, 1, 2, 2, 4, 4]

    while True:
        print("======== Menu ========")
        print("\n".join(f"{i+1}. {name}" for i, name in enumerate(operation_names)))
        print("0. Exit")
        option = int(input("\nChoose an option: "))

        if option == 0:
            break

        if 1 <= option <= 6:
            num_1 = int(input("Enter first number: "))
            num_2 = int(input("Enter second number: "))
            correct_answer = operations[option-1](num_1, num_2)
            user_answer = float(input("What is your answer? "))

            if user_answer == correct_answer:
                score += points[option-1]
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", correct_answer)
        else:
            print("Invalid option. Please choose a valid operation.")

        print(f"Your current score is: {score}")

    print(f"======== Game Over ========\nYour final score is {score}\nKeep going!")

# Llamar al juego para iniciar
if __name__ == "__main__":
    game()
