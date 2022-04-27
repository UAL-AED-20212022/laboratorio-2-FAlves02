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
                    print(f"O número de elementos são {verificar_numero()}")
                case "VP":
                    if not verificar_pais(scan) or verificar_pais() is None:
                        print(f"O país {scan[1]} não se encontra na lista.")
                    else:
                        print(f"O país {scan[1]} encontra-se na lista.")
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
