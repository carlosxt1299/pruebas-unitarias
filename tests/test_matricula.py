import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validadores.matricula import validar_matricula, obtener_tipo_vehiculo

class TestValidadorMatricula:
    
    def test_matriculas_particular_validas(self):
        """Matrículas de vehículo particular"""
        assert validar_matricula("P123ABC") == True
        assert validar_matricula("P123ABC") == True
        # Con minúsculas
        assert validar_matricula("p123abc") == True
    
    def test_matriculas_comerciales_validas(self):
        """Matrículas de vehículo comercial"""
        assert validar_matricula("C456XYZ") == True
    
    def test_matriculas_diplomaticas_validas(self):
        """Matrículas diplomáticas"""
        assert validar_matricula("CD-123") == True
        assert validar_matricula("CC-45") == True
        assert validar_matricula("MI-7") == True
    
    def test_matriculas_cruz_roja_validas(self):
        """Matrículas de Cruz Roja"""
        assert validar_matricula("CRG-123") == True
    
    def test_matriculas_motos_validas(self):
        """Matrículas de motocicleta"""
        assert validar_matricula("M789XYZ") == True
    
    def test_matriculas_formato_incorrecto(self):
        """Formatos inválidos"""
        assert validar_matricula("P12ABC") == False     # Muy pocos números
        assert validar_matricula("P1234ABC") == False   # Muchos números
        assert validar_matricula("123ABC") == False     # Sin letra inicial
        assert validar_matricula("P-123-ABC") == False  # Guiones incorrectos
    
    def test_obtener_tipo_vehiculo(self):
        """Verificar que identifica correctamente el tipo"""
        assert obtener_tipo_vehiculo("P123ABC") == "Particular"
        assert obtener_tipo_vehiculo("A456DEF") == "Alquiler (Taxi)"
        assert obtener_tipo_vehiculo("CD-123") == "Cuerpo Diplomático"
        assert obtener_tipo_vehiculo("M789XYZ") == "Motocicleta"
