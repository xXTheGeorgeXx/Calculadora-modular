import csv
import datetime
import os

ARCHIVO_TXT = "historial.txt"
ARCHIVO_CSV = "historial.csv"

def guardar_en_historial(categoria, entrada, resultado):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_txt = f"[{fecha}] [{categoria}] Entrada: {entrada} → Resultado: {resultado}\n"
    with open(ARCHIVO_TXT, "a", encoding="utf-8") as f:
        f.write(linea_txt)

    escribir_csv = not os.path.exists(ARCHIVO_CSV) or os.stat(ARCHIVO_CSV).st_size == 0
    with open(ARCHIVO_CSV, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if escribir_csv:
            writer.writerow(["Fecha", "Categoría", "Entrada", "Resultado"])
        writer.writerow([fecha, categoria, entrada, resultado])

def mostrar_historial():
    if not os.path.exists(ARCHIVO_TXT) or os.stat(ARCHIVO_TXT).st_size == 0:
        print("No hay historial aún.")
        return
    print("\n--- HISTORIAL ---")
    with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
        print(f.read())

def borrar_historial():
    if not os.path.exists(ARCHIVO_TXT) and not os.path.exists(ARCHIVO_CSV):
        print("No hay historial que borrar.")
        return

    confirmacion = input("¿Estás seguro que deseas borrar todo el historial? (s/n): ").strip().lower()
    if confirmacion == 's':
        if os.path.exists(ARCHIVO_TXT):
            open(ARCHIVO_TXT, "w").close()
        if os.path.exists(ARCHIVO_CSV):
            open(ARCHIVO_CSV, "w").close()
        print("Historial borrado correctamente.\n")
    else:
        print("Operación cancelada.\n")