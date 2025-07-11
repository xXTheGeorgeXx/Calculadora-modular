# conversiones.py

# --- Temperatura ---
def celsius_a_fahrenheit(c):
    return round((c * 9 / 5) + 32, 2)

def fahrenheit_a_celsius(f):
    return round((f - 32) * 5 / 9, 2)

# --- Longitud ---
def metros_a_kilometros(m):
    return round(m / 1000, 4)

def kilometros_a_metros(km):
    return round(km * 1000, 4)

# --- Masa ---
def gramos_a_kilogramos(g):
    return round(g / 1000, 4)

def kilogramos_a_gramos(kg):
    return round(kg * 1000, 4)

def toneladas_a_kilogramos(t):
    return round(t * 1000, 4)

def kilogramos_a_toneladas(kg):
    return round(kg / 1000, 4)

def libras_a_kilogramos(lb):
    return round(lb * 0.45359237, 4)

def kilogramos_a_libras(kg):
    return round(kg / 0.45359237, 4)

# --- Tiempo ---
def segundos_a_minutos(seg):
    return round(seg / 60, 4)

def minutos_a_horas(mins):
    return round(mins / 60, 4)

def horas_a_dias(horas):
    return round(horas / 24, 4)

def dias_a_horas(dias):
    return round(dias * 24, 4)

def semanas_a_dias(sem):
    return round(sem * 7, 4)

def dias_a_semanas(dias):
    return round(dias / 7, 4)

def meses_a_dias(meses):
    return round(meses * 30.44, 2)  # promedio

def dias_a_meses(dias):
    return round(dias / 30.44, 2)

def años_a_dias(años):
    return round(años * 365.25, 2)  # incluye años bisiestos

def dias_a_años(dias):
    return round(dias / 365.25, 4)

# --- Volumen ---
def litros_a_mililitros(l):
    return round(l * 1000, 4)

def mililitros_a_litros(ml):
    return round(ml / 1000, 4)

def litros_a_galones(l):
    return round(l / 3.78541, 4)

def galones_a_litros(gal):
    return round(gal * 3.78541, 4)