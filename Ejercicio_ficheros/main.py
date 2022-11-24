import clases

#Separando los datos del archivo
if __name__ == '__main__':
    with open("alumnos-colegio.txt", "r") as datos:
        valores = []
        for linea in datos:
            valores.append([dato for dato in linea.strip().split("|")])
        #Creando los objetos
        for valor in valores:
            colegio = clases.Colegio(f"{valor[0]}")
            alumno = clases.Alumno(f"{valor[1]}", f"{valor[2]}", f"{valor[3]}")
            asignatura = clases.Asignatura(valor[4].split(";"))
            #Creando archivos a partir de los objetos
            with open(f'{valor[0]}.txt','w', encoding='utf8') as archivo:
                archivo.write(f"{valor}|\n")


#insertar 3 personas
#consultas sacando
    #- los nombres de todas las personas
    #- todos los datos de las personas que tengan un email terminado en "gmail.com"
    #- actualizar a las personas que no tengan un email de "gmail.com" y ponerselo