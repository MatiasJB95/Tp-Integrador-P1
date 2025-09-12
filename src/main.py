"""
Aplicación principal - Gestor de Países
TP Integrador - Programación 1
"""
import os
import sys

# Agregar el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.csv_handler import cargar_paises
from src.services.pais_service import listar_paises, filtrar_por_continente, ordenar_por_poblacion, ordenar_por_superficie
from src.utils.statistics import promedio_poblacion, pais_mas_poblado, pais_mas_grande


def main():
    """Función principal de la aplicación"""
    print("=" * 50)
    print("    GESTOR DE PAÍSES - PROGRAMACIÓN 1")
    print("=" * 50)
    
    # Cargar datos
    try:
        # Ruta al archivo CSV (relativa desde el directorio del proyecto)
        ruta_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'paises.csv')
        paises = cargar_paises(ruta_csv)
        
        if not paises:
            print("No se pudieron cargar los datos de países.")
            return
        
        print(f"✅ Se cargaron {len(paises)} países exitosamente.\n")
        
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")
        return
    
    # Demostración de funcionalidades
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Listar todos los países")
        print("2. Filtrar por continente")
        print("3. Países ordenados por población")
        print("4. Países ordenados por superficie")
        print("5. Estadísticas generales")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            print("\n📋 LISTADO COMPLETO DE PAÍSES:")
            print("-" * 50)
            listar_paises(paises)
            
        elif opcion == "2":
            continente = input("\nIngrese el continente (América, Asia, Europa, África, Oceanía): ").strip()
            paises_filtrados = filtrar_por_continente(paises, continente)
            
            if paises_filtrados:
                print(f"\n🌍 PAÍSES DE {continente.upper()}:")
                print("-" * 50)
                listar_paises(paises_filtrados)
            else:
                print(f"❌ No se encontraron países en {continente}")
                
        elif opcion == "3":
            paises_ordenados = ordenar_por_poblacion(paises, descendente=True)
            print("\n👥 PAÍSES ORDENADOS POR POBLACIÓN (Mayor a menor):")
            print("-" * 50)
            listar_paises(paises_ordenados)
            
        elif opcion == "4":
            paises_ordenados = ordenar_por_superficie(paises, descendente=True)
            print("\n🗺️  PAÍSES ORDENADOS POR SUPERFICIE (Mayor a menor):")
            print("-" * 50)
            listar_paises(paises_ordenados)
            
        elif opcion == "5":
            print("\n📊 ESTADÍSTICAS GENERALES:")
            print("-" * 50)
            
            # Promedio de población
            promedio_pob = promedio_poblacion(paises)
            print(f"Promedio de población mundial: {promedio_pob:,.0f} habitantes")
            
            # País más poblado
            mas_poblado = pais_mas_poblado(paises)
            if mas_poblado:
                print(f"País más poblado: {mas_poblado['nombre']} ({mas_poblado['poblacion']:,} hab.)")
            
            # País más grande
            mas_grande = pais_mas_grande(paises)
            if mas_grande:
                print(f"País más grande: {mas_grande['nombre']} ({mas_grande['superficie']:,} km²)")
                
            # Total de países por continente
            continentes = {}
            for pais in paises:
                cont = pais['continente']
                if cont in continentes:
                    continentes[cont] += 1
                else:
                    continentes[cont] = 1
            
            print("\nPaíses por continente:")
            for continente, cantidad in sorted(continentes.items()):
                print(f"  • {continente}: {cantidad} países")
                
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el Gestor de Países!")
            break
            
        else:
            print("❌ Opción inválida. Por favor, seleccione una opción del 1 al 6.")
        
        # Pausa para que el usuario pueda ver los resultados
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()