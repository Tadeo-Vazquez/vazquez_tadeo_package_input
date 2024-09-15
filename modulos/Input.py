from modulos.validate import *

#creé una sola funcion para decimales como enteros, que al cambiarle un parametro, sabe si validar que el numero es un entero o un decimal

def get_number(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int, numero_verificar:str = None) -> int|None:
    #creamos un bucle para preguntar si queremos verificar un flotante o un entero y hasta que no se ingrese bien el dato no corta
    numero_verificar = input("Verificar un numero entero o decimal (ingresar entero/decimal): ")
    while numero_verificar != "entero" and numero_verificar != "decimal":
        print("Dato ingresado incorrectamente")
        numero_verificar = input("Verificar un numero entero o decimal (ingresar entero/decimal): ")
    while reintentos > 0:
        numero_ingresado = input(mensaje)
        resultado = validate_int(numero_ingresado,minimo,maximo,numero_verificar)         
        if resultado != None:
            return resultado
        else:
            print(f"{numero_ingresado} no es un número válido o esta fuera del rango")    
            if reintentos > 0:
                print(f"Te quedan {reintentos} reintentos")
                mensaje = mensaje_error
                reintentos -= 1
            else:
                print("Te quedaste sin intentos")
                return None




def get_string(longitud_permitida:int) -> str|None:
    cadena = input("Ingresa una string: ")
    return validate_length(cadena,longitud_permitida)





