from controllers.controller import inserir_inicio, inserir_fim, inserir_depois, inserir_antes, inserir_indice, \
    verificar_pais, eliminar_inicio, eliminar_fim, eliminar_pais, verificar_numero


def run():
    try:
        while True:
            scan = input().split()
            match scan[0].upper():
                case "RPI":
                    inserir_inicio(scan)
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
                    pass
                case "":
                    break
    except:
        pass
