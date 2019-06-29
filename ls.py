#! /usr/bin/env python3
import os
import argparse
from datetime import datetime
import pwd
import grp

def ls():
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
	flags = parser.parse_args()

	path = os.getcwd()
	contenido = list()
	for sd in os.scandir():
		contenido.append(sd)

	if flags.nombres:
		nombres = flags.nombres
		files = list()
		dirs = list()
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
		if not flags.all:
			files = listaPunto(files)
			dirs = listaPunto(dirs)
		files.sort()
		dirs.sort()
		for f in files:
			print(f, end='\t')
		print()
		for d in dirs:
			print(d + ':')
			archivosDir = os.listdir(d)
			archivosDir.sort()
			if flags.all:
				for arch in archivosDir:
					print(arch, end='\t')
			else:
				for arch in archivosDir:
					if not arch.startswith("."):
						print(arch, end='\t')
			print()
	else:
		if flags.all:
			lista_contenido= listaPunto(contenido)
		if not flags.all:
			lista_contenido = listaSinPunto(contenido)
		sorted(lista_contenido, key= useName)
		if flags.l:
			for contenido in lista_contenido:
				fecha= datetime.fromtimestamp(os.stat(contenido).st_mtime)
				fecha = fecha.strftime('%b %d %H:%M')
				permisos = oct(os.stat(contenido).st_mode)[-3:]
				permisos = getPermisos(permisos)
				usuario = pwd.getpwuid(os.stat(contenido).st_uid).pw_name
				enlaces = os.stat(contenido).st_nlink
				id_grupo = os.stat(contenido).st_gid
				grupo = grp.getgrgid(id_grupo).gr_name
				size = os.stat(contenido).st_size
				nombre = contenido.name
				print('{:10} {:5} {:16} {:12} {:15} {:15} {:15}'.format(permisos, enlaces, usuario, grupo, size, fecha, nombre))
		else:
			for contenido in lista_contenido:
				print(contenido.name, end = '\t')
			print()
# contenido.sort()#ordenar por fecha de modificacion
# if inode:
#    print()

#contenido.sort()
def useName(elemento):
	return elemento.name

def listaSinPunto(lista):
	for i in lista:
		if i.name.startswith("."):
			lista.remove(i)
	return lista

def listaPunto(lista):
	conPunto=[]
	for i in lista:
		if i.name.startswith("."):
			conPunto.add(i)
	return conPunto

def getPermisos(permiso):
	permiso = (permiso)
	valores =['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
	return valores[int(permiso[0],10)] + valores[int(permiso[1], 10)] + valores[int(permiso[2], 10)]


def main():
	ls()

if __name__ == '__main__':
	main()
