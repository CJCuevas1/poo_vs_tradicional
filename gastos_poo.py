# Se definen las clases que sirven como la plantilla para el objeto.
class ControlGastosSemanal:
    
    # Se presenta el método constructor y se ejecuta al crear un nuevo objeto de esta clase.
    def __init__(self):
        self._gastos_diarios = []

    # Este bloque presenta el método que registrará los gastos diarios.
    def ingresar_gastos(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("*** Registro de Gastos Semanales (POO) ***")
        
        for dia in dias:
            while True:
                try:
                    monto = float(input(f"Ingrese el gasto para el {dia}: $"))
                    if monto < 0:
                        print("Error: El gasto no puede ser un número negativo.")
                        continue
                    
                    # Este bloque modifica el estado interno del propio objeto usando self.
                    self._gastos_diarios.append(monto)
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un monto numérico válido.")

    # Se calcula y presenta el reporte de gastos.
    def generar_reporte(self):
        print("\n***** REPORTE DE GASTOS *****")
        
        if not self._gastos_diarios:
            print("No se registraron gastos esta semana.")
        else:
            total_gastado = sum(self._gastos_diarios)
            promedio_diario = total_gastado / len(self._gastos_diarios)
            
            # Esta parte imprime el reporte.
            print(f"Gasto total de la semana: ${total_gastado:.2f}")
            print(f"Gasto promedio diario: ${promedio_diario:.2f}")
            
        print("-----------------------------------------------------")

# Se toma otra vez el  bloque principal de ejecución
if __name__ == "__main__":
    
    mi_semana = ControlGastosSemanal()
    
    mi_semana.ingresar_gastos()
   
    mi_semana.generar_reporte()