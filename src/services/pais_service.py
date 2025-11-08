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
    # Normalizamos ambos textos a minúsculas y sin espacios extra
    return [p for p in paises if p["continente"].strip().lower() == continente.strip().lower()]


def filtrar_por_poblacion(paises, min_poblacion=0, max_poblacion=float('inf')):
    """
    Filtra países por rango de población.
    """
    return [p for p in paises if min_poblacion <= p["poblacion"] <= max_poblacion]


def filtrar_por_superficie(paises, min_superficie=0, max_superficie=float('inf')):
    """
    Filtra países por rango de superficie.
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


def actualizar_pais(paises, nombre, nueva_poblacion=None, nueva_superficie=None):
    """
    Actualiza la población y/o superficie de un país existente.
    
    Args:
        paises (list): Lista de diccionarios de países
        nombre (str): Nombre del país a actualizar
        nueva_poblacion (int, optional): Nueva población
        nueva_superficie (int, optional): Nueva superficie
        
    Returns:
        bool: True si se actualizó exitosamente, False si no se encontró el país
    """
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            if nueva_poblacion is not None:
                pais["poblacion"] = int(nueva_poblacion)
            if nueva_superficie is not None:
                pais["superficie"] = int(nueva_superficie)
            return True
    return False