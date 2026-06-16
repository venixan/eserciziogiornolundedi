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
    try:
        numero=int(tipo_sala)
        if 2<= numero <=20:
            return True, numero
        return False, None        
 