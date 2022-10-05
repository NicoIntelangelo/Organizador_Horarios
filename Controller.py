
horas = [00.15,00.30,00.45,1.00,1.15,1.30,1.45,2.00,2.15,2.30,2.45,3.00,3.15,3.30,3.45,4.00,4.15,4.30,4.45,5.00,5.15,5.30,5.45,6.00,6.15,6.30,6.45,
7.00,7.15,7.30,7.45,8.00,8.15,8.30,8.45,9.00,9.15,9.30,9.45,10.00,10.15,10.30,10.45,11.00,11.15,11.30,11.45,12.00,12.15,12.30,12.45,
13.00,13.15,13.30,13.45,14.00,14.15,14.30,14.45,15.00,15.15,15.30,15.45,16.00,16.15,16.30,16.45,17.00,17.15,17.30,17.45,18.00,18.15,18.30,18.45,
19.00,19.15,19.30,19.45,20.00,20.15,20.30,20.45,21.00,21.15,21.30,21.45,22.00,22.15,22.30,22.45,23.00,23.15,23.30,23.45,]
            


def amplitudHoraria (inicio: float,fin: float ) -> list:
    horas_validas = [hora for hora in horas if hora >= inicio and hora <= fin]
    return horas_validas    

def quitarHorario (inicio: float,fin: float, horas_validas: list) -> list:
    horas_validas2 = []
    for hora in horas_validas:
        if hora >= fin or hora <= inicio:
            horas_validas2.append(hora)
    return horas_validas2   #validar inicio > fin

def horasPosibles (duracion: float ,horas_validas: list):
    horas_validas2 = []
    for hora in horas_validas:
        if (hora + duracion) in horas_validas:
            horas_validas2.append((hora , (hora + duracion)))
    
    return horas_validas2


