# Se define la clase que representa el control de temperaturas semanales.
class ControlTemperaturasSemanal:
    def __init__(self):
        self._temperaturas_diarias = []

    # Método para registrar las temperaturas de cada día.
    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("*** Registro de Temperaturas Semanales (POO) ***")
        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el {dia}: "))
                    self._temperaturas_diarias.append(temp)
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido.")

    # Método para calcular y mostrar el promedio semanal.
    def generar_reporte(self):
        print("\n**** REPORTE DE TEMPERATURAS ****")
        if not self._temperaturas_diarias:
            print("No se registraron temperaturas esta semana.")
        else:
            promedio_semanal = sum(self._temperaturas_diarias) / len(self._temperaturas_diarias)
            print(f"Promedio semanal de temperatura: {promedio_semanal:.2f}°C")
        print("----")

# Bloque principal de ejecución
if __name__ == "__main__":
    mi_semana = ControlTemperaturasSemanal()
    mi_semana.ingresar_temperaturas()
    mi_semana.generar_reporte()