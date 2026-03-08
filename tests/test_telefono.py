import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validadores.telefono import validar_telefono

class TestValidadorTelefono:
    
    def test_telefonos_validos_con_codigo_pais(self):
        """Teléfonos con código de país +502"""
        assert validar_telefono("+50231234567") == True
        assert validar_telefono("50231234567") == True
        assert validar_telefono("+50251234567") == True
        assert validar_telefono("50261234567") == True
    
    def test_telefonos_validos_nacionales(self):
        """Teléfonos sin código de país (asume nacional)"""
        assert validar_telefono("31234567") == True
        assert validar_telefono("41234567") == True
        assert validar_telefono("51234567") == True
        assert validar_telefono("61234567") == True
        assert validar_telefono("21234567") == True  # Fijo
    
    def test_telefonos_con_formato_variado(self):
        """Diferentes formatos con espacios/guiones"""
        assert validar_telefono("+502 3123 4567") == True
        assert validar_telefono("502-4123-4567") == True
        assert validar_telefono("5123-4567") == True
    
    def test_telefonos_invalidos(self):
        """Números inválidos"""
        assert validar_telefono("+5021234567") == False    # 7 dígitos
        assert validar_telefono("+502123456789") == False  # 9 dígitos
        assert validar_telefono("1234") == False           # Demasiado corto
        assert validar_telefono("+50312345678") == False   # Código El Salvador
    
    def test_primer_digito_invalido(self):
        """Primer dígito no permitido (1,7,8,9,0)"""
        assert validar_telefono("12345678") == False   # 1 no es válido
        assert validar_telefono("72345678") == False   # 7 no es válido
        assert validar_telefono("02345678") == False   # 0 no es válido
