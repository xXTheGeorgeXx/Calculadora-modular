"""
main.py - Calculadora Modular Avanzada
Autor: Jorge Rodriguez
Descripción: Proyecto de consola que permite realizar cálculos aritméticos,
científicos, estadísticos y conversiones, con historial y modularización.
"""
import Funciones as f
import conversiones as conv
import historial

def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: ingrese un número válido.")

def pedir_lista_numeros(mensaje):
    while True:
        datos = input(mensaje)
        try:
            lista = [float(x.strip()) for x in datos.split(",")]
            if len(lista) == 0:
                print("Error: debe ingresar al menos un número.")
                continue
            return lista
        except ValueError:
            print("Error: ingrese solo números separados por coma.")

# --- Menú Aritmética ---
def menu_aritmetico():
    while True:
        print("""
--- OPERACIONES ARITMÉTICAS ---
1 - Suma (varios números)
2 - Resta (dos números)
3 - Multiplicación (varios números)
4 - División (dos números)
5 - Potencia (base y exponente)
6 - Raíz cuadrada
7 - Módulo (a % b)
8 - Promedio
9 - Factorial
10 - Máximo
11 - Mínimo
12 - Redondear número
13 - Operación combinada (ej. 2+3*4)
14 - Volver
""")
        opcion = input("Opción: ")
        if opcion == "1":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            res = f.sumar(lista)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Aritmética", f"suma({lista})", res)
        elif opcion == "2":
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")
            res = f.restar(a, b)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Aritmética", f"resta({a}, {b})", res)
        elif opcion == "3":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            res = f.multiplicar(lista)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Aritmética", f"multiplicar({lista})", res)
        elif opcion == "4":
            a = pedir_numero("Dividendo: ")
            b = pedir_numero("Divisor: ")
            try:
                res = f.dividir(a, b)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"dividir({a}, {b})", res)
            except ValueError:
                print("Error: División por cero no permitida.")
        elif opcion == "5":
            base = pedir_numero("Base: ")
            exp = pedir_numero("Exponente: ")
            res = f.potencia(base, exp)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Aritmética", f"potencia({base}, {exp})", res)
        elif opcion == "6":
            n = pedir_numero("Número: ")
            try:
                res = f.raiz_cuadrada(n)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"raiz_cuadrada({n})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "7":
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")
            try:
                res = f.modulo(a, b)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"modulo({a}, {b})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "8":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.promedio_lista(lista)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"promedio({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "9":
            n = int(pedir_numero("Número entero: "))
            try:
                res = f.factorial(n)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"factorial({n})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "10":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.maximo(lista)
                print(f"Máximo: {res}")
                historial.guardar_en_historial("Aritmética", f"maximo({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "11":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.minimo(lista)
                print(f"Mínimo: {res}")
                historial.guardar_en_historial("Aritmética", f"minimo({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "12":
            num = pedir_numero("Número a redondear: ")
            dec = input("Cantidad de decimales (default = 2): ")
            try:
                dec = int(dec) if dec.strip() else 2
                res = f.redondear(num, dec)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"redondear({num}, {dec})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "13":
            expr = input("Ingrese una expresión matemática (ej. 2+3*4): ")
            try:
                res = f.operar_expresion(expr)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Aritmética", f"operar_expresion('{expr}')", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "14":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

# --- Menú Científica ---
def menu_cientifico():
    while True:
        print("""
--- OPERACIONES CIENTÍFICAS ---
1 - Logaritmo base 10
2 - Arco seno (grados)
3 - Arco coseno (grados)
4 - Arco tangente (grados)
5 - Seno hiperbólico
6 - Coseno hiperbólico
7 - Tangente hiperbólica
8 - Volver
""")
        opcion = input("Opción: ")
        if opcion == "1":
            n = pedir_numero("Número positivo: ")
            try:
                res = f.logaritmo(n)
                print(f"Resultado: {res}")
                historial.guardar_en_historial("Científica", f"logaritmo({n})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            x = pedir_numero("Valor entre -1 y 1: ")
            try:
                res = f.arco_seno(x)
                print(f"Resultado: {res} grados")
                historial.guardar_en_historial("Científica", f"arco_seno({x})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "3":
            x = pedir_numero("Valor entre -1 y 1: ")
            try:
                res = f.arco_coseno(x)
                print(f"Resultado: {res} grados")
                historial.guardar_en_historial("Científica", f"arco_coseno({x})", res)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "4":
            x = pedir_numero("Número: ")
            res = f.arco_tangente(x)
            print(f"Resultado: {res} grados")
            historial.guardar_en_historial("Científica", f"arco_tangente({x})", res)
        elif opcion == "5":
            x = pedir_numero("Número: ")
            res = f.seno_hiperbolico(x)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Científica", f"seno_hiperbolico({x})", res)
        elif opcion == "6":
            x = pedir_numero("Número: ")
            res = f.coseno_hiperbolico(x)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Científica", f"coseno_hiperbolico({x})", res)
        elif opcion == "7":
            x = pedir_numero("Número: ")
            res = f.tangente_hiperbolica(x)
            print(f"Resultado: {res}")
            historial.guardar_en_historial("Científica", f"tangente_hiperbolica({x})", res)
        elif opcion == "8":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

# --- Menú Estadística ---
def menu_estadistica():
    while True:
        print("""
--- MENÚ ESTADÍSTICA ---
1 - Promedio
2 - Mediana
3 - Moda
4 - Varianza
5 - Desviación estándar
6 - Volver
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.promedio_lista(lista)
                print(f"Promedio: {res}")
                historial.guardar_en_historial("Estadística", f"promedio({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.mediana(lista)
                print(f"Mediana: {res}")
                historial.guardar_en_historial("Estadística", f"mediana({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "3":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.moda(lista)
                if res is None:
                    print("No hay moda (todos los valores aparecen igual).")
                else:
                    print(f"Moda: {res}")
                historial.guardar_en_historial("Estadística", f"moda({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "4":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.varianza(lista)
                print(f"Varianza: {res}")
                historial.guardar_en_historial("Estadística", f"varianza({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "5":
            lista = pedir_lista_numeros("Ingrese números separados por coma: ")
            try:
                res = f.desviacion_estandar(lista)
                print(f"Desviación estándar: {res}")
                historial.guardar_en_historial("Estadística", f"desviacion_estandar({lista})", res)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

# --- Menú Conversiones ---
def menu_conversiones():
    while True:
        print("""
--- MENÚ DE CONVERSIONES ---
1 - Temperatura
2 - Longitud
3 - Masa
4 - Tiempo
5 - Volumen
6 - Volver
""")
        opcion = input("Seleccione categoría: ")
        if opcion == "1":
            menu_temperatura()
        elif opcion == "2":
            menu_longitud()
        elif opcion == "3":
            menu_masa()
        elif opcion == "4":
            menu_tiempo()
        elif opcion == "5":
            menu_volumen()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

def menu_temperatura():
    while True:
        print("""
--- CONVERSIONES DE TEMPERATURA ---
1 - Celsius a Fahrenheit
2 - Fahrenheit a Celsius
3 - Volver
""")
        op = input("Opción: ")
        if op == "1":
            c = pedir_numero("Ingrese grados Celsius: ")
            res = conv.celsius_a_fahrenheit(c)
            print(f"Resultado: {res} °F")
            historial.guardar_en_historial("Temperatura", f"{c} °C", f"{res} °F")
        elif op == "2":
            fgrados = pedir_numero("Ingrese grados Fahrenheit: ")
            res = conv.fahrenheit_a_celsius(fgrados)
            print(f"Resultado: {res} °C")
            historial.guardar_en_historial("Temperatura", f"{fgrados} °F", f"{res} °C")
        elif op == "3":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

def menu_longitud():
    while True:
        print("""
--- CONVERSIONES DE LONGITUD ---
1 - Metros a Kilómetros
2 - Kilómetros a Metros
3 - Volver
""")
        op = input("Opción: ")
        if op == "1":
            m = pedir_numero("Ingrese metros: ")
            res = conv.metros_a_kilometros(m)
            print(f"Resultado: {res} km")
            historial.guardar_en_historial("Longitud", f"{m} m", f"{res} km")
        elif op == "2":
            km = pedir_numero("Ingrese kilómetros: ")
            res = conv.kilometros_a_metros(km)
            print(f"Resultado: {res} m")
            historial.guardar_en_historial("Longitud", f"{km} km", f"{res} m")
        elif op == "3":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

def menu_masa():
    while True:
        print("""
--- CONVERSIONES DE MASA ---
1 - Gramos a Kilogramos
2 - Kilogramos a Gramos
3 - Toneladas a Kilogramos
4 - Kilogramos a Toneladas
5 - Libras a Kilogramos
6 - Kilogramos a Libras
7 - Volver
""")
        op = input("Opción: ")
        if op == "1":
            g = pedir_numero("Ingrese gramos: ")
            res = conv.gramos_a_kilogramos(g)
            print(f"Resultado: {res} kg")
            historial.guardar_en_historial("Masa", f"{g} g", f"{res} kg")
        elif op == "2":
            kg = pedir_numero("Ingrese kilogramos: ")
            res = conv.kilogramos_a_gramos(kg)
            print(f"Resultado: {res} g")
            historial.guardar_en_historial("Masa", f"{kg} kg", f"{res} g")
        elif op == "3":
            t = pedir_numero("Ingrese toneladas: ")
            res = conv.toneladas_a_kilogramos(t)
            print(f"Resultado: {res} kg")
            historial.guardar_en_historial("Masa", f"{t} t", f"{res} kg")
        elif op == "4":
            kg = pedir_numero("Ingrese kilogramos: ")
            res = conv.kilogramos_a_toneladas(kg)
            print(f"Resultado: {res} t")
            historial.guardar_en_historial("Masa", f"{kg} kg", f"{res} t")
        elif op == "5":
            lb = pedir_numero("Ingrese libras: ")
            res = conv.libras_a_kilogramos(lb)
            print(f"Resultado: {res} kg")
            historial.guardar_en_historial("Masa", f"{lb} lb", f"{res} kg")
        elif op == "6":
            kg = pedir_numero("Ingrese kilogramos: ")
            res = conv.kilogramos_a_libras(kg)
            print(f"Resultado: {res} lb")
            historial.guardar_en_historial("Masa", f"{kg} kg", f"{res} lb")
        elif op == "7":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

def menu_tiempo():
    while True:
        print("""
--- CONVERSIONES DE TIEMPO ---
1 - Segundos a Minutos
2 - Minutos a Horas
3 - Horas a Días
4 - Días a Horas
5 - Semanas a Días
6 - Días a Semanas
7 - Meses a Días
8 - Días a Meses
9 - Años a Días
10 - Días a Años
11 - Volver
""")
        op = input("Opción: ")
        if op == "1":
            s = pedir_numero("Ingrese segundos: ")
            res = conv.segundos_a_minutos(s)
            print(f"Resultado: {res} minutos")
            historial.guardar_en_historial("Tiempo", f"{s} segundos", f"{res} minutos")
        elif op == "2":
            m = pedir_numero("Ingrese minutos: ")
            res = conv.minutos_a_horas(m)
            print(f"Resultado: {res} horas")
            historial.guardar_en_historial("Tiempo", f"{m} minutos", f"{res} horas")
        elif op == "3":
            h = pedir_numero("Ingrese horas: ")
            res = conv.horas_a_dias(h)
            print(f"Resultado: {res} días")
            historial.guardar_en_historial("Tiempo", f"{h} horas", f"{res} días")
        elif op == "4":
            d = pedir_numero("Ingrese días: ")
            res = conv.dias_a_horas(d)
            print(f"Resultado: {res} horas")
            historial.guardar_en_historial("Tiempo", f"{d} días", f"{res} horas")
        elif op == "5":
            sem = pedir_numero("Ingrese semanas: ")
            res = conv.semanas_a_dias(sem)
            print(f"Resultado: {res} días")
            historial.guardar_en_historial("Tiempo", f"{sem} semanas", f"{res} días")
        elif op == "6":
            d = pedir_numero("Ingrese días: ")
            res = conv.dias_a_semanas(d)
            print(f"Resultado: {res} semanas")
            historial.guardar_en_historial("Tiempo", f"{d} días", f"{res} semanas")
        elif op == "7":
            meses = pedir_numero("Ingrese meses: ")
            res = conv.meses_a_dias(meses)
            print(f"Resultado: {res} días")
            historial.guardar_en_historial("Tiempo", f"{meses} meses", f"{res} días")
        elif op == "8":
            d = pedir_numero("Ingrese días: ")
            res = conv.dias_a_meses(d)
            print(f"Resultado: {res} meses")
            historial.guardar_en_historial("Tiempo", f"{d} días", f"{res} meses")
        elif op == "9":
            años = pedir_numero("Ingrese años: ")
            res = conv.años_a_dias(años)
            print(f"Resultado: {res} días")
            historial.guardar_en_historial("Tiempo", f"{años} años", f"{res} días")
        elif op == "10":
            d = pedir_numero("Ingrese días: ")
            res = conv.dias_a_años(d)
            print(f"Resultado: {res} años")
            historial.guardar_en_historial("Tiempo", f"{d} días", f"{res} años")
        elif op == "11":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

def menu_volumen():
    while True:
        print("""
--- CONVERSIONES DE VOLUMEN ---
1 - Litros a Mililitros
2 - Mililitros a Litros
3 - Litros a Galones
4 - Galones a Litros
5 - Volver
""")
        op = input("Opción: ")
        if op == "1":
            l = pedir_numero("Ingrese litros: ")
            res = conv.litros_a_mililitros(l)
            print(f"Resultado: {res} ml")
            historial.guardar_en_historial("Volumen", f"{l} litros", f"{res} ml")
        elif op == "2":
            ml = pedir_numero("Ingrese mililitros: ")
            res = conv.mililitros_a_litros(ml)
            print(f"Resultado: {res} litros")
            historial.guardar_en_historial("Volumen", f"{ml} ml", f"{res} litros")
        elif op == "3":
            l = pedir_numero("Ingrese litros: ")
            res = conv.litros_a_galones(l)
            print(f"Resultado: {res} galones")
            historial.guardar_en_historial("Volumen", f"{l} litros", f"{res} galones")
        elif op == "4":
            gal = pedir_numero("Ingrese galones: ")
            res = conv.galones_a_litros(gal)
            print(f"Resultado: {res} litros")
            historial.guardar_en_historial("Volumen", f"{gal} galones", f"{res} litros")
        elif op == "5":
            break
        else:
            print("Opción inválida.")
        input("Presione ENTER para continuar...")

# --- Menú Principal ---
def menu_principal():
    while True:
        print("""
========= CALCULADORA MODULAR AVANZADA =========

1 - Operaciones Aritméticas
2 - Operaciones Científicas
3 - Estadística
4 - Conversiones
5 - Ver Historial
6 - Borrar Historial
7 - Salir

===============================================
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_aritmetico()
        elif opcion == "2":
            menu_cientifico()
        elif opcion == "3":
            menu_estadistica()
        elif opcion == "4":
            menu_conversiones()
        elif opcion == "5":
            historial.mostrar_historial()
            input("Presione ENTER para continuar...")
        elif opcion == "6":
            historial.borrar_historial()
            input("Presione ENTER para continuar...")
        elif opcion == "7":
            print("Gracias por usar la calculadora. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida.")
            input("Presione ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()