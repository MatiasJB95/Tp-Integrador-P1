"""
Módulo de validaciones
Responsabilidad: Validar datos de entrada y tipos
"""


def validar_entero_positivo(valor, nombre_campo):
    """
    Valida que un valor sea un entero positivo.
    
    Args:
        valor: Valor a validar
        nombre_campo (str): Nombre del campo para mensajes de error
        
    Returns:
        tuple: (bool, int/None, str) -> (es_valido, valor_convertido, mensaje_error)
    """
    try:
        valor_int = int(valor)
        if valor_int < 0:
            return False, None, f"{nombre_campo} debe ser un número positivo"
        return True, valor_int, ""
    except (ValueError, TypeError):
        return False, None, f"{nombre_campo} debe ser un número válido"


def validar_cadena_no_vacia(valor, nombre_campo):
    """
    Valida que una cadena no esté vacía.
    
    Args:
        valor: Valor a validar
        nombre_campo (str): Nombre del campo para mensajes de error
        
    Returns:
        tuple: (bool, str/None, str) -> (es_valido, valor_limpio, mensaje_error)
    """
    if not valor or not str(valor).strip():
        return False, None, f"{nombre_campo} no puede estar vacío"
    
    valor_limpio = str(valor).strip()
    return True, valor_limpio, ""


def validar_continente(continente):
    """
    Valida que el continente sea uno de los valores permitidos.
    
    Args:
        continente (str): Nombre del continente
        
    Returns:
        tuple: (bool, str/None, str) -> (es_valido, continente_normalizado, mensaje_error)
    """
    continentes_validos = ["América", "Asia", "Europa", "África", "Oceanía"]
    
    es_valido, continente_limpio, error = validar_cadena_no_vacia(continente, "Continente")
    if not es_valido:
        return False, None, error
    
    # Buscar coincidencia insensible a mayúsculas
    for cont_valido in continentes_validos:
        if continente_limpio.lower() == cont_valido.lower():
            return True, cont_valido, ""
    
    return False, None, f"Continente debe ser uno de: {', '.join(continentes_validos)}"


def validar_datos_pais(nombre, poblacion, superficie, continente):
    """
    Valida todos los datos de un país.
    
    Args:
        nombre (str): Nombre del país
        poblacion: Población del país
        superficie: Superficie del país
        continente (str): Continente del país
        
    Returns:
        tuple: (bool, dict/None, list) -> (es_valido, datos_validados, errores)
    """
    errores = []
    datos = {}
    
    # Validar nombre
    valido, valor, error = validar_cadena_no_vacia(nombre, "Nombre del país")
    if valido:
        datos["nombre"] = valor
    else:
        errores.append(error)
    
    # Validar población
    valido, valor, error = validar_entero_positivo(poblacion, "Población")
    if valido:
        datos["poblacion"] = valor
    else:
        errores.append(error)
    
    # Validar superficie
    valido, valor, error = validar_entero_positivo(superficie, "Superficie")
    if valido:
        datos["superficie"] = valor
    else:
        errores.append(error)
    
    # Validar continente
    valido, valor, error = validar_continente(continente)
    if valido:
        datos["continente"] = valor
    else:
        errores.append(error)
    
    return len(errores) == 0, datos if len(errores) == 0 else None, errores