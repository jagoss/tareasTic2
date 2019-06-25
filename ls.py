#! /usr/bin/env python3
import os
import argparse

def ls(nombres, myall = False, mydir = False, inode=False, largo = False, torden = False):
    parser = argparse.ArgumentParser(description='banderas de la funcion')
    path = os.getcwd()
    contenido = os.scandir()
    
    parser.add_argument('-a', '--all',
        help='Incluye los archivos cuyo nombre comienza con punto')
        
    parser.add_argument
    

    if nombres:
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
            print()
           # contenido.sort()#ordenar por fecha de modificacion
       # if inode:
        #    print()

        #contenido.sort()

def listaSinPunto(lista):
    for i in lista:
        if i.name.startswith('.'):
            lista.remove(i)
    return lista




def main():
    print()


if __name__ == '__main__':
    main()
