codigos = [143,568,991,321]
nombresPrecios = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]
datos = dict(zip(codigos, nombresPrecios))
pedido = [] 
print("---Bienvenido---")
cods = list(datos.keys())
print(cods)
codigo = -2
while(codigo!=-1):
    print("Lista de códigos disponibles para agregar:")
    for i in range(len(cods)) :
        print(cods[i])
    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))
    if (codigo not in cods) and (codigo!=-1):
        print("No hay ningún codigo correspondiente a un producto. Por favor ingrese otro codigo")
    if (codigo!=-1) and (codigo in cods):
        datosAInsertar = datos.get(codigo)
        pedido.append(datosAInsertar)
        print("Producto cargado con éxito") 
    elif(codigo == -1):
        print("----------------------------------------")

ListaTotal=[]
print("Tu pedido consiste de: ")
for elemento in pedido:   
    print("Nombre del producto: ", elemento[0], " | Precio: ", int(elemento[1]))
    ListaTotal.append(elemento[1])

total = 0
for numero in ListaTotal:
    total = total + numero
print("El total de sus productos es: ", total)