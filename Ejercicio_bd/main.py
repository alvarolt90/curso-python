from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            #Muestro los nombres de todas las personas
            sentencia = "SELECT nombre FROM personas"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            # Muestro las personas con email de gmail
            sentencia = "SELECT * FROM personas WHERE email LIKE '%gmail.com'"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            #Actualizo los email
            sentencia = "UPDATE personas SET email = CONCAT(left('personas', 'email', locate('@', 'personas', 'email') -1), '%gmail.com')" \ 
                        "WHERE 'personas', 'email' NOT LIKE '%gmail.com'"
            cursor.execute(sentencia)

            conexion.commit()
except Exception as e:
    print(f'Ocurrió un error: {e}')

