def sumar(a, b):
    return a + b

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese la operación
        entrada = input("Escriba la operación (por ejemplo, 2 + 2) o 'c' para borrar: ")

        # Permitir al usuario borrar la operación
        if entrada.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            # Dividir la entrada en los componentes de la operación
            partes = entrada.split()
            num1 = float(partes[0])
            operacion = partes[1]
            num2 = float(partes[2])

            # Realizar la operación de suma si el operador es '+'
            if operacion == '+':
                resultado = sumar(num1, num2)
                print(f"Resultado: {resultado}")
            else:
                print("Operación no soportada. Por favor, use '+'.")
        except Exception as e:
            print(f"Error: {e}. Por favor, ingrese una operación válida.")