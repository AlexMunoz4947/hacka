class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

# Ejemplo de uso
if _name_ == "_main_":
    calculadora = Calculadora()
    while True:
        # Solicitar al usuario que ingrese la operación
        entrada = input("Escriba la operación (por ejemplo, (4 + 4) * 2) o 'c' para borrar: ")

        # Permitir al usuario borrar la operación
        if entrada.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            # Evaluar la expresión completa utilizando eval
            resultado = eval(entrada)
            print(f"Resultado: {resultado}")

        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        except Exception as e:
            print(f"Error: {e}. Por favor, ingrese una operación válida.")