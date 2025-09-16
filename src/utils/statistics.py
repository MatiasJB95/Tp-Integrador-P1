"""
Módulo de estadísticas para análisis de datos de países
Responsabilidad: Cálculos estadísticos y análisis de datos
"""


def promedio_poblacion(paises):
    """
    Calcula el promedio de población de una lista de países.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        float: Promedio de población, 0 si la lista está vacía
    """
    if not paises:
        return 0
    return sum(p["poblacion"] for p in paises) / len(paises)


def promedio_superficie(paises):
    """
    Calcula el promedio de superficie de una lista de países.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        float: Promedio de superficie, 0 si la lista está vacía
    """
    if not paises:
        return 0
    return sum(p["superficie"] for p in paises) / len(paises)


def pais_mas_poblado(paises):
    """
    Encuentra el país con mayor población.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        dict: País con mayor población, None si la lista está vacía
    """
    return max(paises, key=lambda p: p["poblacion"], default=None)


def pais_menos_poblado(paises):
    """
    Encuentra el país con menor población.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        dict: País con menor población, None si la lista está vacía
    """
    return min(paises, key=lambda p: p["poblacion"], default=None)


def pais_mas_grande(paises):
    """
    Encuentra el país con mayor superficie.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        dict: País con mayor superficie, None si la lista está vacía
    """
    return max(paises, key=lambda p: p["superficie"], default=None)


def pais_mas_pequeno(paises):
    """
    Encuentra el país con menor superficie.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        dict: País con menor superficie, None si la lista está vacía
    """
    return min(paises, key=lambda p: p["superficie"], default=None)


def densidad_poblacional(pais):
    """
    Calcula la densidad poblacional de un país (habitantes por km²).
    
    Args:
        pais (dict): Diccionario con datos del país
        
    Returns:
        float: Densidad poblacional, 0 si la superficie es 0
    """
    if pais["superficie"] == 0:
        return 0
    return pais["poblacion"] / pais["superficie"]


def estadisticas_continente(paises, continente):
    """
    Genera estadísticas para un continente específico.
    
    Args:
        paises (list): Lista de diccionarios de países
        continente (str): Nombre del continente
        
    Returns:
        dict: Diccionario con estadísticas del continente
    """
    paises_continente = [p for p in paises if p["continente"].lower() == continente.lower()]
    
    if not paises_continente:
        return None
    
    return {
        "continente": continente,
        "total_paises": len(paises_continente),
        "poblacion_total": sum(p["poblacion"] for p in paises_continente),
        "superficie_total": sum(p["superficie"] for p in paises_continente),
        "promedio_poblacion": promedio_poblacion(paises_continente),
        "promedio_superficie": promedio_superficie(paises_continente),
        "pais_mas_poblado": pais_mas_poblado(paises_continente),
        "pais_mas_grande": pais_mas_grande(paises_continente)
    }


def obtener_continentes(paises):
    """
    Obtiene la lista de continentes únicos de los países.
    
    Args:
        paises (list): Lista de diccionarios de países
        
    Returns:
        list: Lista de continentes únicos ordenados alfabéticamente
    """
    continentes = set(p["continente"] for p in paises)
    return sorted(list(continentes))