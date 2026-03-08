import re

def validar_dpi(dpi: str) -> bool:
    """
    Valida un DPI guatemalteco.
    
    Formato: 13 dígitos, puede tener espacios.
    Ejemplo válido: "1234 56789 0101" o "1234567890101"
    """
    if not dpi or not isinstance(dpi, str):
        return False
    
    # Eliminar espacios y verificar que sea numérico
    dpi_limpio = re.sub(r'\s+', '', dpi)
    
    # Deben ser exactamente 13 dígitos
    if not dpi_limpio.isdigit() or len(dpi_limpio) != 13:
        return False
    
    # Validación adicional: el último dígito podría ser un verificador
    # (Según documentación de SAT, aunque no hay algoritmo público)
    
    return True
