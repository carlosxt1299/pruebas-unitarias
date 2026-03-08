import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validadores.nit import validar_nit

class TestValidadorNIT:
    
    def test_nits_validos_con_guion(self):
        """NITs válidos con formato estándar"""
        assert validar_nit("3602978-5") == True
        assert validar_nit("576937-K") == True
    
    def test_nits_validos_sin_guion(self):
        """NITs válidos sin guión"""
        assert validar_nit("36029785") == True
        assert validar_nit("576937K") == True
    
    def test_nit_con_k_minuscula(self):
        """K minúscula debe ser válida"""
        assert validar_nit("576937-k") == True
    
    def test_nit_con_digito_verificador_incorrecto(self):
        """Dígito verificador incorrecto"""
        assert validar_nit("3602978-6") == False
    
    def test_nit_formato_invalido(self):
        """Formatos que no cumplen el patrón"""
        assert validar_nit("3602978-55") == False  # Verificador de 2 dígitos
        assert validar_nit("3602978") == False     # Sin verificador
        assert validar_nit("ABC123") == False      # Letras donde no van
    
    def test_casos_borde(self):
        """Casos límite"""
        assert validar_nit("") == False
        assert validar_nit(None) == False
        assert validar_nit("   ") == False
        assert validar_nit("-5") == False
