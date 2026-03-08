import re

def validar_nit(nit: str) -> bool:
    """
    Valida un NIT guatemalteco.
    
    Args:
        nit: String con el NIT (puede incluir o no guión)
    
    Returns:
        True si es válido, False en caso contrario
    
    Ejemplos válidos:
        - "3602978-5"
        - "36029785"
        - "576937-K"
        - "576937k"
    """
    if not nit or not isinstance(nit, str):
        return False
    
    # Limpiar espacios y convertir a mayúsculas
    nit = nit.strip().upper()
    
    # Patrón: dígitos, opcionalmente guión, y dígito verificador (número o K)
    patron = r'^(\d+)-?([0-9K])$'
    match = re.match(patron, nit)
    
    if not match:
        return False
    
    numeros = match.group(1)
    verificador = match.group(2)
    
    # Convertir verificador a número (K = 10)
    try:
        verificador_num = 10 if verificador == 'K' else int(verificador)
    except ValueError:
        return False
    
    # Calcular dígito verificador esperado
    suma = 0
    longitud = len(numeros)
    
    for i, digito in enumerate(numeros):
        # Posición: de derecha a izquierda, empezando en 2
        posicion = longitud - i + 1
        suma += int(digito) * posicion
    
    residuo = suma % 11
    esperado = (11 - residuo) % 11
    
    return esperado == verificador_num
