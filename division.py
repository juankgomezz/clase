def divide(num_1, num_2):
    if num_2 == 0:
        print("Error: División por cero no permitida")
        return None
    result = num_1 / num_2
    print(f'{num_1} / {num_2} is equal to {result}')
    return result
