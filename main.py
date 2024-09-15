from modulos.Input import get_number
from modulos.Input import get_string



resultado = get_number("Ingrese numero: ", "Reingrese: ", -1000 , 1000000, 5)

if resultado != None:
    print(f"El numero validado fue {resultado}")
else:
    print("No se ingresó un número válido.")


cadena = get_string(10)

print(cadena)