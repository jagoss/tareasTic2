#! /usr/bin/env python3
import os
import argparse

def ls(nombres):
	parser = argparse.ArgumentParser(description='banderas de la funcion')
	path = os.getcwd()
	contenido = os.scandir()
	nombres = nombres.split()

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

	flags = parser.parse_args()

	if nombres:
		files = []
		dirs = []
		for nombre in nombres:
			existe = False
			for i in contenido:
				if nombre == i.name:
					existe = True
					if os.path.isdir(path + '/' + nombre):
						dirs.append(nombre)
					elif os.path.isfile(path + '/' + nombre):
						files.append(nombre)
			if not existe:
				print( 'ls: cannot access \'' + nombre + '\': No such file or directory')
		files.sort()
		dirs.sort()
		for f in files:
			print(f, end='\t')
		for d in dirs:
			print(d + ':')
			archivosDir = os.listdir(d)
			archivosDir.sort()
			if flags.all:
				for arch in archivosDir:
					print(arch, end='\t')
			else:
				for arch in archivosDir:
					if not arch.startswith('.'):
						print(arch, end='\t')
			print()
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
	ls(input('>>>'))

if __name__ == '__main__':
	main()
