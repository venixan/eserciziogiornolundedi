def validar_codigo_reserva(codigo, reservas):
    if len(codigo) == 7 and codigo.startswhith("R") and " " not in codigo:
        for r in reservas:
            if r["codigo_reserva"] == codigo:
                return False
            return True
        return True
    return False

def validar_nombre_solicitante(solicitante):
    if len(solicitante) >=5:
        for caracter in solicitante:
            if caracter.isdigit():
                return False
            return True
        
def validar_tipo_sala(tipo_sala):
    if tipo_sala() in ["P", "M", "G"]:
        return True
    return False

def validar_cantidad_personas(cant_personas):
    try:
        numero=int(cant_personas)
        if 2<= numero <=20:
            return True, numero
        return False, None   
    except ValueError:
        return False, None     
 
def validar_horas_reserva(horas_reserva):
    try:
        numero = int(horas_reserva)
        if 2<= numero <=8:
            return True, numero
        return False, None
    except ValueError:
        return False, None
    
def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1. Registrar reserva")
    print("2. Buscar reserva.")
    print("3. Eliminar reserva.")
    print("4. Actualizar confirmaciones.")
    print("5. Mostrar reservas.")
    print("6. Salir")
    print("7. Mostrar reservas confirmadas")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1<= opcion <=7:
                return opcion
            print("ERROR!! debe ingresar una opción válida del menú (1-7).")
        except ValueError:
            print("ERROR!! debe ingresar un número entero válido.")


def buscar_reserva(reservas, codigo_reserva):
    for posicion in range(len(reservas)):
        if reservas[posicion]["codigo_reserva"]==codigo_reserva:
            return posicion
    return -1

def agregar_reserva(reservas):
    print("==Registrar nueva reserva==")

    while True:
        codigote=input("Ingrese código de reserva (EJ: R123456): ").strip()
        if validar_codigo_reserva(codigote, reservas):
            break
        print("ERROR!! Código inválido o ya existente(debe empezar con R y tener 7 caracteres)")

        while True:
            nombre=input("Ingrese nombre del solicitante: "). strip()
            if validar_nombre_solicitante(nombre):
                break
            print("ERROR!! nombre inválido (mínimo 5 caracteres y sin números.)")

        while True:
            tipo=input("Ingrese tipo de sala (P=Pequeña, M=Mediana, G=Grande): ").strip()
            if validar_tipo_sala(tipo):
                tipo = tipo.upper()
                break
            print("ERROR!! tipo de sala inválido. Use P, M o G.") 

        while True:
            cant=input("Ingrese cantidad de personas(2-20): ")
            es_valido, cantidad = validar_cantidad_personas   