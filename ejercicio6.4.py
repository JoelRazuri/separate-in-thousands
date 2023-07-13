"""
    Escribir una función que reciba una cadena que contiene un largo número entero
    y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
    '1234567890', debe devolver '1.234.567.890'.
"""


def separacion_en_miles(numero):
    # Recibe una cadena que contiene un largo número entero y devuelve una cadena con el número y las separaciones de miles.

    cadena_reflejo = numero[::-1]
    lista_reflejo = []

    for i in range(len(numero)):

        if i%3==0 and i!=0:
            lista_reflejo.append(".")
        
        lista_reflejo.append(cadena_reflejo[i])
    
    cadena_reflejo = "".join(lista_reflejo)
    numero_miles = cadena_reflejo[::-1]

    print(numero)
    print(numero_miles)


separacion_en_miles("1234567890")
separacion_en_miles("72180947561923")