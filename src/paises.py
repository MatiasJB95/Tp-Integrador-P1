import csv

# -----------------------
# 1) Leer CSV -> lista de diccionarios
# -----------------------
def cargar_paises(path_csv):
    paises = []
    with open(path_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pais = {
                "nombre": row["nombre"],
                "poblacion": int(row["poblacion"]),
                "superficie": int(row["superficie"]),
                "continente": row["continente"]
            }
            paises.append(pais)
    return paises

# -----------------------
# 2) Listar
# -----------------------
def listar_paises(paises):
    for p in paises:
        print(f"{p['nombre']} | {p['poblacion']} hab. | {p['superficie']} km² | {p['continente']}")

# -----------------------
# 3) Filtros
# -----------------------
def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]

# -----------------------
# 4) Ordenamientos
# -----------------------
def ordenar_por_poblacion(paises, descendente=True):
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises, descendente=True):
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

# -----------------------
# 5) Estadísticas
# -----------------------
def promedio_poblacion(paises):
    if not paises:
        return 0
    return sum(p["poblacion"] for p in paises) / len(paises)

def pais_mas_poblado(paises):
    return max(paises, key=lambda p: p["poblacion"], default=None)

def pais_mas_grande(paises):
    return max(paises, key=lambda p: p["superficie"], default=None)
