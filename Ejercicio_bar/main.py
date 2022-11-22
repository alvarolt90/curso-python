import clases

#Creación de objetos

cliente1 = clases.Cliente("Cliente1")

camarero = clases.Camarero("Camarero1")

bar = clases.Bar(cliente1, camarero)

#Atendiendo a los clientes

if __name__ == '__main__':
    camarero.servirTazaCafe(cliente1)