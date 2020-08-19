from producto import Producto
from repository import Repositorios


class ProductoService():

    def get_productosList(self):
        print("Listar Productos")
        return Repositorios.productosList

    def crearProducto(self):
        print("\n---CREAR PRODUCTO")
        descripcion = input("ingrese la descripcion del producto: ")
        precio = int(input("ingrese el precio: "))
        tipo = input("ingrese el tipo de libro: ")
        return Producto(descripcion, precio, tipo)

    '#AGREGAR PRODUCTO'
    def add_producto(self, producto=None):
        print("\n----AGREGAR PRODUCTO")
        if producto is None:
            producto = self.crearProducto
        lastKey = -1
        for productoKey in Repositorios.productosList:
            lastKey = productoKey
        lastKey = int(lastKey) + 1
        Repositorios.productosList[lastKey] = producto.__dict__
        return lastKey

    '#ELIMINAR PRODUCTO'
    def delete_producto(self, productoKey=None):
        print("\n----ELIMINAR PERSONA")
        if productoKey not in Repositorios.productosList:
            raise ValueError("La llave no existe")
        del Repositorios.productosList[productoKey]

    '#ACTUALIZAR PRODUCTO'
    def update_producto(self, productoKey=None, producto=None):
        print("\n----MODIFICAR PERSONA")
        if productoKey is None:
            productoKey = int(input("Ingrese una llave: "))
        if producto is None:
            producto = self.crearProducto
        Repositorios.productosList[productoKey] = producto.__dict__
