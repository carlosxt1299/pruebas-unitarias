import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validadores.dpi import validar_dpi

class TestValidadorDPI:
    def test_dpi_valido(self):
        assert validar_dpi("1234567890101") == True
        assert validar_dpi("1234 56789 0101") == True
        assert validar_dpi(" 1234 56789 0101 ") == True

    def test_dpi_invalido_longitud(self):
        assert validar_dpi("12345678901") == False  # 11 dígitos
        assert validar_dpi("12345678901010") == False  # 14 dígitos

    def test_dpi_invalido_no_numerico(self):
        assert validar_dpi("1234A67890101") == False
        assert validar_dpi("ABCDEFGHIJKLM") == False

    def test_dpi_vacio_o_none(self):
        assert validar_dpi("") == False
        assert validar_dpi(None) == False
        assert validar_dpi("   ") == False
