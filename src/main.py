"""
Aplicación principal - Gestor de Países
TP Integrador - Programación 1
"""
import os
import sys

# Agregar el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.csv_handler import cargar_paises, guardar_paises
from src.services.pais_service import (
    listar_paises, filtrar_por_continente, ordenar_por_poblacion, 
    ordenar_por_superficie, ordenar_por_nombre, buscar_pais,
    filtrar_por_poblacion, filtrar_por_superficie, agregar_pais, actualizar_pais
)
from src.utils.statistics import (
    promedio_poblacion, promedio_superficie, pais_mas_poblado, 
    pais_menos_poblado, pais_mas_grande, pais_mas_pequeno, obtener_continentes
)
from src.utils.validations import validar_datos_pais, validar_entero_positivo


def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    print("\n" + "=" * 60)
    print("                    MENÚ PRINCIPAL")
    print("=" * 60)
    print("1.  Listar todos los países")
    print("2.  Buscar país por nombre")
    print("3.  Agregar nuevo país")
    print("4.  Actualizar datos de un país")
    print("5.  Filtrar países")
    print("6.  Ordenar países")
    print("7.  Estadísticas")
    print("8.  Guardar cambios en CSV")
    print("9.  Salir")
    print("=" * 60)


def menu_filtros(paises):
    """Submenú para filtrar países"""
    while True:
        print("\n" + "=" * 60)
        print("                    FILTROS")
        print("=" * 60)
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menú principal")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            # 🔹 Filtro por continente
            continentes = ["América", "Asia", "Europa", "Oceanía", "África"]

            print("\nContinentes disponibles:")
            for i, cont in enumerate(continentes, 1):
                print(f"{i}. {cont}")

            opcion_cont = input("\nIngrese el número del continente: ").strip()

            if not opcion_cont.isdigit() or not (1 <= int(opcion_cont) <= len(continentes)):
                print("❌ Opción inválida.")
                pausar()
                continue

            continente_elegido = continentes[int(opcion_cont) - 1]
            paises_filtrados = filtrar_por_continente(paises, continente_elegido)

            if paises_filtrados:
                print(f"\n🌍 PAÍSES DE {continente_elegido.upper()}:")
                print("-" * 60)
                listar_paises(paises_filtrados)
            else:
                print(f"❌ No se encontraron países en {continente_elegido}")

        elif opcion == "2":
            # 🔹 Filtro por población
            try:
                min_pob = input("Población mínima (Enter para omitir): ").strip()
                max_pob = input("Población máxima (Enter para omitir): ").strip()
                
                min_poblacion = int(min_pob) if min_pob else 0
                max_poblacion = int(max_pob) if max_pob else float('inf')
                
                paises_filtrados = filtrar_por_poblacion(paises, min_poblacion, max_poblacion)
                
                if paises_filtrados:
                    print(f"\n👥 PAÍSES CON POBLACIÓN ENTRE {min_poblacion:,} Y {max_poblacion:,}:")
                    print("-" * 60)
                    listar_paises(paises_filtrados)
                else:
                    print("❌ No se encontraron países con ese rango de población")
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos")
                
        elif opcion == "3":
            # 🔹 Filtro por superficie
            try:
                min_sup = input("Superficie mínima en km² (Enter para omitir): ").strip()
                max_sup = input("Superficie máxima en km² (Enter para omitir): ").strip()
                
                min_superficie = int(min_sup) if min_sup else 0
                max_superficie = int(max_sup) if max_sup else float('inf')
                
                paises_filtrados = filtrar_por_superficie(paises, min_superficie, max_superficie)
                
                if paises_filtrados:
                    print(f"\n🗺️  PAÍSES CON SUPERFICIE ENTRE {min_superficie:,} Y {max_superficie:,} km²:")
                    print("-" * 60)
                    listar_paises(paises_filtrados)
                else:
                    print("❌ No se encontraron países con ese rango de superficie")
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos")
                
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")
        
        pausar()


def menu_ordenar(paises):
    """Submenú para ordenar países"""
    while True:
        print("\n" + "=" * 60)
        print("                    ORDENAR PAÍSES")
        print("=" * 60)
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("4. Volver al menú principal")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion in ["1", "2", "3"]:
            orden = input("¿Orden ascendente (A) o descendente (D)? ").strip().upper()
            descendente = (orden == "D")
            
            if opcion == "1":
                paises_ordenados = ordenar_por_nombre(paises, descendente)
                print("\n📝 PAÍSES ORDENADOS POR NOMBRE:")
            elif opcion == "2":
                paises_ordenados = ordenar_por_poblacion(paises, descendente)
                print("\n👥 PAÍSES ORDENADOS POR POBLACIÓN:")
            else:
                paises_ordenados = ordenar_por_superficie(paises, descendente)
                print("\n🗺️  PAÍSES ORDENADOS POR SUPERFICIE:")
            
            print("-" * 60)
            listar_paises(paises_ordenados)
            
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")
        
        pausar()


