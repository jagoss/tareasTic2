#! /usr/bin/env python3
import os
import argparse
from datetime import datetime
import pwd
import grp

entrada = None


def ls():
    flags = set_banderas()
    path = os.getcwd()
    lista_contenido = list()
    for sd in os.scandir():
        lista_contenido.append(sd)

    if flags.nombres:
        global entrada
        entrada = flags.nombres
        lista_datos = tiene_nombres(flags, lista_contenido, path)
        imprimir_nombres(lista_datos[0], lista_datos[1], flags)
    else:
        lista_contenido = ordenar(lista_contenido)
        if not flags.all:
            lista_contenido = lista_sin_punto(lista_contenido)
        if flags.l:
            lista_imprimir = get_lista_completa(lista_contenido)
            imprimir_lista_completa(lista_imprimir)
        else:
            imprimir_normal(lista_contenido)


def set_banderas():
    parser = argparse.ArgumentParser(description='banderas de la funcion')
    parser.add_argument('-a', '--all',
                        help='Incluye los archivos cuyo nombre comienza con punto')

    parser.add_argument('-d', '--directory',
                        help='Lista el propio directorio, no los archivos contenidos en el')

    parser.add_argument('-i', '--inode',
                        help='Muestra en la primera columna el numero del nodo i')

    parser.add_argument('-l',
                        help='Genera un listado largo')

    parser.add_argument('-t',
                        help='Ordena segun fecha de modificacion en lugar de alfabetico')

    parser.add_argument('nombres', type=str, nargs='*')

    return parser.parse_args()


def tiene_nombres(flags, contenido, path):
    files = list()
    dirs = list()
    for nombre in flags.nombres:
        existe = False
        for i in contenido:
            if nombre == i.name:
                existe = True
                if os.path.isdir(path + '/' + nombre):
                    dirs.append(nombre)
                elif os.path.isfile(path + '/' + nombre):
                    files.append(nombre)
        if not existe:
            print('ls: cannot access \'' + nombre + '\': No such file or directory')
    if not flags.all:
        files = lista_nombres_sin_punto(files)
        dirs = lista_nombres_sin_punto(dirs)
    files.sort()
    dirs.sort()
    return [files, dirs]


def get_lista_completa(lista_contenido):
    lista_final = list()
    for contenido in lista_contenido:
        if type(contenido) is str:
            guardar_info(contenido, lista_final, entrada)
        else:
            guardar_info(contenido.name, lista_final, entrada)

    return lista_final


def obtener_padre(padres, hijo):
    for padre in padres:
        if os.path.isdir(os.getcwd() + '/' + padre):
            hijos = os.listdir(padre)
            for h in hijos:
                if h == hijo:
                    return padre


def guardar_info(nombre_dato, lista, nombres):
    if nombres is None:
        ruta = nombre_dato
    else:
        ruta = obtener_padre(nombres, nombre_dato) + '/' + nombre_dato
    fecha = datetime.fromtimestamp(os.stat(ruta).st_mtime)
    fecha = fecha.strftime('%b %d %H:%M')
    permisos = oct(os.stat(ruta).st_mode)[-3:]
    permisos = get_permisos(permisos)
    usuario = pwd.getpwuid(os.stat(ruta).st_uid).pw_name
    enlaces = os.stat(ruta).st_nlink
    id_grupo = os.stat(ruta).st_gid
    grupo = grp.getgrgid(id_grupo).gr_name
    size = os.stat(ruta).st_size
    lista.append([permisos, enlaces, usuario, grupo, size, fecha, nombre_dato])


def imprimir_lista_completa(lista_final):
    for contenido in lista_final:
        len1 = str(len(contenido[0]) + 1)
        len3 = str(len(contenido[2]) + 1)
        len4 = str(len(contenido[3]) + 1)
        len6 = str(len(contenido[5]) + 1)
        len7 = str(len(contenido[6]) + 1)
        print((
                '{:' + len1 + '} {:3} {:' + len3 + '} {:' + len4 + '} {:7} {:' + len6 + '} {:' + len7 + '}').format(
            contenido[0], contenido[1], contenido[2], contenido[3],
            contenido[4], contenido[5], contenido[6]))


def imprimir_normal(lista_contenido):
    for contenido in lista_contenido:
        print(contenido.name, end='\t')
    print()


def imprimir_nombres(files, dirs, flags):
    if flags.l:
        # Se imprimen los arhivos del directorio
        lista_imprimir = get_lista_completa(files)
        imprimir_lista_completa(lista_imprimir)
        for d in dirs:
            print(d + ':')
            archivos_dir = os.listdir(d)
            archivos_dir.sort()
            if not flags.all:
                archivos_dir = lista_nombres_sin_punto(archivos_dir)
            lista_imprimir = get_lista_completa(archivos_dir)
            imprimir_lista_completa(lista_imprimir)
            print()
    else:
        imprimir_normal(files)
        for d in dirs:
            print(d + ':')
            archivos_dir = os.listdir(d)
            archivos_dir.sort()
            if flags.all:
                for arch in archivos_dir:
                    print(arch, end='\t')
            else:
                for arch in archivos_dir:
                    if not arch.startswith("."):
                        print(arch, end='\t')
            print()


def ordenar(lista):
    diccionario = dict()
    lista_temp = list()
    for l in lista:
        lista_temp.append(l.name)
        diccionario.update({l.name: l})
    lista_temp.sort(key=str.lower)
    salida = list()
    for l in lista_temp:
        salida.append(diccionario[l])
    return salida


def lista_sin_punto(lista):
    salida = list()
    for i in lista:
        if not i.name.startswith("."):
            salida.append(i)
    return salida


def lista_nombres_sin_punto(lista):
    salida = list()
    for element in lista:
        if not element.startswith('.'):
            salida.append(element)
    return salida


def get_permisos(permiso):
    permiso = list(permiso)
    valores = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
    return valores[int(permiso[0], 10)] + valores[int(permiso[1], 10)] + valores[int(permiso[2], 10)]


def main():
    ls()


if __name__ == '__main__':
    main()
