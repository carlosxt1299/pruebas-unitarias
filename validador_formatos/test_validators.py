# test_validators.py
import pytest
from validators import *

def test_validar_email():
    assert validar_email("test@example.com")
    assert not validar_email("testexample.com")
    assert not validar_email("")
    assert not validar_email(None)
    assert not validar_email("test@.com")



def test_validar_tarjeta_credito():
    assert validar_tarjeta_credito("4539 1488 0343 6467")  # Visa válida
    assert not validar_tarjeta_credito("1234 5678 9012 3456")
    assert not validar_tarjeta_credito("")
    assert not validar_tarjeta_credito(None)
    assert not validar_tarjeta_credito("abcd efgh ijkl mnop")


def test_validar_dpi():
    assert validar_dpi("1234567890123")
    assert not validar_dpi("123456789012")  # Menos de 13 dígitos
    assert not validar_dpi("")
    assert not validar_dpi(None)
    assert not validar_dpi("12345678901AB")

def test_validar_matricula():
    # Ejemplos válidos de Guatemala
    assert validar_matricula("P123BBB")      # Particular
    assert validar_matricula("C456XYZ")      # Comercial
    assert validar_matricula("M789QWE")      # Motocicleta
    assert validar_matricula("R321ASD")      # Remesas
    assert validar_matricula("O654ZXC")      # Oficial
    assert validar_matricula("CD111QAZ")     # Diplomática
    assert validar_matricula("A222WSX")      # Antigua
    # Casos inválidos
    assert not validar_matricula("1234ABC")  # Formato antiguo
    assert not validar_matricula("P12ABCD")  # Demasiados caracteres
    assert not validar_matricula("")
    assert not validar_matricula(None)
    assert not validar_matricula("P1234BBB") # Demasiados dígitos
