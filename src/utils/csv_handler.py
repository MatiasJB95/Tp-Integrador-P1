"""
Módulo para manejo de archivos CSV
Responsabilidad: Lectura y escritura de datos desde/hacia archivos CSV
"""
import csv
import os


def cargar_paises(path_csv):
    """
    Carga los datos de países desde un archivo CSV.
    
    Args:
        path_csv (str): Ruta al archivo CSV
        
    Returns:
        list: Lista de diccionarios con información de países
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si hay problemas con el formato de datos
    """
    paises = []
    
    # Verificar si el archivo existe
    if not os.path.exists(path_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {path_csv}")
    
    try:
        with open(path_csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            
            for row_num, row in enumerate(reader, start=2):  # Empieza en 2 por el header
                try:
                    pais = {
                        "nombre": row["nombre"].strip(),
                        "poblacion": int(row["poblacion"]),
                        "superficie": int(row["superficie"]),
                        "continente": row["continente"].strip()
                    }
                    paises.append(pais)
                    
                except (ValueError, KeyError) as e:
                    print(f"Error en línea {row_num}: {e}")
                    continue
                    
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []
    
    return paises


def guardar_paises(paises, path_csv):
    """
    Guarda los datos de países en un archivo CSV.
    
    Args:
        paises (list): Lista de diccionarios con información de países
        path_csv (str): Ruta donde guardar el archivo CSV
        
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    try:
        with open(path_csv, 'w', newline='', encoding='utf-8') as f:
            if not paises:
                return False
                
            fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(paises)
            
        return True
        
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")
        return False