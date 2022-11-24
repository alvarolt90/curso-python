from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            #Muestro los nombres de todas las personas
            sentencia = "SELECT nombre FROM personas"
            nombres = (tuple(sentencia.split(',')))
            cursor.execute(sentencia, nombres)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            # Muestro las personas con email de gmail
            sentencia = "SELECT * FROM personas WHERE email LIKE '%gmail%'"
            emails = (tuple(sentencia.split(',')))
            cursor.execute(sentencia, emails)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            #Actualizo los email
            sentencia = 'UPDATE personas SET nombre=%s, apellidos=%s, email=%s'
            valores = ('')
            cursor.execute(sentencia, valores)

            conexion.commit()
except Exception as e:
    print(f'Ocurrió un error: {e}')

