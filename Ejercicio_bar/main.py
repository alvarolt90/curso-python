import clases

#Creación de objetos

cliente1 = clases.Cliente("Cliente1")
cliente2 = clases.Cliente("Cliente2")
cliente3 = clases.Cliente("Cliente3")
cliente4 = clases.Cliente("Cliente4")

clientes = [cliente1, cliente2, cliente3, cliente4]

camarero = clases.Camarero("Camarero1")

bar = clases.Bar(clientes, camarero)

#Atendiendo a los clientes

while len(clientes) >= 0:
    for cliente in clientes:
        camarero.servirTazaCafe()