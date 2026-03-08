import re

def validar_telefono(telefono: str) -> bool:
    """
    Valida un número de teléfono guatemalteco.
    
    Formatos aceptados:
        - +50212345678
        - 50212345678
        - 12345678 (asume que es nacional)
        - con espacios o guiones
    """
    if not telefono or not isinstance(telefono, str):
        return False
    
    # Eliminar espacios y guiones
    telefono_limpio = re.sub(r'[\s\-]', '', telefono)
    # Quitar paréntesis
    telefono_limpio = telefono_limpio.replace('(', '').replace(')', '')
    # Quitar el prefijo + si existe
    if telefono_limpio.startswith('+'):
        telefono_limpio = telefono_limpio[1:]
    # Quitar prefijo 502 si existe
    if telefono_limpio.startswith('502'):
        telefono_limpio = telefono_limpio[3:]
    # Deben ser exactamente 8 dígitos
    if len(telefono_limpio) != 8 or not telefono_limpio.isdigit():
        return False
    primer_digito = telefono_limpio[0]
    # Móviles: 3,4,5,6; Fijos: 2
    return primer_digito in ['2', '3', '4', '5', '6']
