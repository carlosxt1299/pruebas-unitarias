# validators.py
# Funciones para validar formatos: email, NIF/NIE, tarjeta de crédito, SSN, matrícula de coche
import re

def validar_email(email):
    if not isinstance(email, str):
        return False
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(patron, email) is not None



def validar_tarjeta_credito(numero):
    if not isinstance(numero, str):
        return False
    numero = numero.replace(' ', '')
    if not numero.isdigit() or len(numero) < 13 or len(numero) > 19:
        return False
    suma = 0
    alternar = False
    for digito in reversed(numero):
        d = int(digito)
        if alternar:
            d *= 2
            if d > 9:
                d -= 9
        suma += d
        alternar = not alternar
    return suma % 10 == 0


# DPI de Guatemala: 13 dígitos
def validar_dpi(dpi):
    if not isinstance(dpi, str):
        return False
    dpi = dpi.replace(' ', '').strip()
    return dpi.isdigit() and len(dpi) == 13

# Matrícula de Guatemala: varios tipos
# Ejemplos:
#   Particular: P123BBB
#   Comercial: C123BBB
#   Motocicleta: M123BBB
#   Remesas: R123BBB
#   Oficial: O123BBB
#   Diplomática: CD123BBB
#   Antigua: A123BBB
def validar_matricula(matricula):
    if not isinstance(matricula, str):
        return False
    matricula = matricula.upper().replace(' ', '')
    patrones = [
        r"^P\d{3}[A-Z]{3}$",      # Particular
        r"^C\d{3}[A-Z]{3}$",      # Comercial
        r"^M\d{3}[A-Z]{3}$",      # Motocicleta
        r"^R\d{3}[A-Z]{3}$",      # Remesas
        r"^O\d{3}[A-Z]{3}$",      # Oficial
        r"^CD\d{3}[A-Z]{3}$",     # Diplomática
        r"^A\d{3}[A-Z]{3}$",      # Antigua
    ]
    return any(re.match(p, matricula) for p in patrones)
