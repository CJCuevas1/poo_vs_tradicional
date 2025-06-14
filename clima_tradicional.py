# Se definen las funciones principales para el registro y análisis de temperaturas semanales.

def registrar_temperaturas_semanales():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("*** Registro de Temperaturas Semanales ***")
    
    # Se solicita la temperatura de cada día de la semana.
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")
    return temperaturas

def analizar_temperaturas(lista_de_temperaturas):
    # Se verifica si la lista tiene datos para evitar división por cero.
    if not lista_de_temperaturas:
        return 0.0
    promedio_semanal = sum(lista_de_temperaturas) / len(lista_de_temperaturas)
    return promedio_semanal

# Bloque principal de ejecución
def main():
    temperaturas_semana = registrar_temperaturas_semanales()
    promedio = analizar_temperaturas(temperaturas_semana)
    print("\n**** REPORTE DE TEMPERATURAS ****")
    print(f"Promedio semanal de temperatura: {promedio:.2f}°C")
    print("----")

if __name__ == "__main__":
    main()