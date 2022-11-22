import clases

#Creación de objetos

cliente1 = clases.Cliente("Cliente1")

camarero = clases.Camarero("Camarero1")

bar = clases.Bar(cliente1, camarero)

#Atendiendo a los clientes

camarero.servirTazaCafe(cliente1)