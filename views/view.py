import self as self

from controllers.controller import *


def run():
    try:
        while True:
            scan = input().split()
            match scan[0].upper():
                case "RPI":
                    inserir_inicio(scan, lista)
                case "RPF":
                    inserir_fim(scan)
                case "RPDE":
                    inserir_depois(scan)
                case "RPAE":
                    inserir_antes(scan)
                case "RPII":
                    inserir_indice(scan)
                case "VNE":
                    verificar_numero()
                case "VP":
                    verificar_pais(scan)
                case "EPE":
                    eliminar_inicio()
                case "EUE":
                    eliminar_fim()
                case "EP":
                    eliminar_pais(scan)
                case _:
                    pass
                
    except:
        pass
