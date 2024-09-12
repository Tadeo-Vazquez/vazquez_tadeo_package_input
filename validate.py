def validate_int(numero:str, minimo:int,maximo:int, numero_verificar:str):
    # Si el parámetro numero_verificar es "entero", intentamos validar el número como entero
    # Si se valida y esta dentro de los límites retorna el numero y si no, retorna None
    if numero_verificar == "entero":
        try:
            numero = int(numero)
            if numero >= minimo and numero <= maximo:
                return numero
            else:
                return None
        except ValueError:
            return None

    # Si el parámetro numero_verificar es "decimal", intentamos validar el número como decimal
    # Si se valida y esta dentro de los límites retorna el numero y si no, retorna None
    elif numero_verificar == "decimal":
        try:
            numero = float(numero)
            if numero >= minimo and numero <= maximo:
                return numero
            else:
                return None
        except ValueError:
            return None


#funcion que verifica si una cadena esta dentro del límite de caracteres permitidos
def validate_length(cadena:str,longitud:int):
    if len(cadena) > longitud:
        return "La cadena es muy larga"
    else:
        return "La cadena es válida"