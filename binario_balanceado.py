def decimal_a_binario(n:int) -> str:
    '''
    Requiere: un entero decimal convertible a binario en base 2.
    Devuelve: un string con su respectivo valor binario.
    '''
    res:str = ""
    while n != 0:
        res = str(n % 2) + res
        n = n // 2
    return res

def es_binario_balanceado(n:int) -> bool:
    """
    Requiere: un numero binario en base 2.
    Devuelve: Si es balanceado o no. Es decir, tiene la misma cantidad
    de 0 que 1. En caso de serlo, devuelve True de lo contrario, False.
    """
    binario:str = decimal_a_binario(n)
    x:int = 0
    uno:int = 0
    cero:int = 0
    while x < len(binario):
        if binario[x] == "1":
            uno = uno + 1
        else:
            cero = cero + 1
        x = x + 1
    return uno == cero

def cantidad_binarios_balanceados_entre(n:int, m:int) -> int:
    '''
    Requiere: Dos valores en los cuales se buscara un binario balanceado entre ellos.
    Devuelve: La cantidad de binarios balanceados (si es que hay, de lo contrario devolvera 0).
    '''
    res:int = 0
    while n <= m:
        if es_binario_balanceado(n) == True:
            res = res + 1
        n = n + 1
    return res

def siguiente_binario_balanceado(n:int) -> int:
    '''
    Requiere: un valor no binario.
    Devuelve: El siguiente valor no binario pero que al convertirlo sea balanceado,
    mas cercano a el (de forma ascendente)
    '''
    res:int = n + 1
    while es_binario_balanceado(res) != True:
        res = res + 1
    return res
    
def anterior_binario_balanceado(n:int) -> int:
    '''
    Requiere: un valor no binario.
    Devuelve: El siguiente valor no binario pero que al convertirlo sea balanceado,
    mas cercano a el (de forma descendente y de no haberlo, devuelve 0.)
    '''
    res:int = n - 1
    while es_binario_balanceado(res) != True and res >= 3:
        res = res - 1
    return res

def binario_balanceado_mas_cercano(n:int) -> int: 
    '''
    Requiere: un valor no binario.
    Devuelve: El siguiente valor no binario pero al convertirlo sea balanceado
    mas cercano a el (en caso de que esten a mismas distancias del incial, se prioriza el mayor).
    '''
    sig:int = siguiente_binario_balanceado(n) - n
    ant:int = n - anterior_binario_balanceado(n)
    res:int = 0
    if es_binario_balanceado(n) == True:
        return n
    elif sig < ant:
        res = siguiente_binario_balanceado(n)
    elif sig > ant:
        res = anterior_binario_balanceado(n)
    elif sig == ant:
        res = siguiente_binario_balanceado(n)
    return res
            
#Definir también las funciones auxiliares que se consideren necesarias.
