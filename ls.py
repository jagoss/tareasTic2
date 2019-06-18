#! /usr/bin/env python3
import os

def ls(nombres, myall = False, mydir = False, inode=False, largo = False, torden = False):
    path = os.getcwd()
    contenido = os.scandir()

    if nombres is not None:
        files = []
        dirs = []
        for nombre in nombres:
            for i in contenido:
                if nombre == i.name:
                    if is_dir(nombre):
                        dirs.append(nombre)
                    elif is_file(nombre):
                        files.append(nombre)
                else:
                    print( 'ls: cannot access \'' + nombre + '\': No such file or directory')


    else:
        if not myall:
           contenido = listaSinPunto(contenido)
        if torden:
           # contenido.sort()#ordenar por fecha de modificacion
        if inode:
            print()

        #contenido.sort()

def listaSinPunto(lista):
    for i in lista:
        if i.name.startswith('.'):
            lista.remove(i)
    return lista




def main():


if __name__ == '__main__':
    main()
