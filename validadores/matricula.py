import re

def validar_matricula(matricula: str) -> bool:
    """
    Valida una matrícula de vehículo guatemalteca.
    
    Formatos:
        - Estándar: P123ABC (particular)
        - Motos: M123ABC
        - Diplomáticas: CD-123
        - Cruz Roja: CRG-123
    """
    if not matricula or not isinstance(matricula, str):
        return False
    
    matricula = matricula.strip().upper()
    
    # Patrones de validación
    patrones = [
        # Formato estándar: letra + 3 números + 3 letras
        r'^([PACUMO])\d{3}[A-Z]{3}$',
        
        # Motocicletas (formato especial)
        r'^M\d{3}[A-Z]{3}$',
        
        # Diplomáticos: CD/CC/MI + guión + 1-3 números
        r'^(CD|CC|MI)-\d{1,3}$',
        
        # Cruz Roja: CRG + guión + 3 números
        r'^CRG-\d{3}$',
        
        # Remolque: TC + guión + 3 números
        r'^TC-\d{3}$',
        
        # Placas antiguas (2004-2021): letra + 3 números + 3 letras
        r'^[A-Z]\d{3}[A-Z]{3}$'
    ]
    
    return any(re.match(patron, matricula) for patron in patrones)


def obtener_tipo_vehiculo(matricula: str) -> str:
    """Devuelve el tipo de vehículo según la matrícula"""
    if not validar_matricula(matricula):
        return "Formato inválido"
    
    matricula = matricula.upper()
    
    # Mapeo de prefijos
    tipos = {
        'P': 'Particular',
        'A': 'Alquiler (Taxi)',
        'C': 'Comercial/Carga/Extraurbano',
        'U': 'Urbano (Transporte público)',
        'M': 'Motocicleta',
        'O': 'Oficial',
        'CD': 'Cuerpo Diplomático',
        'CC': 'Cuerpo Consular',
        'MI': 'Misión Internacional',
        'CRG': 'Cruz Roja',
        'TC': 'Remolque'
    }
    
    # Extraer prefijo
    if '-' in matricula:
        prefijo = matricula.split('-')[0]
    else:
        prefijo = matricula[0]
    
    return tipos.get(prefijo, 'Tipo desconocido')
