#Se definen las funciones en este bloque

def registrar_gastos_semanales():
    gastos = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("*** Registro de Gastos Semanales ***")
    
    # Este bloque itera ante todos los días de la semana para pedir un gasto correspondiente.
    for dia in dias:
        while True:
            try:
                monto = float(input(f"Ingrese el gasto para el {dia}: $"))             
                if monto < 0:
                    print("Error: El gasto no puede ser un número negativo.")
                    continue # Se vuelve a solicitar la entrada para el mismo día en caso de presentarse un error.
                
                # En caso de presentar una entrada válido y no es negativa se añadirá a la lista.
                gastos.append(monto)
                break  
            except ValueError:
                # En caso de no ingresarse un error, este se captura y se notifica.
                print("Error: Por favor, ingrese un monto numérico válido.")
                
    #  Cuando termina el bucle la función regresa a la lista completa de gastos.
    return gastos

def analizar_gastos(lista_de_gastos):
    #  Se verifica si la lista tiene datos para evitar una división por cero.
    if not lista_de_gastos:
        return 0.0, 0.0 # Retorna cero para total y promedio si no hay gastos.
    
    total_gastado = sum(lista_de_gastos)
    promedio_diario = total_gastado / len(lista_de_gastos)
    
    return total_gastado, promedio_diario

# Este bloque es el principal de ejecución

def main():
    # Se hace una llamada a la función para registrar los gastos y se guardan en la lista resultante.
    gastos_de_la_semana = registrar_gastos_semanales()
    
    total, promedio = analizar_gastos(gastos_de_la_semana)
    
    # Este bloque imprime el reporte final de gastos
    print("\n***** REPORTE DE GASTOS *****")
    print(f"Gasto total de la semana: ${total:.2f}")
    print(f"Gasto promedio diario: ${promedio:.2f}")
    print("-----------------------------------------------------")

if __name__ == "__main__":
    main()