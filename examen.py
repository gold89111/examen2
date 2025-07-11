#productos = modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
def actualizar_precio(precio):
    if modelo in stock:
        print("precio actualizado")
        print(stock)
    else:
        print("no existe la marca")
        return False

def busqueda_de_precio(p_min,p_max):
    total= 0 
    for codigo, datos in productos.items():
        precio = stock(codigo[0])
        if precio >= p_min and precio <= p_max and stock (codigo[0])> 0:
            resultado.append()(codigo +'----'+ str(datos[0]))
    p_min = int(input("ingrese el rango minimo de precio"))
    p_max = int(input("ingrese el rango maximo del precio"))



def stock_marca(marca):


    stock = input("ingrese la marca:")



    if stock:
        print("no hay stock de esa marca lo sentimos")
    


def main():


    while True:
        modelo= {}
        stock_marca={}

        print("***MENU***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        opc = int(input("ingrese una opcion del menu:"))
        if opc == 1: 
            stock_marca(stock)
        elif opc == 2: 
            busqueda_de_precio
        elif opc == 3:
            actualizar_precio
        elif opc == 4:
            print("programa terminado...")
            break;
        else:
            print("opcion  no valida")















if (__name__ == "__main__"):
    main();        

    