def menu_estadisticas(paises):
    """Muestra todas las estadísticas disponibles"""
    print("\n" + "=" * 60)
    print("                    ESTADÍSTICAS GENERALES")
    print("=" * 60)
    
    # Población
    print("\n📊 POBLACIÓN:")
    promedio_pob = promedio_poblacion(paises)
    print(f"  • Promedio mundial: {promedio_pob:,.0f} habitantes")
    
    mas_poblado = pais_mas_poblado(paises)
    if mas_poblado:
        print(f"  • País más poblado: {mas_poblado['nombre']} ({mas_poblado['poblacion']:,} hab.)")
    
    menos_poblado = pais_menos_poblado(paises)
    if menos_poblado:
        print(f"  • País menos poblado: {menos_poblado['nombre']} ({menos_poblado['poblacion']:,} hab.)")
    
    # Superficie
    print("\n🗺️  SUPERFICIE:")
    promedio_sup = promedio_superficie(paises)
    print(f"  • Promedio mundial: {promedio_sup:,.0f} km²")
    
    mas_grande = pais_mas_grande(paises)
    if mas_grande:
        print(f"  • País más grande: {mas_grande['nombre']} ({mas_grande['superficie']:,} km²)")
    
    mas_pequeno = pais_mas_pequeno(paises)
    if mas_pequeno:
        print(f"  • País más pequeño: {mas_pequeno['nombre']} ({mas_pequeno['superficie']:,} km²)")
    
    # Países por continente
    print("\n🌍 DISTRIBUCIÓN POR CONTINENTE:")
    continentes = {}
    for pais in paises:
        cont = pais['continente']
        continentes[cont] = continentes.get(cont, 0) + 1
    
    for continente, cantidad in sorted(continentes.items()):
        print(f"  • {continente}: {cantidad} países")
    
    print(f"\n📈 Total de países en el sistema: {len(paises)}")


def main():
    """Función principal de la aplicación"""
    print("=" * 60)
    print("         GESTOR DE PAÍSES - PROGRAMACIÓN 1")
    print("=" * 60)
    
    # Cargar datos
    try:
        ruta_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'paises.csv')
        paises = cargar_paises(ruta_csv)
        
        if not paises:
            print("❌ No se pudieron cargar los datos de países.")
            return
        
        print(f"✅ Se cargaron {len(paises)} países exitosamente.")
        
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")
        return
    
    # Menú principal
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1-9): ").strip()
        
        if opcion == "1":
            # Listar todos los países
            print("\n📋 LISTADO COMPLETO DE PAÍSES:")
            print("-" * 60)
            listar_paises(paises)
            pausar()
            
        elif opcion == "2":
            # Buscar país
            nombre = input("\nIngrese el nombre del país a buscar: ").strip()
            if nombre:
                resultados = buscar_pais(paises, nombre)
                if resultados:
                    print(f"\n🔍 RESULTADOS DE BÚSQUEDA PARA '{nombre}':")
                    print("-" * 60)
                    listar_paises(resultados)
                else:
                    print(f"❌ No se encontraron países con '{nombre}'")
            else:
                print("❌ Debe ingresar un nombre")
            pausar()
            
        elif opcion == "3":
            # Agregar país
            print("\n➕ AGREGAR NUEVO PAÍS:")
            print("-" * 60)
            
            nombre = input("Nombre del país: ").strip()
            poblacion = input("Población: ").strip()
            superficie = input("Superficie (km²): ").strip()
            
            print("\nContinentes disponibles: América, Asia, Europa, África, Oceanía")
            continente = input("Continente: ").strip()
            
            # Validar datos
            es_valido, datos, errores = validar_datos_pais(nombre, poblacion, superficie, continente)
            
            if es_valido:
                if agregar_pais(paises, datos["nombre"], datos["poblacion"], datos["superficie"], datos["continente"]):
                    print(f"✅ País '{datos['nombre']}' agregado exitosamente")
                else:
                    print(f"❌ El país '{datos['nombre']}' ya existe")
            else:
                print("❌ Errores de validación:")
                for error in errores:
                    print(f"  • {error}")
            pausar()
            
        elif opcion == "4":
            # Actualizar país
            print("\n✏️  ACTUALIZAR DATOS DE PAÍS:")
            print("-" * 60)
            
            nombre = input("Nombre del país a actualizar: ").strip()
            
            # Buscar si existe
            if buscar_pais(paises, nombre):
                nueva_pob = input("Nueva población (Enter para mantener): ").strip()
                nueva_sup = input("Nueva superficie (Enter para mantener): ").strip()
                
                poblacion = None
                superficie = None
                
                if nueva_pob:
                    es_valido, poblacion, error = validar_entero_positivo(nueva_pob, "Población")
                    if not es_valido:
                        print(f"❌ {error}")
                        pausar()
                        continue
                
                if nueva_sup:
                    es_valido, superficie, error = validar_entero_positivo(nueva_sup, "Superficie")
                    if not es_valido:
                        print(f"❌ {error}")
                        pausar()
                        continue
                
                if actualizar_pais(paises, nombre, poblacion, superficie):
                    print(f"✅ País '{nombre}' actualizado exitosamente")
                else:
                    print(f"❌ No se pudo actualizar el país")
            else:
                print(f"❌ No se encontró el país '{nombre}'")
            pausar()
            
        elif opcion == "5":
            # Filtros
            menu_filtros(paises)
            
        elif opcion == "6":
            # Ordenar
            menu_ordenar(paises)
            
        elif opcion == "7":
            # Estadísticas
            menu_estadisticas(paises)
            pausar()
            
        elif opcion == "8":
            # Guardar cambios
            try:
                if guardar_paises(paises, ruta_csv):
                    print("✅ Cambios guardados exitosamente en el archivo CSV")
                else:
                    print("❌ No se pudieron guardar los cambios")
            except Exception as e:
                print(f"❌ Error al guardar: {e}")
            pausar()
            
        elif opcion == "9":
            # Salir
            print("\n👋 ¡Gracias por usar el Gestor de Países!")
            print("Desarrollado para TP Integrador - Programación 1")
            break
            
        else:
            print("❌ Opción inválida. Seleccione una opción del 1 al 9.")
            pausar()


if __name__ == "__main__":
    main()