import readline

from models.LinkedList import LinkedList

lista = LinkedList()


def inserir_inicio(scan):
    lista.insert_at_start(scan[1])


def inserir_fim(scan):
    lista.insert_at_end(scan[1])


def inserir_depois(scan):
    lista.insert_after_item(scan[2], scan[1])


def inserir_antes(scan):
    lista.insert_before_item(scan[2], scan[1])


def inserir_indice(scan):
    lista.insert_at_index(scan[2], scan[1])


def verificar_numero():
    lista.get_count()


def verificar_pais(scan):
    lista.search_item(scan[1])


def eliminar_inicio():
    lista.delete_at_start()


def eliminar_fim():
    lista.delete_at_end()


def eliminar_pais(scan):
    lista.delete_element_by_value(scan[1])


def printlist():
    i = list.start_node
    while i is not None:
        next = i.ref
