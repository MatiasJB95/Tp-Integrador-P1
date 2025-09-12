from src.paises import cargar_paises, promedio_poblacion, pais_mas_poblado

def test_promedio_poblacion():
    paises = [
        {"nombre": "A", "poblacion": 100, "superficie": 10, "continente": "X"},
        {"nombre": "B", "poblacion": 300, "superficie": 20, "continente": "Y"},
    ]
    assert promedio_poblacion(paises) == 200

def test_pais_mas_poblado():
    paises = [
        {"nombre": "A", "poblacion": 100, "superficie": 10, "continente": "X"},
        {"nombre": "B", "poblacion": 300, "superficie": 20, "continente": "Y"},
    ]
    assert pais_mas_poblado(paises)["nombre"] == "B"
