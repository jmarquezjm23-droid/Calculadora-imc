# Definición de colores ANSI
VERDE = "\033[32m"    # Verde estándar
MORADO = "\033[35m"   # Magenta estándar
AMARILLO = "\033[33m" # Amarillo para errores
CIAN = "\033[36m"     # Cian para la clasificación
RESET = "\033[0m"

print(f"{VERDE} === CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC) === {RESET}")

# Validación de Texto (Nombre y Apellidos: solo letras y espacios)
def validar_texto(mensaje):
    while True:
        texto = input(f"{MORADO}{mensaje}{RESET} ").strip()
        if not texto:
            print(f"{AMARILLO}Error: El campo no puede quedar vacío.{RESET}")
            continue
        if all(palabra.isalpha() for palabra in texto.split()):
            return texto
        else:
            print(f"{AMARILLO}Error: Solo se permiten letras y espacios.{RESET}")

nombre = validar_texto("Nombre(s):")
apellido_paterno = validar_texto("Apellido paterno:")
apellido_materno = validar_texto("Apellido materno:")

# Validación de Edad
while True:
    edad_input = input(f"{MORADO}Edad (en años):{RESET} ").strip()
    if not edad_input:
        print(f"{AMARILLO}Error: La edad no puede quedar vacía.{RESET}")
        continue
    if edad_input.isdigit():
        edad = int(edad_input)
        if edad > 0:
            break
        else:
            print(f"{AMARILLO}Error: La edad debe ser mayor a cero.{RESET}")
    else:
        print(f"{AMARILLO}Error: La edad debe ser un número entero, por ejemplo 43.{RESET}")

# Capas adicionales para validar si es mayor de edad
if edad < 18:
    estado_edad = "Menor de edad"
else:
    estado_edad = "Mayor de edad"

# Validación de Peso


while True:
    peso_input = input(f"{MORADO}Peso (en kg, ej. 74.5):{RESET} ").strip()
    if not peso_input:
        print(f"{AMARILLO}Error: El peso no puede quedar vacío.{RESET}")
        continue
    try:
        peso = float(peso_input)
        if peso > 0:
            break
        else:
            print(f"{AMARILLO}Error: El peso debe ser mayor a cero.{RESET}")
    except ValueError:
        print(f"{AMARILLO}Error: Debes introducir una cifra numérica válida para el peso.{RESET}")

# Validación de Estatura
while True:
    estatura_input = input(f"{MORADO}Introduce tu estatura (en metros, ej. 1.62):{RESET} ").strip()
    if not estatura_input:
        print(f"{AMARILLO}Error: La estatura no puede quedar vacía.{RESET}")
        continue
    try:
        estatura = float(estatura_input)
        if estatura > 0:
            break
        else:
            print(f"{AMARILLO}Error: La estatura debe ser mayor a cero.{RESET}")
    except ValueError:
        print(f"{AMARILLO}Error: Debes introducir una cifra numérica válida para la estatura.{RESET}")

# Cálculo del IMC
imc = peso / (estatura ** 2)

# Clasificación del IMC basada en los rangos del Gist encontrado
if imc < 16.00:
    clasificacion = "Delgadez severa"
elif imc >= 16.00 and imc <= 16.99:
    clasificacion = "Delgadez moderada"
elif imc >= 17.00 and imc <= 18.49:
    clasificacion = "Delgadez leve"
elif imc >= 18.50 and imc <= 24.99:
    clasificacion = "Normal"
elif imc >= 25.00 and imc <= 29.99:
    clasificacion = "Sobrepeso"
elif imc >= 30.00 and imc <= 34.99:
    clasificacion = "Obesidad leve"
elif imc >= 35.00 and imc <= 39.99:
    clasificacion = "Obesidad media"
else:
    clasificacion = "Obesidad mórbida"

# Resumen de resultados con colores
print(f"\n{VERDE}======================================={RESET}")
print(f"{VERDE}          RESUMEN DE RESULTADOS        {RESET}")
print(f"{VERDE}======================================={RESET}")
print(f"{MORADO}Nombre Completo: {RESET}{nombre} {apellido_paterno} {apellido_materno}")
print(f"{MORADO}Edad: {RESET}{edad} años ({estado_edad})")
print(f"{MORADO}Peso registrado: {RESET}{peso} kg")
print(f"{MORADO}Estatura registrada: {RESET}{estatura} m")
print(f"{VERDE}---------------------------------------{RESET}")
print(f"{VERDE}Tu Índice de Masa Corporal (IMC) es: {RESET}{imc:.2f} kg/m²")
print(f"{CIAN}Diagnóstico: {clasificacion}{RESET}")
print(f"{VERDE}======================================={RESET}")
