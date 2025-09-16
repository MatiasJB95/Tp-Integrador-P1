"""
Servicio para gestión de países
Responsabilidad: Operaciones CRUD y filtros sobre países
"""


def listar_paises(paises):
    """
    Muestra la lista de países en formato tabular.
    
    Args:
        paises (list): Lista de diccionarios de países
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print(f"{'PAÍS':<20} | {'POBLACIÓN':<12} | {'SUPERFICIE':<12} | {'CONTINENTE':<15}")
    print("-" * 65)
    
    for p in paises:
        print(f"{p['nombre']:<20} | {p['poblacion']:>12,} | {p['superficie']:>12,} | {p['continente']:<15}")


def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente.
    
    Args:
        paises (list): Lista de diccionarios de países
        continente (str): Nombre del continente
        
    Returns:
        list: Lista de países del continente especificado
    """
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_poblacion(paises, min_poblacion=0, max_poblacion=float('inf')):
    """
    Filtra países por rango de población.
    
    Args:
        paises (list): Lista de diccionarios de países
        min_poblacion (int): Población mínima
        max_poblacion (int): Población máxima
        
    Returns:
        list: Lista de países dentro del rango de población
    """
    return [p for p in paises if min_poblacion <= p["poblacion"] <= max_poblacion]


def filtrar_por_superficie(paises, min_superficie=0, max_superficie=float('inf')):
    """
    Filtra países por rango de superficie.
    
    Args:
        paises (list): Lista de diccionarios de países
        min_superficie (int): Superficie mínima
        max_superficie (int): Superficie máxima
        
    Returns:
        list: Lista de países dentro del rango de superficie
    """
    return [p for p in paises if min_superficie <= p["superficie"] <= max_superficie]


def buscar_pais(paises, nombre):
    """
    Busca un país por nombre (búsqueda parcial, insensible a mayúsculas).
    
    Args:
        paises (list): Lista de diccionarios de países
        nombre (str): Nombre o parte del nombre a buscar
        
    Returns:
        list: Lista de países que coinciden con la búsqueda
    """
    nombre_lower = nombre.lower()
    return [p for p in paises if nombre_lower in p["nombre"].lower()]


def ordenar_por_poblacion(paises, descendente=True):
    """
    Ordena países por población.
    
    Args:
        paises (list): Lista de diccionarios de países
        descendente (bool): True para orden descendente, False para ascendente
        
    Returns:
        list: Lista de países ordenada por población
    """
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)


def ordenar_por_superficie(paises, descendente=True):
    """
    Ordena países por superficie.
    
    Args:
        paises (list): Lista de diccionarios de países
        descendente (bool): True para orden descendente, False para ascendente
        
    Returns:
        list: Lista de países ordenada por superficie
    """
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)


def ordenar_por_nombre(paises, descendente=False):
    """
    Ordena países por nombre alfabéticamente.
    
    Args:
        paises (list): Lista de diccionarios de países
        descendente (bool): True para orden descendente, False para ascendente
        
    Returns:
        list: Lista de países ordenada por nombre
    """
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    """
    Agrega un nuevo país a la lista.
    
    Args:
        paises (list): Lista de diccionarios de países
        nombre (str): Nombre del país
        poblacion (int): Población del país
        superficie (int): Superficie del país
        continente (str): Continente del país
        
    Returns:
        bool: True si se agregó exitosamente, False si ya existe
    """
    # Verificar si el país ya existe
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        return False
    
    nuevo_pais = {
        "nombre": nombre.strip(),
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente.strip()
    }
    
    paises.append(nuevo_pais)
    return True