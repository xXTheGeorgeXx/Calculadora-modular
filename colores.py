from colorama import init, Fore, Style

init(autoreset=True)  # Resetea colores automáticamente después de cada impresión

# Constantes de colores para usar directo
AZUL = Fore.BLUE + Style.BRIGHT
VERDE = Fore.GREEN + Style.BRIGHT
AMARILLO = Fore.YELLOW + Style.BRIGHT
ROJO = Fore.RED + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
RESET = Style.RESET_ALL

# Funciones de impresión con colores
def imprimir_titulo(texto):
    print(CYAN + texto + RESET)

def imprimir_menu_opcion(texto):
    print(AMARILLO + texto + RESET)

def imprimir_error(texto):
    print(ROJO + "Error: " + texto + RESET)

def imprimir_exito(texto):
    print(VERDE + texto + RESET)

def imprimir_resultado(texto):
    print(MAGENTA + "Resultado: " + str(texto) + RESET)