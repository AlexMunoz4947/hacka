class Calculadora2:

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

            # Realizar la operación basada en el operador
            if operacion == '+':
                resultado = calculadora.sumar(num1, num2)
            elif operacion == '-':
                resultado = calculadora.restar(num1, num2)
            elif operacion == '*':
                resultado = calculadora.multiplicar(num1, num2)
            elif operacion == '/':
                resultado = calculadora.dividir(num1, num2)
            else:
                print("Operación no soportada. Por favor, use '+', '-', '*', '/'")
                continue

            print(f"Resultado: {resultado}")

        except Exception as e:
            print(f"Error: {e}. Por favor, ingrese una operación válida.")