def validar_codigo_reserva(codigo, reservas):
    if len(codigo) == 7 and codigo.startswhith("R") and " " not in codigo:
        for r in reservas:
            if r["codigo_reserva"] == codigo:
                return False
        return True
    return False

def validar_nombre_solicitante(solicitante):
    if len(solicitante) >=5:
        for caracter in solicitante:
            if caracter.isdigit():
                return False
            return True
        
def validar_tipo_sala(tipo_sala):
    if tipo_sala.upper() in ["P", "M", "G"]:
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
            es_valido, cantidad = validar_cantidad_personas(cant)
            if es_valido:
                break
            print("ERROR!! Cantidad inválida (debe ser un número entero entre 2 y 20).")

        while True:
            horas=input("Ingrese horas de reserva (1-8): ").strip()
            es_valido, horas = validar_horas_reserva(horas)
            if es_valido:
                break
            print("ERRO!! Horas inválidas (debe ser un número entero entre 1-8).")

            reserva = {
                "codigo_reserva": codigote,
                "nombre_solicitante": nombre,
                "tipo_sala": tipo,
                "cantidad_personas": cantidad,
                "horas_reserva": horas,
                "confirmada": False
            }      
            reservas.append(reserva)
            print("REserva registrada con éxito!!")

def eliminar_reserva(reservas, codigo_reserva):
    posicion = buscar_reserva(reservas, codigo_reserva)
    if posicion == -1:
        print("ERROR!! L reserva nofue encontrada.")
    else:
        reservas.pop(posicion)
        print("Reserva eliminada con éxito!")

def actualizar_confirmaciones(reservas):
    for res in reservas:
        if res["cantidad_personas"] >=10:
            res["confirmada"] = True
        else:
            res["Confirmada"] = False
    print("Estados de confirmación actualizados correctamente.")

def mostrar_reservas(reservas):
    if len(reservas) == 0:
        print("No existen reservas almacenadas.")
        return
    print("---LISTA DE TOAS LAS RESERVAS---")
    for res in reservas:
        print("-" * 35)
        reporte = {
            "Código": res["codigo_reserva"],
            "Solicitante": res["nombre_solicitante"],
            "Tipo Sala": res["tipo_sala"],
            "Personas": res["cantidad_personas"],
            "Horas": res["horas_reserva"],
            "Confirmada": "SÍ" if res["confirmada"] else "NO"
        }                                 
        for etiqueta, valor, in reporte.items():
            print(f"- {etiqueta} : {valor}")
        print("-" * 35) 
        #estaba probando esto que lo vi en un video.

def mostrar_reservas_confirmadas(reservas):
    contador_confirmados = 0
    print("----LISTA DE RESERVAS CONFIRMADAS----")
    for res in reservas:
        if res["confirmada"] == True:
            contador_confirmados +=1
            print("-" * 35)
            print(f"Código: {res["codigo_reserva"]}")
            print(f"Solicitante: {res["nombre_solicitante"]}")
            print(f"Cantidad de personas: {res["cantidad_personas"]}")
    if contador_confirmados == 0:
        print("No hay registros de reservas confirmadas actualmente.")
    else:
        print("-"*35)

lista_reservas =[] 
while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion ==1:
        agregar_reserva(lista_reservas)
    elif opcion ==2:
        codigo_buscar = input("Ingrese el código de reserva que desea buscar: ").strip()
        posicion = buscar_reserva(lista_reservas, codigo_buscar)
        if posicion == 1:
            print("Reserva no encontrada.")
        else:
            print(f"Reserva encontrada en la posición: {posicion}")
    elif opcion == 3:
        codigo_eliminar=input("Ingrese el código de reserva que eliminara: ").strip()
        eliminar_reserva(lista_reservas, codigo_eliminar)
    elif opcion == 4:
        actualizar_confirmaciones(lista_reservas)
    elif opcion == 5:
        mostrar_reservas(lista_reservas)
    elif opcion == 6: 
        print("Programa finalizado. Hasta luego!")
        break
    elif opcion == 7:
        mostrar_reservas_confirmadas(lista_reservas)                            
