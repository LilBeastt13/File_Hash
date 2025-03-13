#Importamos las librerias hashlib y configparser
import hashlib
import configparser

#creamos el archivo de configurracion
config = configparser.ConfigParser()
#Leemos el archivo de configuracions
config.read("config.txt")
#Creamos el archivo de resultados en modo write
fo = open("result.txt","w")

#Hacemos un ciclo for del rarngo 1 al 5
for i in range(1,6):
	#Sacamos el nombre del archivo desde el archvio de configuracion
	path = config.get("config", "op" + str(i))
	#Abrimos y leemos el archivo desde el modo read binary
	file_obj = open (path, "rb")
	file = file_obj.read()
	#Aplicamos el algoritmo hash sha-256 y lo asignamos a la variable Hash
	Hash = hashlib.sha256(file)
	#Regresamos el algoritmo en cadena hexadicimal
	Hashed = Hash.hexdigest()
	#Escribimos en el archivo resultado el nombre del archivo y enseguida su clave HASH
	fo.write(path + " - " + Hashed + "\n")

#Cerramos el archivo
fo.close()
print("Las claves se han guardado exitosamente en el archivo de resultado")
