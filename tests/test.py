import re
import math
import unittest

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

def calculate(expression: str):
    # Limpiar la expresión de espacios en blanco
    expression = expression.replace(" ", "")

    # Verificar si la expresión está vacía o tiene solo espacios en blanco
    if not expression:
        raise ValueError("La entrada no puede estar vacía")

    # Expresión regular para validar caracteres permitidos
    if not re.match(r'^[\d+\-*/(). ]+$', expression):
        raise ValueError("Caracter no soportado en la expresión")

    try:
        # Evaluar la expresión utilizando eval, pero primero verificar la sintaxis
        resultado = eval(expression)

        # Redondear los resultados a una precisión de 10 decimales para manejar los errores de precisión
        if isinstance(resultado, float):
            resultado = round(resultado, 10)

    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis inválida en la expresión")
    except NameError:
        raise ValueError("Caracter no soportado en la expresión")
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")

    return resultado

# Ejemplo de uso
if __name__ == "__main__":
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
            resultado = calculate(entrada)
            print(f"Resultado: {resultado}")

        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        except SyntaxError:
            print("Error: Sintaxis inválida.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese una operación válida.")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor, contacte al soporte técnico.")