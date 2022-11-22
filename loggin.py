import logging as log

#Aqui activo o desactivo que nivel de log funciona, desde el nivel marcado hacia abajo
#TRACE
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

log.basicConfig(level=log.WARNING)

log.debug("Esto es un log de prueba")
