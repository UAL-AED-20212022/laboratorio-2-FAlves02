from models.LinkedList import LinkedList

lista = LinkedList()


def inserir_inicio(scan, lista):
    lista.insert_at_start(scan[1])
    lista.traverse_list()
    return lista


def inserir_fim(scan):
    lista.insert_at_end(scan[1])
    lista.traverse_list()
    return lista


def inserir_depois(scan):
    lista.insert_after_item(scan[2], scan[1])
    lista.traverse_list()
    return lista


def inserir_antes(scan):
    lista.insert_before_item(scan[2], scan[1])
    lista.traverse_list()
    return lista


def inserir_indice(scan):
    lista.insert_at_index(scan[2], scan[1])
    lista.traverse_list()
    return lista


def verificar_numero():
    lista.get_count()
    lista.traverse_list()
    return lista


def verificar_pais(scan):
    lista.search_item(scan[1])
    lista.traverse_list()
    return lista


def eliminar_inicio():
    lista.delete_at_start()
    lista.traverse_list()
    return lista


def eliminar_fim():
    lista.delete_at_end()
    lista.traverse_list()


def eliminar_pais(scan):
    lista.delete_element_by_value(scan[1])
    lista.traverse_list()
    return lista
